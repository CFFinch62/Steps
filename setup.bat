@echo off
REM Setup script for Steps programming language
REM Creates virtual environment and installs dependencies

setlocal enabledelayedexpansion

set VENV_DIR=venv-win
set SCRIPT_DIR=%~dp0

echo.
echo Steps Setup Script
echo ====================
echo.

REM Check if venv exists
if exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Virtual environment already exists at %VENV_DIR%
) else (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create virtual environment
        exit /b 1
    )
    echo ✓ Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip
    exit /b 1
)

REM Install the Steps package in editable mode
echo Installing Steps package...
pip install -e .
if errorlevel 1 (
    echo Failed to install Steps package
    exit /b 1
)

REM Install IDE dependencies
echo Installing IDE dependencies (textual, watchfiles)...
pip install textual watchfiles
if errorlevel 1 (
    echo Failed to install IDE dependencies
    exit /b 1
)

REM Install tree-sitter-steps for syntax highlighting
echo Installing tree-sitter-steps for syntax highlighting...
pip install -e tree-sitter-steps/
if errorlevel 1 (
    echo Failed to install tree-sitter-steps
    exit /b 1
)

REM Install development dependencies (optional)
set /p INSTALL_DEV="Install development dependencies (pytest, mypy, black, isort)? [y/N] "
if /i "%INSTALL_DEV%"=="y" (
    echo Installing development dependencies...
    pip install pytest pytest-cov mypy black isort
    if errorlevel 1 (
        echo Failed to install development dependencies
        exit /b 1
    )
    echo ✓ Development dependencies installed
)

echo.
echo Setup complete!
echo.
echo To activate the virtual environment manually, run:
echo   %VENV_DIR%\Scripts\activate.bat
echo.
echo To run the Steps IDE, use:
echo   run.bat
echo.

endlocal

