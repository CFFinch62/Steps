from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import Static


class StatusBar(Widget):
    """A status bar widget showing file info, cursor position, encoding."""

    DEFAULT_CSS = """
    StatusBar {
        height: 1;
        background: $surface;
        color: $text;
        layout: horizontal;
    }

    StatusBar .status-item {
        padding: 0 1;
        width: auto;
    }

    StatusBar #file-path {
        width: 1fr;
    }

    StatusBar #modified {
        color: $warning;
        width: 2;
    }

    StatusBar #cursor-pos {
        width: auto;
        min-width: 14;
    }

    StatusBar #encoding {
        color: $text-muted;
        width: auto;
        min-width: 6;
    }

    StatusBar #line-ending {
        color: $text-muted;
        width: auto;
        min-width: 4;
    }
    """

    # Use init=False to prevent watchers from triggering before compose
    file_path = reactive("Untitled", init=False)
    cursor_position = reactive((1, 1), init=False)
    is_modified = reactive(False, init=False)
    encoding = reactive("UTF-8", init=False)
    line_ending = reactive("LF", init=False)

    def compose(self):
        yield Static(self.file_path, id="file-path", classes="status-item")
        yield Static("", id="modified", classes="status-item")
        yield Static(f"Ln {self.cursor_position[0]}, Col {self.cursor_position[1]}", id="cursor-pos", classes="status-item")
        yield Static(self.encoding, id="encoding", classes="status-item")
        yield Static(self.line_ending, id="line-ending", classes="status-item")

    def watch_file_path(self, path: str) -> None:
        try:
            self.query_one("#file-path", Static).update(path)
        except Exception:
            pass

    def watch_cursor_position(self, pos: tuple[int, int]) -> None:
        try:
            self.query_one("#cursor-pos", Static).update(f"Ln {pos[0]}, Col {pos[1]}")
        except Exception:
            pass

    def watch_is_modified(self, modified: bool) -> None:
        try:
            indicator = "●" if modified else ""
            self.query_one("#modified", Static).update(indicator)
        except Exception:
            pass

    def watch_encoding(self, enc: str) -> None:
        try:
            self.query_one("#encoding", Static).update(enc)
        except Exception:
            pass

    def watch_line_ending(self, ending: str) -> None:
        try:
            self.query_one("#line-ending", Static).update(ending)
        except Exception:
            pass
