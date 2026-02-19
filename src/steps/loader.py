"""Steps Loader - Project Discovery and File Loading.

The loader is responsible for:
- Discovering Steps project structure
- Loading and parsing building, floor, and step files
- Validating project structure
- Registering all components with the environment
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union, cast

from .ast_nodes import BuildingNode, FloorNode, StepNode, RiserNode
from .environment import Environment, StepDefinition, RiserDefinition, FloorDefinition
from .errors import StepsError, StructureError, ErrorCode, SourceLocation
from .lexer import Lexer
from .parser import Parser, ParseResult


@dataclass
class LoadResult:
    """Result of loading a Steps project."""
    success: bool
    building: Optional[BuildingNode] = None
    errors: List[StepsError] = field(default_factory=list)

    def add_error(self, error: StepsError) -> None:
        self.errors.append(error)
        self.success = False


class Loader:
    """Loads Steps projects from the filesystem.
    
    A Steps project has the following structure:
    
    project_name/
    ├── project_name.building    # Entry point
    ├── floor_one/
    │   ├── floor_one.floor      # Floor definition
    │   ├── step_a.step
    │   └── step_b.step
    └── floor_two/
        ├── floor_two.floor
        └── step_c.step
    """
    
    def __init__(self, project_path: Path):
        """Initialize the loader.
        
        Args:
            project_path: Path to the project directory
        """
        self.project_path = Path(project_path).resolve()
        self.errors: List[Exception] = []
    
    def load(self, environment: Environment) -> LoadResult:
        """Load the entire project into the environment.
        
        Args:
            environment: The environment to populate
        
        Returns:
            LoadResult with the building AST and any errors
        """
        result = LoadResult(success=True)
        
        # Validate project directory exists
        if not self.project_path.exists():
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"Project directory '{self.project_path}' does not exist.",
                file=self.project_path,
                line=0,
                column=0,
                hint="Check that the path is correct and the directory exists."
            ))
            return result
        
        if not self.project_path.is_dir():
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"'{self.project_path}' is not a directory.",
                file=self.project_path,
                line=0,
                column=0,
                hint="Steps projects must be directories, not single files."
            ))
            return result
        
        # Find the building file
        building_name = self.project_path.name
        building_file = self.project_path / f"{building_name}.building"
        
        if not building_file.exists():
            # Try to find any .building file
            building_files = list(self.project_path.glob("*.building"))
            if building_files:
                building_file = building_files[0]
                building_name = building_file.stem
            else:
                result.add_error(StructureError(
                    code=ErrorCode.E002,
                    message=f"No building file found in '{self.project_path}'.",
                    file=self.project_path,
                    line=0,
                    column=0,
                    hint=f"Create a file named '{building_name}.building' in the project directory."
                ))
                return result
        
        # Load the building file
        building_result = self._load_building(building_file)
        if not building_result.success:
            for error in building_result.errors:
                result.add_error(error)
            return result
        
        # Type narrow: at this point ast is BuildingNode since success is True
        building_node = cast(BuildingNode, building_result.ast)
        environment.building_name = building_node.name

        # Load standard library first (project floors can override)
        self._load_stdlib(environment)

        # Load all project floors and steps
        floor_dirs = [d for d in self.project_path.iterdir() if d.is_dir()]
        for floor_dir in floor_dirs:
            floor_file = floor_dir / f"{floor_dir.name}.floor"
            if floor_file.exists():
                floor_result = self._load_floor(floor_file, floor_dir, environment)
                if not floor_result.success:
                    for error in floor_result.errors:
                        result.add_error(error)

        result.building = building_node
        return result
    
    def _get_stdlib_path(self) -> Path:
        """Get path to the bundled standard library."""
        return Path(__file__).parent / "stdlib"
    
    def _load_stdlib(self, environment: Environment) -> None:
        """Load the standard library floors.
        
        The stdlib is loaded first, so project floors can override
        stdlib definitions if they use the same names.
        """
        stdlib_path = self._get_stdlib_path()
        if not stdlib_path.exists():
            return  # No stdlib bundled, that's okay
        
        # Load each floor in stdlib
        for floor_dir in stdlib_path.iterdir():
            if floor_dir.is_dir():
                floor_file = floor_dir / f"{floor_dir.name}.floor"
                if floor_file.exists():
                    # Silently load stdlib floors (no error propagation)
                    self._load_floor(floor_file, floor_dir, environment)

    
    def _load_building(self, path: Path) -> ParseResult:
        """Load and parse a building file."""
        try:
            source = path.read_text(encoding='utf-8')
        except IOError as e:
            return ParseResult(
                ast=None,
                errors=[StructureError(
                    code=ErrorCode.E001,
                    message=f"Could not read building file: {e}",
                    file=path,
                    line=0,
                    column=0,
                    hint="Check file permissions and encoding."
                )]
            )
        
        lexer = Lexer(source, path)
        try:
            tokens = lexer.tokenize()
        except StepsError as e:
            return ParseResult(ast=None, errors=[e])
        except Exception as e:
            return ParseResult(ast=None, errors=[StructureError(
                code=ErrorCode.E001,
                message=f"Lexer error: {e}",
                file=path,
                line=0,
                column=0,
                hint="Check the file syntax."
            )])
        
        parser = Parser(tokens, path)
        return parser.parse_building()
    
    def _load_floor(
        self, 
        floor_file: Path, 
        floor_dir: Path, 
        environment: Environment
    ) -> LoadResult:
        """Load a floor and all its steps."""
        result = LoadResult(success=True)
        
        # Parse the floor file
        try:
            source = floor_file.read_text(encoding='utf-8')
        except IOError as e:
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"Could not read floor file: {e}",
                file=floor_file,
                line=0,
                column=0,
                hint="Check file permissions and encoding."
            ))
            return result
        
        lexer = Lexer(source, floor_file)
        try:
            tokens = lexer.tokenize()
        except StepsError as e:
            result.add_error(e)
            return result
        except Exception as e:
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"Lexer error: {e}",
                file=floor_file,
                line=0,
                column=0,
                hint="Check the file syntax."
            ))
            return result
        
        parser = Parser(tokens, floor_file)
        parse_result = parser.parse_floor()
        
        if not parse_result.success:
            for error in parse_result.errors:
                result.add_error(error)
            return result

        # Type narrow: at this point ast is FloorNode since success is True
        floor_node = cast(FloorNode, parse_result.ast)

        # Register the floor
        floor_def = FloorDefinition(
            name=floor_node.name,
            steps=floor_node.steps,
            file_path=floor_file
        )
        environment.register_floor(floor_def)

        # Load each step file
        for step_name in floor_node.steps:
            step_file = floor_dir / f"{step_name}.step"
            if not step_file.exists():
                result.add_error(StructureError(
                    code=ErrorCode.E003,
                    message=f"Step file '{step_name}.step' not found in floor '{floor_node.name}'.",
                    file=floor_file,
                    line=0,
                    column=0,
                    hint=f"Create the file '{step_file}' or remove '{step_name}' from the floor definition."
                ))
                continue
            
            step_result = self._load_step(step_file, environment)
            if not step_result.success:
                for error in step_result.errors:
                    result.add_error(error)
        
        return result
    
    def _load_step(self, step_file: Path, environment: Environment) -> LoadResult:
        """Load and register a step."""
        result = LoadResult(success=True)
        
        try:
            source = step_file.read_text(encoding='utf-8')
        except IOError as e:
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"Could not read step file: {e}",
                file=step_file,
                line=0,
                column=0,
                hint="Check file permissions and encoding."
            ))
            return result
        
        lexer = Lexer(source, step_file)
        try:
            tokens = lexer.tokenize()
        except StepsError as e:
            result.add_error(e)
            return result
        except Exception as e:
            result.add_error(StructureError(
                code=ErrorCode.E001,
                message=f"Lexer error: {e}",
                file=step_file,
                line=0,
                column=0,
                hint="Check the file syntax."
            ))
            return result
        
        parser = Parser(tokens, step_file)
        parse_result = parser.parse_step()
        
        if not parse_result.success:
            for error in parse_result.errors:
                result.add_error(error)
            return result

        # Type narrow: at this point ast is StepNode since success is True
        step_node = cast(StepNode, parse_result.ast)

        # Convert risers to RiserDefinitions
        risers: Dict[str, RiserDefinition] = {}
        for riser in step_node.risers:
            risers[riser.name] = RiserDefinition(
                name=riser.name,
                parameters=[p.name for p in riser.expects],
                returns=riser.returns.name if riser.returns else None,
                declarations=riser.declarations,
                body=riser.body
            )
        
        # Register the step
        step_def = StepDefinition(
            name=step_node.name,
            belongs_to=step_node.belongs_to,
            parameters=[p.name for p in step_node.expects],
            returns=step_node.returns.name if step_node.returns else None,
            body=step_node.body,
            declarations=step_node.declarations,  # Include declarations from the step
            risers=risers,
            file_path=step_file
        )
        environment.register_step(step_def)
        
        return result


def load_project(project_path: Path) -> Tuple[Optional[BuildingNode], Environment, List[StepsError]]:
    """Convenience function to load a Steps project.

    Args:
        project_path: Path to the project directory

    Returns:
        Tuple of (building AST, environment, errors)
    """
    environment = Environment()
    loader = Loader(project_path)
    result = loader.load(environment)

    return result.building, environment, result.errors


def load_building_source(source: str, name: str = "main") -> Tuple[Optional[BuildingNode], List[StepsError]]:
    """Load a building from source code (for testing/REPL).

    Args:
        source: Building source code
        name: Building name

    Returns:
        Tuple of (building AST, errors)
    """
    from .parser import parse_building

    result = parse_building(source, Path(f"{name}.building"))
    # Cast is safe because parse_building returns a BuildingNode when successful
    building = cast(Optional[BuildingNode], result.ast) if result.success else None
    return building, list(result.errors)
