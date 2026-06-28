#!/bin/bash

echo "=========================================="
echo "UniSafe Full-Stack Platform Setup"
echo "=========================================="

cd backend || exit

echo "[1/4] Checking python virtual environment..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "[2/4] Activating environment and installing pip packages..."
source venv/bin/activate
# python3 -m pip install --upgrade pip
# pip install -r requirements.txt

echo "[3/4] Initializing and seeding SQLite Database..."
python3 init_db.py

echo "[4/4] Starting FastAPI Server..."
echo "----------------------------------------------------"
echo "Server is running! Open: http://127.0.0.1:8000"
echo "----------------------------------------------------"
python3 -m uvicorn main:app --host 127.0.0.1 --port 8000