#!/usr/bin/env python3
"""
Steps IDE - A modern IDE for the Steps programming language
Based on the EZ IDE codebase
"""

import sys
import os

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

from steps_ide.app.main_window import StepsIDEMainWindow
from steps_ide.app.settings import SettingsManager


def main():
    """Main entry point for the Steps IDE"""
    
    # Check if running in CLI mode (used for frozen execute to run internal steps interpreter)
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        # Remove '--cli' so arguments align with what steps.main expects
        del sys.argv[1]
        try:
            from steps.main import main as steps_main
            sys.exit(steps_main())
        except ImportError as e:
            print(f"Error: Could not import steps interpreter: {e}")
            sys.exit(1)
            
    # Enable high DPI scaling
    app = QApplication(sys.argv)
    app.setApplicationName("Steps IDE")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Steps Language")
    
    # Set Application Icon
    from pathlib import Path
    
    # Calculate path to the images folder
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller bundled execution path
        root_dir = Path(sys._MEIPASS)
    else:
        # Development execution path relative to this file
        # main.py -> steps_ide -> src -> Steps
        root_dir = Path(__file__).resolve().parent.parent.parent
        
    icon_path = root_dir / "images" / "steps_simple_256.png"
    
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
        
        # Ensure icon shows up in Windows taskbar
        if sys.platform == 'win32':
            import ctypes
            myappid = 'stepslanguage.stepside.ide.1.0.0'
            try:
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            except Exception:
                pass
    
    # Load settings
    settings = SettingsManager()
    
    # Apply theme
    from steps_ide.app.themes import ThemeManager
    theme_manager = ThemeManager(settings)
    app.setStyleSheet(theme_manager.get_current_stylesheet())
    
    # Create and show main window
    window = StepsIDEMainWindow(settings, theme_manager)
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
