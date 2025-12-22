"""Unit tests for the Steps Debugger."""

import pytest
from pathlib import Path
from unittest.mock import Mock, call

from steps.debugger import DebugInterpreter, DebugMode, DebugEvent
from steps.environment import Environment
from steps.ast_nodes import (
    BuildingNode, StepNode, DisplayStatement, SourceLocation,
    SetStatement, ExpressionNode, NumberLiteral
)
from steps.types import StepsNumber

class TestDebugger:
    
    @pytest.fixture
    def env(self):
        return Environment()
    
    @pytest.fixture
    def mock_callback(self):
        return Mock()
    
    @pytest.fixture
    def debugger(self, env, mock_callback):
        return DebugInterpreter(env, mock_callback)
    
    def create_dummy_stmt(self, line: int):
        loc = SourceLocation(Path("test.steps"), line, 1, 10)
        # DisplayStatement needs an expression
        expr = NumberLiteral(1, loc)
        # ASTNode (base) fields come first in dataclass inheritance usually
        stmt = DisplayStatement(loc, expr)
        return stmt

    def test_initial_state(self, debugger):
        assert debugger.get_mode() == DebugMode.PAUSED
        assert len(debugger.get_breakpoints()) == 0

    def test_breakpoint_management(self, debugger):
        path = Path("test.steps")
        debugger.add_breakpoint(path, 10)
        assert debugger.has_breakpoint(path, 10)
        
        debugger.remove_breakpoint(path, 10)
        assert not debugger.has_breakpoint(path, 10)

    def test_should_pause_breakpoint(self, debugger):
        path = Path("test.steps")
        debugger.add_breakpoint(path, 5)
        debugger.set_mode(DebugMode.RUN_TO_BREAKPOINT)
        
        stmt = self.create_dummy_stmt(5)
        assert debugger._should_pause(stmt) is True
        
        stmt_no_break = self.create_dummy_stmt(6)
        assert debugger._should_pause(stmt_no_break) is False
        
    def test_should_pause_step_into(self, debugger):
        debugger.set_mode(DebugMode.STEP_INTO)
        stmt = self.create_dummy_stmt(5)
        assert debugger._should_pause(stmt) is True

    def test_step_over_logic(self, debugger):
        # Initial depth is 0
        debugger.set_mode(DebugMode.STEP_OVER)
        # Should pause at same depth
        stmt = self.create_dummy_stmt(5)
        assert debugger._should_pause(stmt) is True
        
        # Simulate entering a call
        debugger._call_depth += 1
        # Should NOT pause (deeper)
        assert debugger._should_pause(stmt) is False
        
        # Return to original depth
        debugger._call_depth -= 1
        assert debugger._should_pause(stmt) is True

    def test_step_out_logic(self, debugger):
        debugger._call_depth = 5
        debugger.set_mode(DebugMode.STEP_OUT)
        # Target depth is 4 (one less than current)
        
        stmt = self.create_dummy_stmt(5)
        
        # Still at depth 5 -> Don't pause
        assert debugger._should_pause(stmt) is False
        
        # Return to depth 4
        debugger._call_depth = 4
        assert debugger._should_pause(stmt) is True
