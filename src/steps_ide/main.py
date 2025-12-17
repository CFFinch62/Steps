"""Steps IDE - Educational programming environment for the Steps language."""

import sys
from steps_ide.app.application import StepsIDEApp


def main():
    """Run the Steps IDE."""
    app = StepsIDEApp()
    app.run()


if __name__ == "__main__":
    main()
