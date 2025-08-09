@echo off
pyinstaller --onefile --windowed --icon=icon.ico --name "Infinite Installer" infinite_installer.py
echo EXE built in 'dist' folder!
pause