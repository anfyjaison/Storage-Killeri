@echo off
:: Create a blank icon file if none exists
if not exist "icon.ico" (
  echo Creating dummy icon file...
  copy nul "icon.ico" > nul
  attrib +h "icon.ico"
)