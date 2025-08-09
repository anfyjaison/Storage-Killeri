import os
import sys
import subprocess
from PIL import Image, ImageDraw  # For creating an icon if needed

def create_dummy_icon():
    """Create a simple red/blue icon if none exists"""
    try:
        img = Image.new('RGBA', (256, 256), (255, 0, 0, 255))  # Red background
        draw = ImageDraw.Draw(img)
        draw.ellipse((50, 50, 206, 206), fill=(0, 0, 255, 255))  # Blue circle
        img.save('icon.ico', sizes=[(256, 256)])
        print("Created default icon.ico")
    except Exception as e:
        print(f"Couldn't create icon: {e}")
        return False
    return True

def build_app():
    # Check for icon
    if not os.path.exists("icon.ico"):
        if not create_dummy_icon():
            print("Proceeding without icon...")
            icon_arg = ""
        else:
            icon_arg = "--icon=icon.ico"
    else:
        icon_arg = "--icon=icon.ico"

    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "Infinite Installer",
        "--distpath", "dist",
        "--workpath", "build",
        "--specpath", ".",
    ]
    
    if icon_arg:
        cmd.append(icon_arg)
    
    cmd.append("infinite_installer.py")

    # Run build
    try:
        print("Building EXE...")
        subprocess.run(cmd, check=True)
        print("\nSUCCESS! EXE created in /dist folder")
        
        # Create installer if Inno Setup is available
        if os.path.exists(r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"):
            print("Creating installer...")
            subprocess.run([
                r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
                "setup.iss"
            ])
            print("Installer created in /Output folder")
        else:
            print("Inno Setup not found - skipping installer creation")
            
    except subprocess.CalledProcessError as e:
        print(f"\nBUILD FAILED: {e}")
        return False
    
    return True

if __name__ == "__main__":
    if not os.path.exists("infinite_installer.py"):
        print("Error: infinite_installer.py not found!")
        sys.exit(1)
        
    build_app()
    input("Press Enter to exit...")