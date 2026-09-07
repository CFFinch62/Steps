# STEPS Language — VS Code extension

Syntax highlighting, editor behaviours, snippets and one-key running for
[STEPS](https://github.com/CFFinch62/STEPS) (`.building` and `.step` files).

## Getting STEPS

This extension highlights and runs STEPS projects — it does not bundle the
interpreter. Get it from GitHub:

**<https://github.com/CFFinch62/STEPS>**

STEPS is free and open source under the **MIT License**, as is this extension.

```sh
git clone https://github.com/CFFinch62/STEPS.git
cd STEPS
pip install -e .
```

That puts `steps` on your `PATH`. If it lives in a virtualenv, or you use the
standalone build at `~/.local/bin/steps`, point `steps.interpreterPath` at it.

## Projects, not files

This is the one extension in the suite where **Run does not run the file you
are looking at**. `steps run` and `steps check` take a project *directory* —
the one holding the `.building` file — and that is deliberate: a step belongs
to a floor of a building, and STEPS exists to make that structure real rather
than optional.

So **Run Project** walks up from whatever file you have open until it finds a
`.building`, and runs the whole project. It works the same from the
`.building` itself or from a `.step` buried three directories down. The search
stops at your workspace folder, so a stray `.building` further up your home
directory is never mistaken for the project root.

Running a single step in isolation stays a terminal job:

```sh
steps run-step path/to/one.step
```

## What it does

**Syntax highlighting** for both file types, generated from the lexer's own
tables: 27 multi-word keywords, 11 colon keywords and 50 plain keywords split
by role, plus the 56 native functions. The multi-word operators are matched
first, so `is greater than or equal to`, `storing result in`, `added to` and
`for each` highlight as single operators instead of dissolving into their
component words.

`building:`, `floor:`, `step:` and `riser:` names are scoped as definitions, so
the architectural spine of a program stands out from the code inside it.

**Editor behaviours** — `note:` comment toggling and `note block:` / `end note`
block comments, bracket matching, auto-closing pairs, and indentation that
follows the structure. It distinguishes the cases the language overloads: a
`step:` at column 0 defines a step and opens its body, while an indented
`step:` inside a `floors:` block is one entry in a list and opens nothing.
`expects:`, `belongs to:` and `returns:` are header lines, not blocks. Folding
follows indentation, because the nesting is the point.

**Snippets** for a whole building, a complete `.step` file with its header, a
riser, every control form, `attempt:` / `if unsuccessful:`, and the common
native calls.

**Commands** — each also available from the Command Palette:

| Command | Default key | What it runs |
|---|---|---|
| STEPS: Run Project | `Ctrl+F5` | `steps run <project>` |
| STEPS: Check Project | `Ctrl+Shift+F5` | `steps check <project>` |
| STEPS: Show Flow Diagram | `Ctrl+D` | `steps diagram <project>` |
| STEPS: Open REPL | — | `steps repl` |

**Show Flow Diagram** opens the ASCII diagram in a panel beside the editor,
the way the STEPS IDE does, rather than leaving it in a terminal that scrolls
away. `Ctrl+D` matches the IDE's binding.

**Problems panel** — STEPS reports `file:line:col: Error [E207]: message`, so
diagnostics land on the exact character, with the error code attached. A
runtime error's indented `Hint:` line is folded into the same diagnostic
rather than dropped, since it is usually the more useful half. **Check
Project** validates without running.

## Settings

| Setting | Default | Purpose |
|---|---|---|
| `steps.interpreterPath` | `steps` | Path to the `steps` command |
| `steps.saveBeforeRun` | `true` | Save before running or checking |
| `steps.runInTerminal` | `true` | Run in a terminal so `input` works |
| `steps.checkOnSave` | `false` | Run `steps check` on every save |
| `steps.engine` | `tree` | `tree` interpreter, or `vm` for NucleusVM bytecode |

## Installing from source

```sh
cd editors/vscode
npx @vscode/vsce package
code --install-extension steps-language-0.1.0.vsix
```

## Without the extension

`tasks.example.json` in this directory sets up check and run tasks using only
VS Code's built-in task runner and problem matcher. Note those tasks use
`${fileDirname}` and so assume the open file sits at the project root — the
extension's project search is the part a task cannot do.

## License

MIT — see [LICENSE](LICENSE).
