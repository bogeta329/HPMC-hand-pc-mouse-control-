@echo off
setlocal

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo ========================================
echo Testing Hand Gesture Controller System
echo ========================================
echo.
echo Working directory: %CD%
echo.

REM Check if virtual environment exists
if not exist "%SCRIPT_DIR%venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Expected location: %SCRIPT_DIR%venv\Scripts\activate.bat
    echo Please run setup.bat first.
    echo.
    pause
    exit /b 1
)

echo Virtual environment found!
echo.

REM Activate virtual environment and run test
call "%SCRIPT_DIR%venv\Scripts\activate.bat"
py "%SCRIPT_DIR%test_system.py"

echo.
pause
endlocal
