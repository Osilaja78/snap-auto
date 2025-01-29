@echo off
cd /d "%~dp0"

echo Starting Appium server...
start /b appium  > nul 2>&1

:: Wait a few seconds to ensure Appium starts properly
timeout /t 10 >nul

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Running bot menu...
python main.py

echo Stopping Appium server...
taskkill /F /IM node.exe >nul 2>&1

echo Bot has exited. Press any key to close...
pause
