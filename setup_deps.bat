@echo off
echo Installing Dependencies...

:: Install Node.js (if not installed)
where node >nul 2>nul || (
    echo Node.js not found. Downloading...
    curl -o node-setup.msi https://nodejs.org/dist/v18.16.0/node-v18.16.0-x64.msi
    start /wait node-setup.msi
)

:: Install Appium & Drivers
npm install -g appium
appium driver install uiautomator2

:: Install Python Dependencies
echo Checking for Python installation...

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python manually from https://www.python.org/downloads/
    pause
    exit /b
)

:: Get the current script directory
set "CURRENT_DIR=%~dp0"
echo %CURRENT_DIR%


:: Install required Python packages
echo Installing required dependencies...
pip install -r "%CURRENT_DIR%\requirements.txt"

echo Installation Complete! Press any key to exit.
pause
