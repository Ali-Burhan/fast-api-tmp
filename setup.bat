@echo off
REM FastAPI Speech Translation API - Setup Script
REM For Windows

echo ==========================================
echo FastAPI Speech Translation API Setup
echo ==========================================
echo.

REM Check for Python
echo Checking for Python 3.13+...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.13+ from:
    echo   https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Found Python %PYTHON_VERSION%

REM Check if virtual environment exists
if exist "venv\" (
    echo.
    echo Virtual environment already exists.
    set /p RECREATE="Do you want to recreate it? (y/N): "
    if /i "%RECREATE%"=="y" (
        echo Removing existing virtual environment...
        rmdir /s /q venv
    ) else (
        echo Using existing virtual environment.
    )
)

REM Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo [SUCCESS] Virtual environment created
)

echo.

REM Activate virtual environment and install dependencies
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip --quiet

echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo [SUCCESS] All dependencies installed successfully!

echo.
echo ==========================================
echo Setup Complete! 🎉
echo ==========================================
echo.
echo Next steps:
echo   1. Activate the virtual environment:
echo      venv\Scripts\activate.bat
echo.
echo   2. Configure your environment variables:
echo      copy .env.example .env
echo      Then edit .env with your API keys
echo.
echo   3. Start the application:
echo      uvicorn app.main:app --reload
echo.
echo   4. Visit the API documentation:
echo      http://localhost:8000/docs
echo.
echo For detailed instructions, see INSTALLATION.md
echo.
pause
