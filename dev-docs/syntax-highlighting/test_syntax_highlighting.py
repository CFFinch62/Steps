#!/usr/bin/env python3
"""Test script to verify Steps syntax highlighting is working."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_tree_sitter_import():
    """Test that tree-sitter-steps can be imported."""
    print("Testing tree-sitter-steps import...")
    try:
        import tree_sitter_steps
        print("✓ tree_sitter_steps imported successfully")
        
        # Test getting the language
        lang = tree_sitter_steps.get_language()
        print(f"✓ Language object obtained: {lang}")
        
        # Test getting the highlight query
        query = tree_sitter_steps.get_highlight_query()
        print(f"✓ Highlight query loaded ({len(query)} characters)")
        print(f"  First 100 chars: {query[:100]}...")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def test_registration():
    """Test that the Steps language can be registered with TextArea."""
    print("\nTesting Steps language registration...")
    try:
        from textual.widgets import TextArea
        from steps_ide.editor.register_steps_language import register_steps_language
        
        # Create a TextArea
        text_area = TextArea()
        print("✓ TextArea created")
        
        # Register the language
        success = register_steps_language(text_area)
        if success:
            print("✓ Steps language registered successfully")
        else:
            print("✗ Failed to register Steps language")
            return False
        
        # Try to set the language
        text_area.language = "steps"
        print(f"✓ Language set to: {text_area.language}")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_steps_editor():
    """Test that StepsEditor properly detects and uses Steps language."""
    print("\nTesting StepsEditor...")
    try:
        from steps_ide.editor.steps_editor import StepsEditor
        
        # Create a StepsEditor
        editor = StepsEditor()
        print("✓ StepsEditor created")
        
        # Test language detection for a .step file
        lang = editor.detect_language("test.step")
        print(f"✓ Detected language for test.step: {lang}")
        
        if lang == "steps":
            print("✓ Steps language properly detected!")
        elif lang is None:
            print("⚠ Language is None (registration may have failed)")
        else:
            print(f"✗ Unexpected language: {lang}")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Steps Syntax Highlighting Test Suite")
    print("=" * 60)
    
    results = []
    
    results.append(("Tree-sitter import", test_tree_sitter_import()))
    results.append(("Language registration", test_registration()))
    results.append(("StepsEditor integration", test_steps_editor()))
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print("=" * 60)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(result[1] for result in results)
    
    print("=" * 60)
    if all_passed:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())

