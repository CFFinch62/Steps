#!/bin/bash
set -e

# ============================================================
#  Steps IDE - macOS Intel (x86_64) Build Script
# ============================================================

PROJECT_ROOT=$(pwd)
DIST_DIR="$PROJECT_ROOT/dist/mac-intel"
BUILD_DIR="$PROJECT_ROOT/build/mac-intel"
VENV_DIR="$PROJECT_ROOT/venv-mac"

echo "============================================"
echo "  Steps IDE  ·  macOS Intel Build Script"
echo "============================================"
echo ""

# ── Virtual environment ──────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating venv-mac virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✓ venv-mac created"
else
    echo "✓ venv-mac already exists"
fi

echo "🔌 Activating venv-mac..."
source "$VENV_DIR/bin/activate"

echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

echo "📥 Installing project dependencies..."
pip install -e . --quiet
pip install PyQt6 PyQt6-WebEngine --quiet

# ── Clean previous Mac build ─────────────────────────────────
echo ""
echo "🧹 Cleaning previous mac-intel builds..."
rm -rf "$DIST_DIR" "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

# ── Generate .icns icon (macOS requires .icns, not .png) ─────
echo ""
echo "🎨 Generating macOS icon (Steps.icns)..."
ICONSET_DIR="$BUILD_DIR/Steps.iconset"
ICNS_FILE="$PROJECT_ROOT/images/Steps.icns"
mkdir -p "$ICONSET_DIR"
sips -z 16   16   "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_16x16.png"    > /dev/null
sips -z 32   32   "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_16x16@2x.png" > /dev/null
sips -z 32   32   "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_32x32.png"    > /dev/null
sips -z 64   64   "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_32x32@2x.png" > /dev/null
sips -z 128  128  "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_128x128.png"  > /dev/null
sips -z 256  256  "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_128x128@2x.png" > /dev/null
sips -z 256  256  "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_256x256.png"  > /dev/null
sips -z 512  512  "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_256x256@2x.png" > /dev/null
sips -z 512  512  "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_512x512.png"  > /dev/null
sips -z 1024 1024 "$PROJECT_ROOT/images/Steps.png" --out "$ICONSET_DIR/icon_512x512@2x.png" > /dev/null
iconutil -c icns "$ICONSET_DIR" --output "$ICNS_FILE"
echo "✓ Steps.icns created at images/Steps.icns"

# ── PyInstaller ──────────────────────────────────────────────
echo ""
echo "📦 Installing PyInstaller..."
pip install pyinstaller --quiet

# ── Build Steps IDE (.app bundle) ───────────────────────────
echo ""
echo "🔨 Building Steps IDE..."
pyinstaller --name="StepsIDE" \
            --windowed \
            --noconsole \
            --clean \
            --noconfirm \
            --icon="$ICNS_FILE" \
            --distpath "$DIST_DIR" \
            --workpath "$BUILD_DIR" \
            --add-data "src/steps/stdlib:steps/stdlib" \
            --add-data "docs/QUICK-REFERENCE.md:docs" \
            --add-data "images:images" \
            --hidden-import "PyQt6.QtWebEngineCore" \
            --hidden-import "PyQt6.QtWebEngineWidgets" \
            --osx-bundle-identifier "com.steps.stepsIDE" \
            --target-arch x86_64 \
            src/steps_ide/main.py

# ── Build Steps Interpreter (CLI binary) ────────────────────
echo ""
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
            --target-arch x86_64 \
            src/steps/main.py

# ── Convenience launcher ─────────────────────────────────────
echo "#!/bin/bash" > "$DIST_DIR/run.sh"
echo 'open "$(dirname "$0")/StepsIDE.app"' >> "$DIST_DIR/run.sh"
chmod +x "$DIST_DIR/run.sh"

# ── Done ─────────────────────────────────────────────────────
echo ""
echo "============================================"
echo "  ✅ Build complete!"
echo "============================================"
echo ""
echo "  🖥️  IDE app bundle : dist/mac-intel/StepsIDE.app"
echo "  ⚙️  CLI interpreter: dist/mac-intel/steps"
echo "  🚀 Quick launch   : dist/mac-intel/run.sh"
echo ""
echo "  To run the IDE directly:"
echo "    open dist/mac-intel/StepsIDE.app"
echo ""
echo "  To install the CLI system-wide:"
echo "    sudo cp dist/mac-intel/steps /usr/local/bin/steps"
echo ""

