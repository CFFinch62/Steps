@echo off
REM Run script for Steps IDE
REM Checks for venv, runs setup if needed, then launches the IDE

setlocal enabledelayedexpansion

set VENV_DIR=venv-win
set SCRIPT_DIR=%~dp0

REM Check if venv exists
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Virtual environment not found!
    echo Running setup.bat to create it...
    echo.
    call "%SCRIPT_DIR%setup.bat"
    if errorlevel 1 (
        echo Setup failed
        exit /b 1
    )
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment
    exit /b 1
)

REM Check if Steps is installed
python -c "import steps" 2>nul
if errorlevel 1 (
    echo Steps package not found in virtual environment!
    echo Running setup.bat to install it...
    echo.
    call "%SCRIPT_DIR%setup.bat"
    if errorlevel 1 (
        echo Setup failed
        exit /b 1
    )
    echo.
)

REM Launch the Steps IDE
echo Launching Steps IDE...
echo.
python -m steps_ide.main

endlocal

