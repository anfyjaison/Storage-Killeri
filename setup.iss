[Setup]
AppName=Infinite Installer
AppVersion=1.0
AppPublisher=Useless Apps Inc.
DefaultDirName={pf}\Infinite Installer
DefaultGroupName=Infinite Installer
OutputDir=Output
OutputBaseFilename=InfiniteInstaller_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

[Files]
Source: "dist\Infinite Installer.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Infinite Installer"; Filename: "{app}\Infinite Installer.exe"
Name: "{commondesktop}\Infinite Installer"; Filename: "{app}\Infinite Installer.exe"

[Run]
Filename: "{app}\Infinite Installer.exe"; Description: "Run Infinite Installer"; Flags: postinstall nowait