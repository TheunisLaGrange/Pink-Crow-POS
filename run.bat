@echo off
TITLE Pink Crow Cafe POS - Initializing Node
SETLOCAL Enabledelayedexpansion

echo ===================================================
echo   PINK CROW CAFÉ - PROPRIETARY FRANCHISE POS NODE  
echo ===================================================
echo Checking terminal environment dependencies...

:: 1. Verify if Python is accessible on the host path execution framework
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to system PATH.
    echo Please install Python 3.10+ from the Microsoft Store or python.org before proceeding.
    pause
    exit /b
)

:: 2. Check if a local runtime environment workspace wrapper exists
if not exist ".venv" (
    echo Building clean localized production virtual environment (.venv)...
    python -m venv .venv
    if !errorlevel! neq 0 ( echo [ERROR] Failed to compile venv. & pause & exit /b )
    
    echo Activating environment node and downloading frame manifests...
    call .venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo Localized environment sandbox detected. Activating node...
    call .venv\Scripts\activate
)

:: 3. Launch local franchise interface asynchronously inside browser window frames
echo Starting local service web frames daemon network...
start "" "http://127.0.0.1:5000"

:: 4. Execute your decoupled server routing script loop natively
python server.py
if %errorlevel% neq 0 (
    echo [CRITICAL ERROR] POS application engine terminated unexpectedly.
    pause
)
