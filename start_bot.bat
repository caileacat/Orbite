@echo off
setlocal

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Ensure watchdog and requests are installed
pip show watchdog >nul 2>&1
if errorlevel 1 (
    echo Installing watchdog...
    pip install watchdog
)

pip show requests >nul 2>&1
if errorlevel 1 (
    echo Installing requests...
    pip install requests
)

:: Run the watchdog script
python watchdog_script.py

endlocal

