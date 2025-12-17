"""Flow Diagram Generator for Steps Programs.

Generates ASCII art flow diagrams showing the structure of Steps programs
with their buildings, floors, and steps.
"""

from typing import Optional, List, Dict
from .ast_nodes import BuildingNode, FloorNode, StepNode
from .environment import Environment


def generate_flow_diagram(building: BuildingNode, environment: Environment) -> str:
    """Generate an ASCII flow diagram for a Steps program.
    
    Args:
        building: The building AST node
        environment: The environment with floor/step registries
    
    Returns:
        ASCII string representation of the program flow
    """
    lines: List[str] = []
    
    # Building header
    lines.append("┌" + "─" * 50 + "┐")
    lines.append(f"│ 🏢 BUILDING: {building.name:<36} │")
    lines.append("├" + "─" * 50 + "┤")
    
    # Get floors from the environment
    floor_names = list(environment.floors.keys())

    if not floor_names:
        lines.append("│    (no floors)                                    │")
    else:
        for i, floor_name in enumerate(floor_names):
            # Get steps for this floor - filter by floor name
            floor_steps = {name: step for name, step in environment.steps.items()
                          if hasattr(step, 'floor') and step.floor == floor_name}
            step_names = list(floor_steps.keys())
            
            # Floor box
            lines.append("│                                                    │")
            lines.append(f"│  ┌{'─' * 44}┐  │")
            lines.append(f"│  │ 📂 FLOOR: {floor_name:<32} │  │")
            lines.append(f"│  ├{'─' * 44}┤  │")
            
            if not step_names:
                lines.append(f"│  │     (no steps)                             │  │")
            else:
                for j, step_name in enumerate(step_names):
                    step_def = floor_steps[step_name]
                    # Get step details
                    params = _format_params(step_def)
                    returns = _format_returns(step_def)
                    
                    lines.append(f"│  │                                            │  │")
                    lines.append(f"│  │    ┌{'─' * 36}┐   │  │")
                    lines.append(f"│  │    │ 🔷 {step_name:<32} │   │  │")
                    if params:
                        lines.append(f"│  │    │   needs: {params:<26} │   │  │")
                    if returns:
                        lines.append(f"│  │    │   returns: {returns:<24} │   │  │")
                    lines.append(f"│  │    └{'─' * 36}┘   │  │")
                    
                    # Arrow between steps
                    if j < len(step_names) - 1:
                        lines.append(f"│  │            │                              │  │")
                        lines.append(f"│  │            ▼                              │  │")
            
            lines.append(f"│  │                                            │  │")
            lines.append(f"│  └{'─' * 44}┘  │")
            
            # Arrow between floors
            if i < len(floor_names) - 1:
                lines.append("│                    │                              │")
                lines.append("│                    ▼                              │")
    
    lines.append("│                                                    │")
    lines.append("└" + "─" * 50 + "┘")
    
    return "\n".join(lines)


def _format_params(step_def: object) -> str:
    """Format step parameters for display."""
    if hasattr(step_def, 'parameters') and step_def.parameters:
        params = step_def.parameters
        if len(params) <= 2:
            return ", ".join(p.name for p in params)
        else:
            return f"{params[0].name}, ... ({len(params)} total)"
    return ""


def _format_returns(step_def: object) -> str:
    """Format step return type for display."""
    if hasattr(step_def, 'returns') and step_def.returns:
        return str(step_def.returns.type_name)
    return ""


def generate_simple_diagram(building: BuildingNode, environment: Environment) -> str:
    """Generate a simple tree-style diagram.
    
    Args:
        building: The building AST node
        environment: The environment with floor/step registries
    
    Returns:
        Simple ASCII tree representation
    """
    lines: List[str] = []
    
    lines.append(f"🏢 {building.name}")

    floor_names = list(environment.floors.keys())

    for i, floor_name in enumerate(floor_names):
        is_last_floor = (i == len(floor_names) - 1)
        floor_prefix = "└── " if is_last_floor else "├── "
        child_prefix = "    " if is_last_floor else "│   "

        lines.append(f"{floor_prefix}📂 {floor_name}")

        # Get steps for this floor
        floor_steps = {name: step for name, step in environment.steps.items()
                      if hasattr(step, 'floor') and step.floor == floor_name}
        step_names = list(floor_steps.keys())
        
        for j, step_name in enumerate(step_names):
            is_last_step = (j == len(step_names) - 1)
            step_prefix = "└── " if is_last_step else "├── "
            lines.append(f"{child_prefix}{step_prefix}🔷 {step_name}")
    
    return "\n".join(lines)

