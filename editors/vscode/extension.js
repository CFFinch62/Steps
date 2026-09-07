// STEPS Language extension — project-level run/check/diagram for .building
// and .step files.
//
// Syntax highlighting, editor behaviours and snippets are entirely
// declarative (package.json + the grammar + language-configuration.json);
// none of them need this file. What this file exists for is the thing that
// makes STEPS different from every other language in this suite: `steps run`
// and `steps check` take a PROJECT DIRECTORY, not a file. So the commands
// resolve the project that owns whatever you happen to have open, and run
// the whole thing.
//
// Running one step in isolation stays a terminal job (`steps run-step`), by
// design: a step belongs to a floor of a building, and the language is about
// that structure being real rather than optional.

const vscode = require('vscode');
const cp = require('child_process');
const fs = require('fs');
const path = require('path');

/** `steps check` and a failing `steps run` both report
 *  `<file>:<line>:<col>: Error [E207]: <message>`. A runtime error adds an
 *  indented `Hint:` line, which is folded into the message below. */
const DIAGNOSTIC_RE =
  /^(.*?):(\d+):(\d+):\s+(Error|Warning)\s*(?:\[([A-Z]\d+)\])?:\s*(.*)$/;
const HINT_RE = /^\s+Hint:\s*(.*)$/;

let diagnostics = null;
let output = null;

function config() {
  return vscode.workspace.getConfiguration('steps');
}

function interpreter() {
  return config().get('interpreterPath', 'steps') || 'steps';
}

function shellQuote(p) {
  if (process.platform === 'win32') return `"${p}"`;
  return `'${String(p).replace(/'/g, `'\\''`)}'`;
}

/** Find the project that owns `filePath`: the nearest directory at or above
 *  it that holds a `*.building` file.
 *
 *  A `.building` file IS the project root marker — `steps run` wants the
 *  directory containing it, and rejects the file itself — so this walks up
 *  from the active file until it finds one, stopping at the workspace folder
 *  or the filesystem root. That is what lets Run work from a `.step` buried
 *  in a subdirectory. */
function findProjectDir(filePath) {
  const roots = (vscode.workspace.workspaceFolders || []).map((f) =>
    path.resolve(f.uri.fsPath)
  );

  let dir = path.dirname(path.resolve(filePath));
  for (;;) {
    let entries;
    try {
      entries = fs.readdirSync(dir);
    } catch {
      return null;
    }
    if (entries.some((e) => e.toLowerCase().endsWith('.building'))) return dir;

    // Stop once we leave every workspace folder, so a stray .building
    // somewhere up near $HOME is never mistaken for this project's root.
    if (roots.length && roots.includes(dir)) return null;

    const parent = path.dirname(dir);
    if (parent === dir) return null;
    dir = parent;
  }
}

async function activeProject() {
  const editor = vscode.window.activeTextEditor;
  if (!editor || editor.document.languageId !== 'steps') {
    vscode.window.showErrorMessage(
      'STEPS: no .building or .step file is active.'
    );
    return null;
  }
  if (config().get('saveBeforeRun', true) && editor.document.isDirty) {
    await editor.document.save();
  }

  const projectDir = findProjectDir(editor.document.fileName);
  if (!projectDir) {
    vscode.window.showErrorMessage(
      'STEPS: no .building file found in this file’s directory or above it. ' +
        'A STEPS project is the directory that holds its .building file.'
    );
    return null;
  }
  return { doc: editor.document, projectDir };
}

/** Run in the integrated terminal — output appears live and `input` works. */
function runInTerminal(projectDir, args) {
  let term = vscode.window.terminals.find((t) => t.name === 'STEPS');
  if (!term) {
    term = vscode.window.createTerminal({ name: 'STEPS', cwd: projectDir });
  }
  term.show(true);
  const isFlag = (a) => /^--[a-z-]+$/.test(a);
  const parts = [
    shellQuote(interpreter()),
    ...args.map((a) => (isFlag(a) ? a : shellQuote(a))),
  ];
  term.sendText(parts.join(' '));
}

/** Run as a child process — output goes to an Output channel and diagnostics
 *  become squiggles via the Problems panel. */
function runInOutputChannel(projectDir, args, label, onDone) {
  if (!output) output = vscode.window.createOutputChannel('STEPS');
  output.clear();
  output.show(true);

  const exe = interpreter();
  output.appendLine(`> ${exe} ${args.join(' ')}`);
  output.appendLine('');

  const started = Date.now();
  const child = cp.spawn(exe, args, { cwd: projectDir });

  // STEPS prints diagnostics on stdout for `check` and stderr for a failing
  // run, so both streams are scanned.
  let combined = '';
  child.stdout.on('data', (d) => {
    const t = d.toString();
    combined += t;
    output.append(t);
  });
  child.stderr.on('data', (d) => {
    const t = d.toString();
    combined += t;
    output.append(t);
  });

  child.on('error', (err) => reportSpawnError(err, exe));

  child.on('close', (code) => {
    publishDiagnostics(projectDir, combined);
    output.appendLine('');
    output.appendLine(
      `[${label} exit ${code} in ${((Date.now() - started) / 1000).toFixed(2)}s]`
    );
    if (onDone) onDone(code, combined);
  });

  child.stdin.end();
}

function reportSpawnError(err, exe) {
  if (err.code === 'ENOENT') {
    vscode.window
      .showErrorMessage(
        `STEPS: '${exe}' not found. Run 'pip install -e .' in the STEPS repo, or set steps.interpreterPath.`,
        'Open Settings'
      )
      .then((choice) => {
        if (choice === 'Open Settings') {
          vscode.commands.executeCommand(
            'workbench.action.openSettings',
            'steps.interpreterPath'
          );
        }
      });
  } else {
    vscode.window.showErrorMessage(`STEPS: ${err.message}`);
  }
}

/** Turn `file:line:col: Error [CODE]: message` into editor squiggles, folding
 *  a following indented `Hint:` line into the same diagnostic rather than
 *  dropping the most useful half of the message. */
function publishDiagnostics(projectDir, text) {
  const byFile = new Map();
  let last = null;

  for (const raw of text.split('\n')) {
    const line = raw.replace(/\r$/, '');

    const hint = HINT_RE.exec(line);
    if (hint && last) {
      last.message = `${last.message}\nHint: ${hint[1]}`;
      continue;
    }

    const m = DIAGNOSTIC_RE.exec(line);
    if (!m) continue;

    const [, file, lineNo, colNo, severity, code, message] = m;
    const pos = new vscode.Position(
      Math.max(0, parseInt(lineNo, 10) - 1),
      Math.max(0, parseInt(colNo, 10) - 1)
    );
    const uri = vscode.Uri.file(path.resolve(projectDir, file));

    const diag = new vscode.Diagnostic(
      new vscode.Range(pos, pos),
      message,
      severity === 'Warning'
        ? vscode.DiagnosticSeverity.Warning
        : vscode.DiagnosticSeverity.Error
    );
    diag.source = 'steps';
    if (code) diag.code = code;

    const key = uri.toString();
    if (!byFile.has(key)) byFile.set(key, { uri, items: [] });
    byFile.get(key).items.push(diag);
    last = diag;
  }

  diagnostics.clear();
  for (const { uri, items } of byFile.values()) {
    diagnostics.set(uri, items);
  }
}

function checkQuietly(doc) {
  const projectDir = findProjectDir(doc.fileName);
  if (!projectDir) return;

  const child = cp.spawn(interpreter(), ['check', projectDir], {
    cwd: projectDir,
  });
  let combined = '';
  child.stdout.on('data', (d) => (combined += d.toString()));
  child.stderr.on('data', (d) => (combined += d.toString()));
  child.on('error', () => {});
  child.on('close', () => publishDiagnostics(projectDir, combined));
  child.stdin.end();
}

async function runProject() {
  const ctx = await activeProject();
  if (!ctx) return;
  const engine = config().get('engine', 'tree');
  const args = ['run'];
  if (engine && engine !== 'tree') args.push('--engine', engine);
  args.push(ctx.projectDir);

  if (config().get('runInTerminal', true)) runInTerminal(ctx.projectDir, args);
  else runInOutputChannel(ctx.projectDir, args, 'run');
}

async function checkProject() {
  const ctx = await activeProject();
  if (!ctx) return;
  runInOutputChannel(ctx.projectDir, ['check', ctx.projectDir], 'check');
}

/** The IDE shows the flow diagram in a panel, so do the same rather than
 *  leaving ASCII art in a terminal that scrolls away. */
async function showDiagram() {
  const ctx = await activeProject();
  if (!ctx) return;

  const exe = interpreter();
  cp.execFile(
    exe,
    ['diagram', ctx.projectDir],
    { cwd: ctx.projectDir, maxBuffer: 8 * 1024 * 1024 },
    (err, stdout, stderr) => {
      if (err && err.code === 'ENOENT') return reportSpawnError(err, exe);

      const body = (stdout || '') + (stderr || '');
      if (!body.trim()) {
        vscode.window.showInformationMessage(
          'STEPS: the diagram command produced no output.'
        );
        return;
      }

      const panel = vscode.window.createWebviewPanel(
        'stepsDiagram',
        `STEPS diagram — ${path.basename(ctx.projectDir)}`,
        vscode.ViewColumn.Beside,
        {}
      );
      panel.webview.html = diagramHtml(body);
    }
  );
}

function escapeHtml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/** The diagram is ASCII art, so it needs a monospace font and no wrapping.
 *  Colours come from VS Code's own theme variables so it matches the editor. */
function diagramHtml(text) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline';">
<style>
  body {
    margin: 0;
    padding: 1rem;
    background: var(--vscode-editor-background);
    color: var(--vscode-editor-foreground);
    font-family: var(--vscode-editor-font-family, monospace);
    font-size: var(--vscode-editor-font-size, 13px);
  }
  pre { margin: 0; white-space: pre; overflow-x: auto; }
</style>
</head>
<body><pre>${escapeHtml(text)}</pre></body>
</html>`;
}

function openRepl() {
  const term = vscode.window.createTerminal({ name: 'STEPS REPL' });
  term.show(true);
  term.sendText(`${shellQuote(interpreter())} repl`);
}

function activate(context) {
  diagnostics = vscode.languages.createDiagnosticCollection('steps');

  context.subscriptions.push(
    diagnostics,
    vscode.commands.registerCommand('steps.runProject', runProject),
    vscode.commands.registerCommand('steps.checkProject', checkProject),
    vscode.commands.registerCommand('steps.diagram', showDiagram),
    vscode.commands.registerCommand('steps.repl', openRepl),

    // A file's errors are stale the moment it is edited.
    vscode.workspace.onDidChangeTextDocument((e) => {
      if (e.document.languageId === 'steps') {
        diagnostics.delete(e.document.uri);
      }
    }),

    vscode.workspace.onDidSaveTextDocument((doc) => {
      if (doc.languageId === 'steps' && config().get('checkOnSave', false)) {
        checkQuietly(doc);
      }
    })
  );
}

function deactivate() {
  if (output) output.dispose();
}

module.exports = { activate, deactivate };
