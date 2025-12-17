"""Steps Interpreter - AST Execution Engine.

The interpreter executes Steps programs by walking the AST and evaluating
each node. It uses the visitor pattern to handle different node types.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

from .ast_nodes import (
    # Top-level nodes
    ASTNode, BuildingNode, FloorNode, StepNode, RiserNode,
    # Declaration nodes
    ParameterNode, ReturnDeclaration, DeclarationNode,
    # Statement nodes
    StatementNode, DisplayStatement, SetStatement, SetIndexStatement, CallStatement,
    ReturnStatement, ExitStatement, IfStatement, IfBranch,
    RepeatTimesStatement, RepeatForEachStatement, RepeatWhileStatement,
    AttemptStatement, NoteStatement, AddToListStatement, RemoveFromListStatement,
    # Expression nodes
    ExpressionNode, NumberLiteral, TextLiteral, BooleanLiteral, NothingLiteral,
    ListLiteral, TableLiteral, IdentifierNode, InputNode,
    BinaryOpNode, UnaryOpNode, TypeConversionNode, TableAccessNode,
    AddedToNode, SplitByNode, CharacterAtNode, LengthOfNode,
    ContainsNode, StartsWithNode, EndsWithNode, IsInNode,
)
from .environment import Environment, StepDefinition
from .types import (
    StepsValue, StepsNumber, StepsText, StepsBoolean, 
    StepsList, StepsTable, StepsNothing, make_value
)
from .errors import (
    StepsError, StepsRuntimeError, StepsTypeError, 
    SourceLocation, ErrorCode
)
from . import builtins


class ReturnValue(Exception):
    """Exception used to propagate return values up the call stack."""
    def __init__(self, value: StepsValue):
        self.value = value


class ExitProgram(Exception):
    """Exception used to signal program termination."""
    pass


class AttemptFailed(Exception):
    """Exception used to signal a failed attempt block."""
    def __init__(self, original_error: StepsError):
        self.original_error = original_error


@dataclass
class ExecutionResult:
    """Result of executing a Steps program."""
    success: bool
    return_value: Optional[StepsValue] = None
    error: Optional[StepsError] = None
    output_lines: Optional[List[str]] = None

    def __post_init__(self) -> None:
        if self.output_lines is None:
            self.output_lines = []


class Interpreter:
    """Executes Steps programs by walking the AST.
    
    Uses the visitor pattern to handle different node types.
    Maintains an environment for variable scopes and step registry.
    """
    
    def __init__(self, environment: Optional[Environment] = None):
        """Initialize the interpreter.
        
        Args:
            environment: Optional pre-configured environment
        """
        self.env = environment or Environment()
        self.output_lines: List[str] = []
        
        # Override output handler to capture output
        self._original_output = self.env.output_handler
        self.env.output_handler = self._capture_output
    
    def _capture_output(self, message: str) -> None:
        """Capture output for testing and also send to original handler."""
        self.output_lines.append(message)
        self._original_output(message)
    
    # =========================================================================
    # Main Entry Points
    # =========================================================================
    
    def run_building(self, building: BuildingNode) -> ExecutionResult:
        """Execute a building program.
        
        Args:
            building: The building AST to execute
        
        Returns:
            ExecutionResult with success status and any output
        """
        self.output_lines = []
        
        try:
            self.env.building_name = building.name
            
            # Execute the building body
            for statement in building.body:
                self.execute_statement(statement)
            
            return ExecutionResult(
                success=True,
                output_lines=self.output_lines.copy()
            )
        
        except ExitProgram:
            # Normal exit
            return ExecutionResult(
                success=True,
                output_lines=self.output_lines.copy()
            )
        
        except StepsError as e:
            return ExecutionResult(
                success=False,
                error=e,
                output_lines=self.output_lines.copy()
            )
        
        except Exception as e:
            # Unexpected error
            return ExecutionResult(
                success=False,
                error=StepsRuntimeError(
                    code=ErrorCode.E407,
                    message=f"Internal error: {str(e)}",
                    file=Path("<unknown>"),
                    line=0,
                    column=0,
                    hint="This is likely a bug in the Steps interpreter."
                ),
                output_lines=self.output_lines.copy()
            )
    
    def call_step(
        self, 
        step_name: str, 
        arguments: List[StepsValue],
        location: Optional[SourceLocation] = None
    ) -> StepsValue:
        """Call a step and return its result.
        
        Args:
            step_name: Name of the step to call
            arguments: Arguments to pass
            location: Source location for error messages
        
        Returns:
            The step's return value (or StepsNothing)
        """
        # Get step definition
        step_def = self.env.get_step(step_name, location)
        
        # Check recursion
        if self.env.is_recursive(step_name):
            raise StepsRuntimeError(
                code=ErrorCode.E408,
                message=f"Maximum recursion depth exceeded when calling '{step_name}'.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=f"Call stack: {self.env.get_call_stack_string()}"
            )
        
        # Check argument count
        if len(arguments) != len(step_def.parameters):
            raise StepsRuntimeError(
                code=ErrorCode.E409,
                message=f"Step '{step_name}' expects {len(step_def.parameters)} argument(s), got {len(arguments)}.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=f"Expected parameters: {', '.join(step_def.parameters) or '(none)'}"
            )
        
        # Enter step context
        with self.env.step_context(step_name):
            # Bind arguments to parameters
            for param_name, arg_value in zip(step_def.parameters, arguments):
                self.env.set_variable(param_name, arg_value, is_declaration=True)

            # Register risers in current scope
            self._current_risers = step_def.risers

            # Execute step body
            try:
                for statement in step_def.body:
                    self.execute_statement(statement)

                # No explicit return
                return StepsNothing()

            except ReturnValue as rv:
                return rv.value

        # This should never be reached, but satisfies type checker
        return StepsNothing()
    
    # =========================================================================
    # Statement Execution
    # =========================================================================
    
    def execute_statement(self, stmt: StatementNode) -> None:
        """Execute a statement."""
        if isinstance(stmt, DisplayStatement):
            self._exec_display(stmt)
        elif isinstance(stmt, SetStatement):
            self._exec_set(stmt)
        elif isinstance(stmt, SetIndexStatement):
            self._exec_set_index(stmt)
        elif isinstance(stmt, CallStatement):
            self._exec_call(stmt)
        elif isinstance(stmt, ReturnStatement):
            self._exec_return(stmt)
        elif isinstance(stmt, ExitStatement):
            self._exec_exit(stmt)
        elif isinstance(stmt, IfStatement):
            self._exec_if(stmt)
        elif isinstance(stmt, RepeatTimesStatement):
            self._exec_repeat_times(stmt)
        elif isinstance(stmt, RepeatForEachStatement):
            self._exec_repeat_for_each(stmt)
        elif isinstance(stmt, RepeatWhileStatement):
            self._exec_repeat_while(stmt)
        elif isinstance(stmt, AttemptStatement):
            self._exec_attempt(stmt)
        elif isinstance(stmt, AddToListStatement):
            self._exec_add_to_list(stmt)
        elif isinstance(stmt, RemoveFromListStatement):
            self._exec_remove_from_list(stmt)
        elif isinstance(stmt, NoteStatement):
            pass  # Notes are comments, do nothing
        else:
            raise StepsRuntimeError(
                code=ErrorCode.E407,
                message=f"Unknown statement type: {type(stmt).__name__}",
                file=stmt.location.file,
                line=stmt.location.line,
                column=stmt.location.column,
                hint="This is likely a bug in the Steps interpreter."
            )
    
    def _exec_display(self, stmt: DisplayStatement) -> None:
        """Execute: display expression"""
        value = self.evaluate_expression(stmt.expression)
        self.env.write_output(value.display_string())
    
    def _exec_set(self, stmt: SetStatement) -> None:
        """Execute: set target to value"""
        value = self.evaluate_expression(stmt.value)
        self.env.set_variable(stmt.target, value, stmt.location)
    
    def _exec_set_index(self, stmt: SetIndexStatement) -> None:
        """Execute: set target[index] to value"""
        # Get the container (list or table)
        container = self.env.get_variable(stmt.target, stmt.location)
        # Evaluate the index/key
        key = self.evaluate_expression(stmt.index)
        # Evaluate the value
        value = self.evaluate_expression(stmt.value)
        # Use builtins to set the value
        builtins.table_set(container, key, value, stmt.location)
    
    def _exec_call(self, stmt: CallStatement) -> None:
        """Execute: call step_name [with args] [storing result in var]"""
        # Evaluate arguments
        arg_values = [self.evaluate_expression(arg) for arg in stmt.arguments]
        
        # Check if it's a riser call
        if hasattr(self, '_current_risers') and stmt.step_name in self._current_risers:
            result = self._call_riser(stmt.step_name, arg_values, stmt.location)
        else:
            # Regular step call
            result = self.call_step(stmt.step_name, arg_values, stmt.location)
        
        # Store result if requested
        if stmt.result_target:
            self.env.set_variable(stmt.result_target, result, stmt.location)
    
    def _call_riser(
        self, 
        riser_name: str, 
        arguments: List[StepsValue],
        location: Optional[SourceLocation]
    ) -> StepsValue:
        """Call a riser (private helper function)."""
        riser_def = self._current_risers[riser_name]
        
        # Check argument count
        if len(arguments) != len(riser_def.parameters):
            raise StepsRuntimeError(
                code=ErrorCode.E409,
                message=f"Riser '{riser_name}' expects {len(riser_def.parameters)} argument(s), got {len(arguments)}.",
                file=location.file if location else Path("<unknown>"),
                line=location.line if location else 0,
                column=location.column if location else 0,
                hint=f"Expected parameters: {', '.join(riser_def.parameters) or '(none)'}"
            )
        
        # New scope for riser
        self.env.push_scope()
        try:
            # Bind arguments
            for param_name, arg_value in zip(riser_def.parameters, arguments):
                self.env.set_variable(param_name, arg_value, is_declaration=True)
            
            # Execute riser body
            try:
                for statement in riser_def.body:
                    self.execute_statement(statement)
                return StepsNothing()
            except ReturnValue as rv:
                return rv.value
        finally:
            self.env.pop_scope()
    
    def _exec_return(self, stmt: ReturnStatement) -> None:
        """Execute: return [value]"""
        if stmt.value:
            value = self.evaluate_expression(stmt.value)
        else:
            value = StepsNothing()
        raise ReturnValue(value)
    
    def _exec_exit(self, stmt: ExitStatement) -> None:
        """Execute: exit"""
        raise ExitProgram()
    
    def _exec_if(self, stmt: IfStatement) -> None:
        """Execute: if ... otherwise if ... otherwise"""
        # Check main if branch
        condition = self.evaluate_expression(stmt.if_branch.condition)
        if condition.is_truthy():
            self._execute_block(stmt.if_branch.body)
            return
        
        # Check otherwise if branches
        for branch in stmt.otherwise_if_branches:
            condition = self.evaluate_expression(branch.condition)
            if condition.is_truthy():
                self._execute_block(branch.body)
                return
        
        # Otherwise branch
        if stmt.otherwise_branch:
            self._execute_block(stmt.otherwise_branch)
    
    def _exec_repeat_times(self, stmt: RepeatTimesStatement) -> None:
        """Execute: repeat N times"""
        count_value = self.evaluate_expression(stmt.count)
        
        if not isinstance(count_value, StepsNumber):
            raise StepsTypeError(
                code=ErrorCode.E302,
                message=f"'repeat ... times' requires a number, got {count_value.type_name()}.",
                file=stmt.location.file,
                line=stmt.location.line,
                column=stmt.location.column,
                hint="The repeat count must be a number."
            )
        
        count = int(count_value.value)
        for _ in range(count):
            self._execute_block(stmt.body)
    
    def _exec_repeat_for_each(self, stmt: RepeatForEachStatement) -> None:
        """Execute: repeat for each item in collection"""
        collection = self.evaluate_expression(stmt.collection)
        
        if isinstance(collection, StepsList):
            items = list(collection)
        elif isinstance(collection, StepsText):
            # Iterate over characters
            items = [StepsText(c) for c in collection.value]
        elif isinstance(collection, StepsTable):
            # Iterate over keys
            items = [StepsText(k) for k in collection.pairs.keys()]
        else:
            raise StepsTypeError(
                code=ErrorCode.E302,
                message=f"Cannot iterate over {collection.type_name()}.",
                file=stmt.location.file,
                line=stmt.location.line,
                column=stmt.location.column,
                hint="'for each' works with lists, text, and tables."
            )
        
        for item in items:
            self.env.push_scope()
            try:
                self.env.set_variable(stmt.item_name, item, is_declaration=True)
                self._execute_block(stmt.body)
            finally:
                self.env.pop_scope()
    
    def _exec_repeat_while(self, stmt: RepeatWhileStatement) -> None:
        """Execute: repeat while condition"""
        max_iterations = 10000  # Safety limit
        iterations = 0
        
        while True:
            condition = self.evaluate_expression(stmt.condition)
            if not condition.is_truthy():
                break
            
            self._execute_block(stmt.body)
            
            iterations += 1
            if iterations >= max_iterations:
                raise StepsRuntimeError(
                    code=ErrorCode.E410,
                    message="Maximum loop iterations exceeded (10000).",
                    file=stmt.location.file,
                    line=stmt.location.line,
                    column=stmt.location.column,
                    hint="Your loop may be infinite. Check the condition."
                )
    
    def _exec_attempt(self, stmt: AttemptStatement) -> None:
        """Execute: attempt: ... if unsuccessful: ... then continue:"""
        try:
            self._execute_block(stmt.attempt_body)
            
            # Success - execute continue block
            if stmt.continue_body:
                self._execute_block(stmt.continue_body)
        
        except StepsError as e:
            # Failure - execute unsuccessful block
            if stmt.unsuccessful_body:
                self._execute_block(stmt.unsuccessful_body)
            
            # Then continue if specified
            if stmt.continue_body:
                self._execute_block(stmt.continue_body)
    
    def _exec_add_to_list(self, stmt: AddToListStatement) -> None:
        """Execute: add item to list_name"""
        item = self.evaluate_expression(stmt.item)
        lst = self.env.get_variable(stmt.list_name, stmt.location)
        builtins.list_add(lst, item, stmt.location)
    
    def _exec_remove_from_list(self, stmt: RemoveFromListStatement) -> None:
        """Execute: remove item from list_name"""
        item = self.evaluate_expression(stmt.item)
        lst = self.env.get_variable(stmt.list_name, stmt.location)
        builtins.list_remove(lst, item, stmt.location)
    
    def _execute_block(self, statements: List[StatementNode]) -> None:
        """Execute a block of statements."""
        for statement in statements:
            self.execute_statement(statement)
    
    # =========================================================================
    # Expression Evaluation
    # =========================================================================
    
    def evaluate_expression(self, expr: ExpressionNode) -> StepsValue:
        """Evaluate an expression and return its value."""
        # Literals
        if isinstance(expr, NumberLiteral):
            return StepsNumber(expr.value)
        
        if isinstance(expr, TextLiteral):
            return StepsText(expr.value)
        
        if isinstance(expr, BooleanLiteral):
            return StepsBoolean(expr.value)
        
        if isinstance(expr, NothingLiteral):
            return StepsNothing()
        
        if isinstance(expr, ListLiteral):
            elements = [self.evaluate_expression(e) for e in expr.elements]
            return StepsList(elements)
        
        if isinstance(expr, TableLiteral):
            pairs = {}
            for key_expr, value_expr in expr.pairs:
                key = self.evaluate_expression(key_expr).as_text().value
                value = self.evaluate_expression(value_expr)
                pairs[key] = value
            return StepsTable(pairs)
        
        # References
        if isinstance(expr, IdentifierNode):
            return self.env.get_variable(expr.name, expr.location)
        
        if isinstance(expr, InputNode):
            text = self.env.read_input()
            return StepsText(text)
        
        # Binary operations
        if isinstance(expr, BinaryOpNode):
            return self._eval_binary_op(expr)
        
        # Unary operations
        if isinstance(expr, UnaryOpNode):
            return self._eval_unary_op(expr)
        
        # Type conversion
        if isinstance(expr, TypeConversionNode):
            return self._eval_type_conversion(expr)
        
        # Collection access
        if isinstance(expr, TableAccessNode):
            return self._eval_table_access(expr)
        
        # Text operations
        if isinstance(expr, AddedToNode):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            return builtins.text_concatenate(left, right, expr.location)
        
        if isinstance(expr, SplitByNode):
            split_text = self.evaluate_expression(expr.text)
            delimiter = self.evaluate_expression(expr.delimiter)
            return builtins.text_split(split_text, delimiter, expr.location)

        if isinstance(expr, CharacterAtNode):
            char_text = self.evaluate_expression(expr.text)
            index = self.evaluate_expression(expr.index)
            return builtins.text_character_at(char_text, index, expr.location)

        if isinstance(expr, LengthOfNode):
            len_collection = self.evaluate_expression(expr.collection)
            return builtins.text_length(len_collection, expr.location)

        if isinstance(expr, ContainsNode):
            contains_text = self.evaluate_expression(expr.text)
            substring = self.evaluate_expression(expr.substring)
            return builtins.text_contains(contains_text, substring, expr.location)

        if isinstance(expr, StartsWithNode):
            starts_text = self.evaluate_expression(expr.text)
            prefix = self.evaluate_expression(expr.prefix)
            return builtins.text_starts_with(starts_text, prefix, expr.location)

        if isinstance(expr, EndsWithNode):
            ends_text = self.evaluate_expression(expr.text)
            suffix = self.evaluate_expression(expr.suffix)
            return builtins.text_ends_with(ends_text, suffix, expr.location)
        
        if isinstance(expr, IsInNode):
            item = self.evaluate_expression(expr.item)
            collection = self.evaluate_expression(expr.collection)
            return builtins.list_contains(collection, item, expr.location)
        
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Unknown expression type: {type(expr).__name__}",
            file=expr.location.file,
            line=expr.location.line,
            column=expr.location.column,
            hint="This is likely a bug in the Steps interpreter."
        )
    
    def _eval_binary_op(self, expr: BinaryOpNode) -> StepsValue:
        """Evaluate a binary operation."""
        left = self.evaluate_expression(expr.left)
        right = self.evaluate_expression(expr.right)
        
        op = expr.operator
        loc = expr.location
        
        # Arithmetic
        if op == "+":
            return builtins.add_numbers(left, right, loc)
        if op == "-":
            return builtins.subtract_numbers(left, right, loc)
        if op == "*":
            return builtins.multiply_numbers(left, right, loc)
        if op == "/":
            return builtins.divide_numbers(left, right, loc)
        
        # Comparison
        if op in ("is equal to", "equals"):
            return builtins.equals(left, right)
        if op == "is not equal to":
            return builtins.not_equals(left, right)
        if op == "is less than":
            return builtins.less_than(left, right, loc)
        if op == "is greater than":
            return builtins.greater_than(left, right, loc)
        if op == "is less than or equal to":
            return builtins.less_than_or_equal(left, right, loc)
        if op == "is greater than or equal to":
            return builtins.greater_than_or_equal(left, right, loc)
        
        # Boolean
        if op == "and":
            return builtins.boolean_and(left, right)
        if op == "or":
            return builtins.boolean_or(left, right)
        
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Unknown binary operator: {op}",
            file=loc.file,
            line=loc.line,
            column=loc.column,
            hint="This is likely a bug in the Steps interpreter."
        )
    
    def _eval_unary_op(self, expr: UnaryOpNode) -> StepsValue:
        """Evaluate a unary operation."""
        operand = self.evaluate_expression(expr.operand)
        
        if expr.operator == "-":
            return builtins.negate_number(operand, expr.location)
        if expr.operator == "not":
            return builtins.boolean_not(operand)
        
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Unknown unary operator: {expr.operator}",
            file=expr.location.file,
            line=expr.location.line,
            column=expr.location.column,
            hint="This is likely a bug in the Steps interpreter."
        )
    
    def _eval_type_conversion(self, expr: TypeConversionNode) -> StepsValue:
        """Evaluate a type conversion."""
        value = self.evaluate_expression(expr.expression)
        
        if expr.target_type == "number":
            return builtins.convert_to_number(value, expr.location)
        if expr.target_type == "text":
            return builtins.convert_to_text(value)
        if expr.target_type == "boolean":
            return builtins.convert_to_boolean(value)
        
        raise StepsRuntimeError(
            code=ErrorCode.E407,
            message=f"Unknown target type: {expr.target_type}",
            file=expr.location.file,
            line=expr.location.line,
            column=expr.location.column,
            hint="Valid types are: number, text, boolean."
        )
    
    def _eval_table_access(self, expr: TableAccessNode) -> StepsValue:
        """Evaluate table/list access."""
        table = self.evaluate_expression(expr.table)
        key = self.evaluate_expression(expr.key)
        return builtins.table_get(table, key, expr.location)


# =============================================================================
# Convenience Functions
# =============================================================================

def run_building(building: BuildingNode, environment: Optional[Environment] = None) -> ExecutionResult:
    """Execute a building program.
    
    Args:
        building: The building AST
        environment: Optional pre-configured environment
    
    Returns:
        ExecutionResult with success status and output
    """
    interpreter = Interpreter(environment)
    return interpreter.run_building(building)


def run_source(source: str) -> ExecutionResult:
    """Parse and run Steps source code.

    Args:
        source: Building source code

    Returns:
        ExecutionResult with success status and output
    """
    from typing import cast
    from .parser import parse_building

    result = parse_building(source)
    if not result.success:
        return ExecutionResult(
            success=False,
            error=result.errors[0] if result.errors else None
        )

    # Cast is safe because parse_building returns BuildingNode when successful
    building = cast(BuildingNode, result.ast)
    return run_building(building)
