@echo off
echo Setting up Android SDK environment...

:: Get the current script directory
set "CURRENT_DIR=%~dp0"
set "SDK_DIR=%CURRENT_DIR%SDKTools"
set "PLATFORM_TOOLS_DIR=%SDK_DIR%\platform-tools"
set "BUILD_TOOLS_DIR=%SDK_DIR%\build-tools"
set "CMDLINE_TOOLS_DIR=%SDK_DIR%\cmdline-tools"
set "PLATFORM_DIR=%SDK_DIR%\platforms"
set "TOOLS_DIR=%SDK_DIR%\tools"

:: Verify that SDKTools exists
if not exist "%SDK_DIR%" (
    echo ERROR: SDKTools folder not found! Please make sure it exists in the same directory as this script.
    pause
    exit /b
)

:: Add SDK paths to the system PATH
setx PATH "%PLATFORM_TOOLS_DIR%;%BUILD_TOOLS_DIR%;%CMDLINE_TOOLS_DIR%\bin;%TOOLS_DIR%\bin;%PATH%" /M
echo Android SDK paths added to system PATH.

:: Verify installation
echo Verifying ADB installation...
"%PLATFORM_TOOLS_DIR%\adb.exe" version

echo Setup complete! Close this window and restart your terminal.
pause
