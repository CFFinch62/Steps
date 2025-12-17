"""Steps IDE Application - Main entry point for the Steps IDE."""

import os
from pathlib import Path
from textual.app import App, ComposeResult, SystemCommand
from steps_ide.app.screens.main_screen import MainScreen
from steps_ide.editor.steps_editor import StepsEditor
from steps_ide.editor.editor_widget import SYNTAX_THEMES
from steps_ide.app.widgets.file_browser import FileBrowser


class StepsIDEApp(App):
    """Steps IDE - Educational programming environment for the Steps language."""

    TITLE = "Steps IDE"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def on_mount(self) -> None:
        self.push_screen(MainScreen())
        # Delay initial sync until screen is fully mounted
        self.set_timer(0.2, self._sync_syntax_theme)

    def watch_theme(self, old_theme: str, new_theme: str) -> None:
        """Called when the UI theme changes."""
        self._sync_syntax_theme()

    def _sync_syntax_theme(self) -> None:
        """Sync syntax highlighting theme with UI theme."""
        try:
            screen = self.screen
            editor = screen.query_one(StepsEditor)
            editor.set_syntax_theme_for_ui(self.theme)
            editor.refresh()
        except Exception:
            pass  # Editor not mounted yet

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_select_syntax_theme(self, theme: str) -> None:
        """Set syntax theme manually (user override)."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.set_user_syntax_theme(theme)
            editor.refresh()
            self.notify(f"Syntax theme: {theme}")
        except Exception:
            pass

    def action_reset_syntax_theme(self) -> None:
        """Reset syntax theme to auto-match UI theme."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.clear_user_syntax_theme()
            editor.set_syntax_theme_for_ui(self.theme)
            editor.refresh()
            self.notify("Syntax theme: auto-matching UI")
        except Exception:
            pass

    def action_set_indent_width(self, width: int) -> None:
        """Set the indent width (number of spaces per indent level)."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.indent_width = width
            self.notify(f"Indent width: {width}")
        except Exception:
            pass

    def action_set_indent_type(self, indent_type: str) -> None:
        """Set indent type to spaces or tabs."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.indent_type = indent_type
            self.notify(f"Indent type: {indent_type}")
        except Exception:
            pass

    def action_toggle_soft_wrap(self) -> None:
        """Toggle soft wrap on/off."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.soft_wrap = not editor.soft_wrap
            status = "on" if editor.soft_wrap else "off"
            self.notify(f"Soft wrap: {status}")
        except Exception:
            pass

    def action_toggle_auto_indent(self) -> None:
        """Toggle auto-indent on/off."""
        try:
            editor = self.screen.query_one(StepsEditor)
            editor.auto_indent = not editor.auto_indent
            status = "on" if editor.auto_indent else "off"
            self.notify(f"Auto-indent: {status}")
        except Exception:
            pass

    def action_browse_home(self) -> None:
        """Set file browser root to home directory."""
        try:
            browser = self.screen.query_one(FileBrowser)
            home = str(Path.home())
            browser.set_root(home)
            self.notify(f"Browse: ~")
        except Exception:
            pass

    def action_browse_root(self) -> None:
        """Set file browser root to filesystem root."""
        try:
            browser = self.screen.query_one(FileBrowser)
            browser.set_root("/")
            self.notify("Browse: /")
        except Exception:
            pass

    def action_browse_cwd(self) -> None:
        """Set file browser root to current working directory."""
        try:
            browser = self.screen.query_one(FileBrowser)
            cwd = os.getcwd()
            browser.set_root(cwd)
            # Shorten path for display
            home = str(Path.home())
            display = cwd.replace(home, "~") if cwd.startswith(home) else cwd
            self.notify(f"Browse: {display}")
        except Exception:
            pass

    def get_system_commands(self, screen):
        """Add syntax theme commands to command palette."""
        # First yield all default system commands
        yield from super().get_system_commands(screen)

        # Add syntax theme selection commands
        for theme in SYNTAX_THEMES:
            yield SystemCommand(
                f"Syntax Theme: {theme}",
                f"Set syntax highlighting to {theme}",
                lambda t=theme: self.action_select_syntax_theme(t),
            )

        # Add auto-match option
        yield SystemCommand(
            "Syntax Theme: Auto (match UI)",
            "Reset syntax theme to auto-match UI theme",
            self.action_reset_syntax_theme,
        )

        # Editor settings: Indent width
        for width in [2, 4, 8]:
            yield SystemCommand(
                f"Indent Width: {width}",
                f"Set indent width to {width} spaces",
                lambda w=width: self.action_set_indent_width(w),
            )

        # Editor settings: Indent type (spaces vs tabs)
        yield SystemCommand(
            "Indent Type: Spaces",
            "Use spaces for indentation",
            lambda: self.action_set_indent_type("spaces"),
        )
        yield SystemCommand(
            "Indent Type: Tabs",
            "Use tabs for indentation",
            lambda: self.action_set_indent_type("tabs"),
        )

        # Editor settings: Soft wrap toggle
        yield SystemCommand(
            "Toggle Soft Wrap",
            "Toggle line wrapping on/off",
            self.action_toggle_soft_wrap,
        )

        # Editor settings: Auto-indent toggle
        yield SystemCommand(
            "Toggle Auto-Indent",
            "Toggle auto-indent on Enter (for code vs prose)",
            self.action_toggle_auto_indent,
        )

        # File browser root switching
        yield SystemCommand(
            "Browse: Home Directory",
            "Set file browser to home directory (~)",
            self.action_browse_home,
        )
        yield SystemCommand(
            "Browse: Filesystem Root",
            "Set file browser to filesystem root (/)",
            self.action_browse_root,
        )
        yield SystemCommand(
            "Browse: Launch Directory",
            "Set file browser to directory where app was launched",
            self.action_browse_cwd,
        )

        # Steps project operations
        yield SystemCommand(
            "Steps: New Project",
            "Create a new Steps project",
            self._action_new_project,
        )
        yield SystemCommand(
            "Steps: New Floor",
            "Create a new floor in the current project",
            self._action_new_floor,
        )
        yield SystemCommand(
            "Steps: New Step",
            "Create a new step in the current floor",
            self._action_new_step,
        )
        yield SystemCommand(
            "Steps: Run Project (F5)",
            "Run the current Steps project",
            self._action_run_steps,
        )
        yield SystemCommand(
            "Steps: Check Syntax (F6)",
            "Check syntax of the current Steps project",
            self._action_check_steps,
        )

    def _action_new_project(self) -> None:
        """Trigger new project action on main screen."""
        try:
            self.screen.action_new_project()
        except Exception:
            pass

    def _action_new_floor(self) -> None:
        """Trigger new floor action on main screen."""
        try:
            self.screen.action_new_floor()
        except Exception:
            pass

    def _action_new_step(self) -> None:
        """Trigger new step action on main screen."""
        try:
            self.screen.action_new_step()
        except Exception:
            pass

    def _action_run_steps(self) -> None:
        """Trigger run steps action on main screen."""
        try:
            self.screen.action_run_steps()
        except Exception:
            pass

    def _action_check_steps(self) -> None:
        """Trigger check steps action on main screen."""
        try:
            self.screen.action_check_steps()
        except Exception:
            pass
