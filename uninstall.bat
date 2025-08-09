@echo off
rmdir /s /q "%ProgramFiles%\Infinite Installer"
del "%USERPROFILE%\Desktop\Infinite Installer.lnk"
echo Uninstalled! Your storage is free again.
pause