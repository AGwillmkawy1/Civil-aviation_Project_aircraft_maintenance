#!/bin/bash

# =============================================================================
# Aircraft Predictive Maintenance - Quick Start for Mac/Linux
# =============================================================================
# This script sets up and runs the entire application in one go

echo ""
echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║     Aircraft Predictive Maintenance System - Setup & Launch            ║"
echo "║                    Running on Mac/Linux                                 ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 not found. Please install Python 3.13+"
    echo "ℹ️  macOS: brew install python3"
    echo "ℹ️  Linux: sudo apt install python3"
    exit 1
fi

echo "✅ Python found"
python3 --version

# Check if virtual environment exists
if [ -d ".venv" ]; then
    echo "✅ Virtual environment detected"
else
    echo "⏳ Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "⏳ Activating virtual environment..."
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment"
    exit 1
fi
echo "✅ Virtual environment activated"

# Install/upgrade pip
echo "⏳ Updating pip..."
python -m pip install --upgrade pip --quiet

# Install dependencies
echo "⏳ Installing dependencies (this may take 2-3 minutes)..."
pip install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo "✅ Dependencies installed"

# Check Node.js for frontend
if ! command -v node &> /dev/null; then
    echo "⚠️  WARNING: Node.js not found (needed for frontend)"
    echo "ℹ️  macOS: brew install node"
    echo "ℹ️  Linux: sudo apt install nodejs npm"
    echo "ℹ️  Continuing with backend-only for now..."
    FRONTEND_AVAILABLE=0
else
    echo "✅ Node.js found"
    node --version
    FRONTEND_AVAILABLE=1
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║                      Setup Complete! 🎉                               ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

# Start backend
echo "⏳ Starting Backend API (FastAPI)..."
echo "ℹ️  API will be available at: http://localhost:8000"
echo "ℹ️  API Docs at: http://localhost:8000/docs"
echo ""
echo "Press CTRL+C to stop..."
echo ""

# Function to start processes and manage them
start_backend() {
    cd src
    python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
}

start_frontend() {
    cd frontend
    npm install > /dev/null 2>&1
    npm run dev
}

# Export functions for use in subshells
export -f start_backend
export -f start_frontend

# Start backend in background
start_backend &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend if available
if [ $FRONTEND_AVAILABLE -eq 1 ]; then
    echo "⏳ Starting Frontend (React Vite)..."
    echo "ℹ️  Frontend will be available at: http://localhost:5173"
    echo ""
    
    start_frontend &
    FRONTEND_PID=$!
    
    sleep 3
    
    echo ""
    echo "✅ Everything running!"
    echo ""
    echo "📋 What to do next:"
    echo "   1. Backend: http://localhost:8000/docs"
    echo "   2. Frontend: http://localhost:5173"
    echo "   3. Try making a prediction!"
    echo ""
else
    echo ""
    echo "✅ Backend running!"
    echo ""
    echo "📋 What to do next:"
    echo "   1. Visit: http://localhost:8000/docs"
    echo "   2. Try making a prediction using the Swagger UI"
    echo "   3. To run frontend: install Node.js, then cd frontend && npm run dev"
    echo ""
fi

echo "💡 Tip: Open two terminals if you want to see both logs clearly"
echo "💡 To stop: Press CTRL+C"
echo ""

# Handle cleanup on exit
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" SIGINT SIGTERM

# Wait for all background processes
wait
