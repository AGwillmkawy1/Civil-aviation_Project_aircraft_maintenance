@echo off
REM =============================================================================
REM Aircraft Predictive Maintenance - Quick Start for Windows
REM =============================================================================
REM This script sets up and runs the entire application in one go

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║     Aircraft Predictive Maintenance System - Setup & Launch            ║
echo ║                    Running on Windows                                   ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python not found. Please install Python 3.13+
    echo ℹ️  Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Check if virtual environment exists
if exist ".venv" (
    echo ✅ Virtual environment detected
) else (
    echo ⏳ Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
)

REM Activate virtual environment
echo ⏳ Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment activated

REM Install/upgrade pip
echo ⏳ Updating pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo ⚠️  Warning: Could not upgrade pip, continuing anyway...
)

REM Install dependencies
echo ⏳ Installing dependencies (this may take 2-3 minutes)...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)
echo ✅ Dependencies installed

REM Check Node.js for frontend
node --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  WARNING: Node.js not found (needed for frontend)
    echo ℹ️  Download from: https://nodejs.org/
    echo ℹ️  Continuing with backend-only for now...
    set FRONTEND_AVAILABLE=0
) else (
    echo ✅ Node.js found
    node --version
    set FRONTEND_AVAILABLE=1
)

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                      Setup Complete! 🎉                               ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.

REM Start backend
echo ⏳ Starting Backend API (FastAPI)...
echo ℹ️  API will be available at: http://localhost:8000
echo ℹ️  API Docs at: http://localhost:8000/docs
echo.
echo Press CTRL+C to stop...
echo.

start cmd /k "cd src && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"

REM Wait a moment for backend to start
timeout /t 3 /nobreak

REM Start frontend if available
if %FRONTEND_AVAILABLE% equ 1 (
    echo ⏳ Starting Frontend (React Vite)...
    echo ℹ️  Frontend will be available at: http://localhost:5173
    echo.
    
    start cmd /k "cd frontend && npm install && npm run dev"
    
    timeout /t 3 /nobreak
    
    echo.
    echo ✅ Everything running!
    echo.
    echo 📋 What to do next:
    echo    1. Backend: http://localhost:8000/docs
    echo    2. Frontend: http://localhost:5173
    echo    3. Try making a prediction!
    echo.
) else (
    echo.
    echo ✅ Backend running!
    echo.
    echo 📋 What to do next:
    echo    1. Visit: http://localhost:8000/docs
    echo    2. Try making a prediction using the Swagger UI
    echo    3. To run frontend: install Node.js, then cd frontend && npm run dev
    echo.
)

echo.
echo 💡 Tip: Open two terminals if you want to see both logs clearly
echo 💡 To stop: Press CTRL+C in the terminal windows
echo.

pause
