#!/bin/bash
set -e

# Define project root
PROJECT_ROOT=$(pwd)
DIST_DIR="$PROJECT_ROOT/dist/linux"
BUILD_DIR="$PROJECT_ROOT/build/linux"
VENV_DIR="$PROJECT_ROOT/venv"

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "🔧 Running setup.sh to create it..."
    bash "$PROJECT_ROOT/setup.sh"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "🧹 Cleaning previous builds..."
rm -rf "$DIST_DIR" "$BUILD_DIR" "*.spec"

echo "📦 Installing build dependencies..."
pip install pyinstaller

echo "🔨 Building Steps IDE..."
# Create the executable
# --noconsole: Don't show a terminal window
# --name: Name of the executable
# --add-data: Include the Quick Reference file
# --hidden-import: Ensure all needed modules are found (PyQt6-WebEngine might need this)
# --clean: Clean PyInstaller cache
# --noconfirm: Don't ask to overwrite
pyinstaller --name="StepsIDE" \
            --windowed \
            --noconsole \
            --clean \
            --noconfirm \
            --icon="images/Steps.png" \
            --distpath "$DIST_DIR" \
            --workpath "$BUILD_DIR" \
            --add-data "src/steps/stdlib:steps/stdlib" \
            --add-data "docs/QUICK-REFERENCE.md:docs" \
            --add-data "images:images" \
            --hidden-import "PyQt6.QtWebEngineCore" \
            --hidden-import "PyQt6.QtWebEngineWidgets" \
            src/steps_ide/main.py

echo "🔨 Building Steps Interpreter..."
pyinstaller --name="steps" \
            --onefile \
            --console \
            --clean \
            --noconfirm \
            --distpath "$DIST_DIR" \
            --workpath "$BUILD_DIR" \
            --paths "src" \
            --add-data "src/steps/stdlib:steps/stdlib" \
            --hidden-import "steps_repl" \
            --hidden-import "steps_repl.repl" \
            --hidden-import "steps_repl.commands" \
            --hidden-import "steps_repl.environment" \
            src/steps/main.py

echo "✅ Build complete!"
echo "🚀 executable is located at: dist/linux/StepsIDE/StepsIDE"
echo "   (or dist/linux/StepsIDE if using --onefile, but we used directory mode for faster startup)"

# Optional: Create a simple run script in dist for convenience
echo "#!/bin/bash" > "$DIST_DIR/StepsIDE/run.sh"
echo 'cd "$(dirname "$0")"' >> "$DIST_DIR/StepsIDE/run.sh"
echo './StepsIDE' >> "$DIST_DIR/StepsIDE/run.sh"
chmod +x "$DIST_DIR/StepsIDE/run.sh"

echo "✨ Ready to test!"
