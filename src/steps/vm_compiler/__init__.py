"""AST-to-NucleusVM-bytecode compiler for STEPS.

This is a *new*, additive execution path — see `compiler.py`'s module
docstring for the language subset covered and why (NucleusVM's own
dev-docs/PLAN.md has the full rationale). Nothing in the existing
tree-walking interpreter (`interpreter.py` and friends) is touched by
this package.
"""
from nucleus_vm import VM

from .compiler import VMCompiler, compile_program
from .natives import build_natives

__all__ = ["VMCompiler", "compile_program", "build_natives", "run_building_vm"]


def run_building_vm(building, environment, output_func=None):
    """Compile and run a loaded (building, environment) pair — the same
    pair `Loader.load()`/`load_project()` already produce — through
    NucleusVM instead of the tree-walking interpreter.

    `output_func` defaults to `environment.output_handler` (matching how
    `display` already routes output in the tree-walker) so callers can
    override it the same way they would set `environment.output_handler`
    directly.
    """
    if output_func is None:
        output_func = environment.output_handler

    chunk = compile_program(building, environment)
    vm = VM(natives=build_natives(output_func))
    return vm.run(chunk)
