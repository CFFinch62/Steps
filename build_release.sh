#!/bin/bash
set -e

# Define project root
PROJECT_ROOT=$(pwd)
DIST_DIR="$PROJECT_ROOT/dist"
BUILD_DIR="$PROJECT_ROOT/build"

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
            --add-data "docs/QUICK-REFERENCE.md:docs" \
            --hidden-import "PyQt6.QtWebEngineCore" \
            --hidden-import "PyQt6.QtWebEngineWidgets" \
            src/steps_ide/main.py

echo "✅ Build complete!"
echo "🚀 executable is located at: dist/StepsIDE/StepsIDE"
echo "   (or dist/StepsIDE if using --onefile, but we used directory mode for faster startup)"

# Optional: Create a simple run script in dist for convenience
echo "#!/bin/bash" > "$DIST_DIR/StepsIDE/run.sh"
echo 'cd "$(dirname "$0")"' >> "$DIST_DIR/StepsIDE/run.sh"
echo './StepsIDE' >> "$DIST_DIR/StepsIDE/run.sh"
chmod +x "$DIST_DIR/StepsIDE/run.sh"

echo "✨ Ready to test!"
