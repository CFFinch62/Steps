#!/usr/bin/env python3
"""
Quick test script for the diagram feature
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from steps_ide.app.editor import validate_diagram_font

# Need QApplication for font operations
app = QApplication(sys.argv)

# Test font validation
print("Testing font validation...")
print()

# Test with JetBrains Mono (should be good)
font1 = QFont("JetBrains Mono", 10)
is_valid, msg = validate_diagram_font(font1)
print(f"JetBrains Mono: {'✓ Valid' if is_valid else '✗ Invalid'}")
if msg:
    print(f"  Warning: {msg}")
print()

# Test with Courier (should be good)
font2 = QFont("Courier", 10)
is_valid, msg = validate_diagram_font(font2)
print(f"Courier: {'✓ Valid' if is_valid else '✗ Invalid'}")
if msg:
    print(f"  Warning: {msg}")
print()

# Test with Arial (should warn - not monospace)
font3 = QFont("Arial", 10)
is_valid, msg = validate_diagram_font(font3)
print(f"Arial: {'✓ Valid' if is_valid else '✗ Invalid'}")
if msg:
    print(f"  Warning: {msg}")
print()

print("Font validation test complete!")
print()
print("To test the full feature:")
print("1. Run: python -m steps_ide.main")
print("2. Open a Steps project file (or don't)")
print("3. Go to View → Show Project Diagram (or press Ctrl+D)")
print("4. Select a project if no file is open")
print("5. The diagram should appear in a new tab")
print("6. Click 'Save Diagram As...' to save it")

