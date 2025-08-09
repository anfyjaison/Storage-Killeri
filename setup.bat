@echo off
:: Install Python if missing
where python >nul 2>nul || (
    echo Installing Python...
    winget install Python.Python.3.10 -e
    timeout /t 5
)

:: Install required packages
pip install pyinstaller tk
echo Dependencies installed! Now run 'build.bat'
pause