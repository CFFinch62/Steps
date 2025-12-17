#!/bin/bash
# Run script for Steps IDE
# Checks for venv, runs setup if needed, then launches the IDE

set -e  # Exit on error

VENV_DIR="venv"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "🔧 Running setup.sh to create it..."
    echo ""
    bash "$SCRIPT_DIR/setup.sh"
    echo ""
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Check if Steps is installed
if ! python -c "import steps" 2>/dev/null; then
    echo "⚠️  Steps package not found in virtual environment!"
    echo "🔧 Running setup.sh to install it..."
    echo ""
    bash "$SCRIPT_DIR/setup.sh"
    echo ""
fi

# Launch the Steps IDE
echo "🚀 Launching Steps IDE..."
echo ""
python -m steps_ide.main

