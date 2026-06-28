@echo off
echo ==========================================
echo UniSafe Full-Stack Platform Setup
echo ==========================================

cd backend

echo [1/4] Checking python virtual environment...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo [2/4] Activating environment and installing pip packages...
rem call venv\Scripts\activate.bat
rem python -m pip install --upgrade pip
rem pip install -r requirements.txt

echo [3/4] Initializing and seeding SQLite Database...
python init_db.py

echo [4/4] Starting FastAPI Server...
echo ----------------------------------------------------
echo Server is running! Open: http://127.0.0.1:8000
echo ----------------------------------------------------
python -m uvicorn main:app --host 127.0.0.1 --port 8000
pause
