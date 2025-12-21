#!/usr/bin/env python3
"""Entry point for running steps as a module: python -m steps"""

import sys
from steps.main import main

if __name__ == "__main__":
    sys.exit(main())
