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
    # Enable high DPI scaling
    app = QApplication(sys.argv)
    app.setApplicationName("Steps IDE")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Steps Language")
    
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
