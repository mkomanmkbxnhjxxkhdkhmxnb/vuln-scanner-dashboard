@echo off
echo ========================================
echo Vulnerability Scanner Dashboard
echo ========================================
echo.
echo Starting application...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run application
echo.
echo Starting Flask server...
echo Dashboard will open at: http://localhost:5000
echo.
python app.py

pause
