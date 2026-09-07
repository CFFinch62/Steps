# NucleusVM parked; dependency made optional

**Date:** 2026-09-07

## What changed

NucleusVM did not deliver the speed-up it was built for when measured, so the
experiment is parked. The compiler (`src/steps/vm_compiler/`) and the
`--engine vm` flag both still work and are kept for reference — nothing was
removed.

What did change is how the dependency is declared.

### The problem

`pyproject.toml` listed NucleusVM as a **hard runtime dependency, pinned to an
absolute path on one machine**:

```toml
dependencies = [
    ...,
    "nucleus-vm @ file:///home/chuck/Dropbox/.../LANGUAGES/NucleusVM",
]
```

STEPS is a public repository. Anyone who cloned it and ran `pip install -e .`
hit an installation failure, because that path does not exist on their machine
— and it failed for a package the default execution path never touches.

### The fix

- `nucleus-vm` moved out of `dependencies` into a new `vm` optional extra.
- `run_project()` in `src/steps/main.py` now catches `ImportError` around the
  lazy `steps.vm_compiler` import and reports what is missing, rather than
  surfacing a raw traceback:

  ```
  steps: --engine vm needs NucleusVM, which is not installed.
         Install it with:  pip install -e '.[vm]'
         (or drop --engine vm to use the default interpreter)
  ```

- The README's NucleusVM section says the engine is parked and not installed
  by default, and how to install it from the sibling checkout.
- The VS Code extension's `steps.engine` setting says the same, so the `vm`
  option is not presented as if it were ready to use.

NucleusVM is not on PyPI, so the `vm` extra resolves only against a local
checkout: `pip install -e ../NucleusVM`.

## Verified

- A clean `python -m venv` + `pip install -e .` from a bare checkout now
  succeeds, and `steps run` / `steps check` work in it.
- `--engine vm` in that environment reports the missing dependency and exits 1.
- In a venv that *does* have NucleusVM, `--engine vm` still runs correctly.
- Test suite unchanged: 450 passed.

---

## Follow-up: the other heavyweight dependencies (2026-09-07)

The same audit turned up three more required dependencies that the installed
package never uses.

`fastapi` and `uvicorn` are imported only by `steps-web/backend/`, which is
**not shipped** — `packages = ["src/steps", "src/steps_ide"]`. Nothing you
pip-install imports them. `PyQt6` and `PyQt6-WebEngine` are used by
`src/steps_ide`, but were listed *both* as required dependencies and in the
`ide` extra.

Net effect: `pip install -e .` downloaded Qt and a web framework in order to
run `steps run` in a terminal, which needs neither.

### The fix

- `dependencies` is now empty. The language core is standard library only.
- `fastapi`/`uvicorn` moved to a new `web` extra.
- `PyQt6`/`PyQt6-WebEngine` are now *only* in the existing `ide` extra.
- `src/steps_ide/main.py` catches the PyQt6 `ImportError` and reports which
  extra to install rather than dying on a traceback.
- `setup.sh` now runs `pip install -e ".[ide,serial]"` instead of installing
  PyQt6 and pyserial by name. Same result, declared in one place.
- The README's install section documents the extras. It previously said to
  `pip install textual watchfiles` for the IDE — stale from an earlier TUI
  design; the PyQt6 IDE uses neither.

**Local workflow is unchanged.** `./setup.sh` still produces a full
install with the IDE and serial support; verified end to end in a clean venv,
including launching `steps-ide`.

### Verified

- `pip install -e ".[ide,serial]"` in a clean venv: PyQt6 and pyserial
  present, `steps-ide` launches, CLI works.
- Bare `pip install -e .` in a clean venv: **zero** third-party packages,
  `steps run` works, `steps-ide` prints the install hint and exits 1.
- Existing dev venv unaffected; 450 tests pass.
