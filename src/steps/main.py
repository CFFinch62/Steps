#!/usr/bin/env python3
"""Steps CLI - Command-line interface for the Steps programming language.

Usage:
    steps run <path>         Run a Steps project
    steps run-step <file>    Run a single step file for testing
    steps check <path>       Validate a Steps project without running
    steps repl               Start the interactive REPL
    steps diagram <path>     Generate flow diagram for a project
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from steps.loader import load_project, load_building_source
from steps.interpreter import run_building, ExecutionResult
from steps.errors import StepsError


def run_project(project_path: str) -> int:
    """Run a Steps project.
    
    Args:
        project_path: Path to the project directory
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    path = Path(project_path)
    
    if not path.exists():
        print(f"Error: Path '{project_path}' does not exist.", file=sys.stderr)
        return 1
    
    if not path.is_dir():
        print(f"Error: '{project_path}' is not a directory.", file=sys.stderr)
        print("Steps projects must be directories containing a .building file.", file=sys.stderr)
        return 1
    
    # Load the project
    building, environment, errors = load_project(path)
    
    if errors:
        print(f"Found {len(errors)} error(s) loading project:", file=sys.stderr)
        for error in errors:
            _print_error(error)
        return 1
    
    if building is None:
        print("Error: No building found in project.", file=sys.stderr)
        return 1
    
    # Run the program
    result = run_building(building, environment)
    
    if not result.success:
        if result.error:
            _print_error(result.error)
        return 1
    
    return 0


def check_project(project_path: str) -> int:
    """Validate a Steps project without running it.
    
    Args:
        project_path: Path to the project directory
    
    Returns:
        Exit code (0 for success, 1 for errors)
    """
    path = Path(project_path)
    
    if not path.exists():
        print(f"Error: Path '{project_path}' does not exist.", file=sys.stderr)
        return 1
    
    if not path.is_dir():
        print(f"Error: '{project_path}' is not a directory.", file=sys.stderr)
        return 1
    
    # Load the project (this validates structure and syntax)
    building, environment, errors = load_project(path)
    
    if errors:
        print(f"✗ Found {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            _print_error(error)
        return 1
    
    if building is None:
        print("✗ No building found in project.", file=sys.stderr)
        return 1
    
    # Count floors and steps
    floor_count = len(environment.floors)
    step_count = len(environment.steps)
    
    print(f"✓ Project '{building.name}' is valid")
    print(f"  {floor_count} floor(s), {step_count} step(s)")
    
    return 0


def start_repl() -> int:
    """Start the interactive REPL.
    
    Returns:
        Exit code (0 for success)
    """
    from steps_repl.repl import StepsREPL
    
    repl = StepsREPL()
    repl.run()
    return 0


def generate_diagram(project_path: str) -> int:
    """Generate flow diagram for a project.
    
    Args:
        project_path: Path to the project directory
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    path = Path(project_path)
    
    if not path.exists():
        print(f"Error: Path '{project_path}' does not exist.", file=sys.stderr)
        return 1
    
    # Load project for diagram
    building, environment, errors = load_project(path)
    
    if errors or building is None:
        print("Error: Could not load project for diagram.", file=sys.stderr)
        return 1
    
    from .diagram import generate_flow_diagram
    diagram = generate_flow_diagram(building, environment, path.resolve())
    print(diagram)
    
    return 0


def run_step(step_path: str, args: Optional[list] = None) -> int:
    """Run a single step file for testing.
    
    This wraps the step in a minimal building and executes it,
    making it easy to test steps in isolation.
    
    Args:
        step_path: Path to the .step file
        args: Optional arguments to pass to the step
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    from typing import cast, List
    from steps.lexer import Lexer
    from steps.parser import Parser
    from steps.ast_nodes import StepNode
    from steps.environment import Environment, StepDefinition
    
    path = Path(step_path)
    
    if not path.exists():
        print(f"Error: Step file '{step_path}' does not exist.", file=sys.stderr)
        return 1
    
    if not path.suffix == '.step':
        print(f"Error: '{step_path}' is not a .step file.", file=sys.stderr)
        print("Use 'steps run <path>' to run a full project.", file=sys.stderr)
        return 1
    
    # Read and parse the step file
    try:
        source = path.read_text(encoding='utf-8')
    except IOError as e:
        print(f"Error: Could not read step file: {e}", file=sys.stderr)
        return 1
    
    # Parse the step
    lexer = Lexer(source, path)
    try:
        tokens = lexer.tokenize()
    except StepsError as e:
        _print_error(e)
        return 1
    
    parser = Parser(tokens, path)
    parse_result = parser.parse_step()
    
    if not parse_result.success:
        for error in parse_result.errors:
            _print_error(error)
        return 1
    
    step_node = cast(StepNode, parse_result.ast)
    
    # Display step info
    param_names = [p.name for p in step_node.expects]
    param_str = ", ".join(param_names) if param_names else "none"
    returns_str = step_node.returns.name if step_node.returns else "nothing"
    
    print(f"Running step: {step_node.name}")
    print(f"  Expects: {param_str}")
    print(f"  Returns: {returns_str}")
    print()
    
    # Validate arguments
    if args is None:
        args = []
    
    if len(args) < len(param_names):
        print(f"Error: Step expects {len(param_names)} argument(s) ({param_str}), "
              f"but got {len(args)}.", file=sys.stderr)
        print(f"  Usage: steps run-step {step_path} --args " + 
              " ".join(f"<{p}>" for p in param_names), file=sys.stderr)
        return 1
    
    # Build argument string for the call
    formatted_args: List[str] = []
    for i, arg in enumerate(args[:len(param_names)]):
        # Try to detect if it's a number or text
        try:
            float(arg)
            formatted_args.append(arg)  # It's a number
        except ValueError:
            formatted_args.append(f'"{arg}"')  # It's text, quote it
    
    args_str = ", ".join(formatted_args) if formatted_args else ""
    
    # Create a synthetic building that calls the step
    if step_node.returns:
        building_source = f'''building: _test_harness
    call {step_node.name} with {args_str} storing result in _result
    display "Result: " added to (_result as text)
'''
    elif args_str:
        building_source = f'''building: _test_harness
    call {step_node.name} with {args_str}
'''
    else:
        building_source = f'''building: _test_harness
    call {step_node.name}
'''
    
    # Set up environment with the step registered
    environment = Environment()
    
    # Register the step
    from .environment import StepDefinition, RiserDefinition
    from typing import Dict
    
    risers: Dict[str, RiserDefinition] = {}
    for riser in step_node.risers:
        risers[riser.name] = RiserDefinition(
            name=riser.name,
            parameters=[p.name for p in riser.expects],
            returns=riser.returns.name if riser.returns else None,
            declarations=riser.declarations,
            body=riser.body
        )
    
    step_def = StepDefinition(
        name=step_node.name,
        belongs_to=step_node.belongs_to or "_test",
        parameters=param_names,
        returns=step_node.returns.name if step_node.returns else None,
        body=step_node.body,
        declarations=step_node.declarations,  # Include declarations from the step
        risers=risers,
        file_path=path
    )
    environment.register_step(step_def)
    
    # Parse the synthetic building
    building, errors = load_building_source(building_source, "_test_harness")
    
    if errors:
        print("Internal error: Could not create test harness.", file=sys.stderr)
        for error in errors:
            _print_error(error)
        return 1
    
    if building is None:
        print("Internal error: No building created.", file=sys.stderr)
        return 1
    
    # Run the program
    result = run_building(building, environment)
    
    if not result.success:
        if result.error:
            _print_error(result.error)
        return 1
    
    return 0


def _print_error(error: StepsError) -> None:
    """Print a Steps error in a user-friendly format."""
    location = ""
    if error.file and error.line:
        location = f"{error.file}:{error.line}"
        if error.column:
            location += f":{error.column}"
        location += ": "

    print(f"{location}Error [{error.code}]: {error.message}", file=sys.stderr)

    if error.hint:
        print(f"  Hint: {error.hint}", file=sys.stderr)


def main() -> int:
    """Main entry point for the Steps CLI."""
    parser = argparse.ArgumentParser(
        prog="steps",
        description="Steps Programming Language - Educational programming with visible structure"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # run command
    run_parser = subparsers.add_parser("run", help="Run a Steps project")
    run_parser.add_argument("path", help="Path to the project directory")

    # check command
    check_parser = subparsers.add_parser("check", help="Validate a Steps project")
    check_parser.add_argument("path", help="Path to the project directory")

    # repl command
    repl_parser = subparsers.add_parser("repl", help="Start interactive REPL")

    # diagram command
    diagram_parser = subparsers.add_parser("diagram", help="Generate flow diagram")
    diagram_parser.add_argument("path", help="Path to the project directory")

    # run-step command
    run_step_parser = subparsers.add_parser("run-step", help="Run a single step file for testing")
    run_step_parser.add_argument("path", help="Path to the .step file")
    run_step_parser.add_argument("--args", nargs="*", default=[], help="Arguments to pass to the step")

    args = parser.parse_args()

    if args.command == "run":
        return run_project(args.path)
    elif args.command == "check":
        return check_project(args.path)
    elif args.command == "repl":
        return start_repl()
    elif args.command == "diagram":
        return generate_diagram(args.path)
    elif args.command == "run-step":
        return run_step(args.path, args.args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())

