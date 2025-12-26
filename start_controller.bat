@echo off
setlocal

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo ========================================
echo Starting Hand Gesture PC Controller
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

REM Activate virtual environment and run the controller
call "%SCRIPT_DIR%venv\Scripts\activate.bat"
py "%SCRIPT_DIR%hand_controller.py"

REM Deactivate when done
call "%SCRIPT_DIR%venv\Scripts\deactivate.bat"
endlocal
