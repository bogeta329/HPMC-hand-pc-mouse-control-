@echo off
setlocal

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo ========================================
echo Hand Gesture Demo - Practice Mode
echo ========================================
echo.
echo This mode shows gesture detection
echo WITHOUT controlling your mouse.
echo.
echo Perfect for learning and practicing!
echo.
echo ========================================
echo.
echo Working directory: %CD%
echo.

REM Check if virtual environment exists
if not exist "%SCRIPT_DIR%venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Expected location: %SCRIPT_DIR%venv\Scripts\activate.bat
    echo Please run setup.bat first to install dependencies.
    echo.
    pause
    exit /b 1
)

echo Virtual environment found!
echo.

REM Activate virtual environment and run demo
call "%SCRIPT_DIR%venv\Scripts\activate.bat"
py "%SCRIPT_DIR%demo_practice.py"

REM Deactivate when done
call "%SCRIPT_DIR%venv\Scripts\deactivate.bat"
endlocal
