import pyautogui
import time
import os
import subprocess
import platform
import webbrowser

def open_target(target):
    """
    Opens an application, file, or URL depending on the input.
    - If target is a URL → opens in default browser
    - If target is a file → opens with default app
    - If target is an app name → launches it
    """
    system = platform.system()

    # Case 1: URL
    if target.startswith("http://") or target.startswith("https://"):
        webbrowser.open(target)
        print(f"Opened URL: {target}")
        return

    # Case 2: File
    if os.path.exists(target):
        if system == "Windows":
            os.startfile(target)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", target])
        elif system == "Linux":
            subprocess.Popen(["xdg-open", target])
        print(f"Opened file: {target}")
        return

    # Case 3: Application
    try:
        if system == "Windows":
            subprocess.Popen(target)
        elif system == "Darwin":
            subprocess.Popen(["open", "-a", target])
        elif system == "Linux":
            subprocess.Popen([target])
        print(f"Launched application: {target}")
    except Exception as e:
        print(f"Could not open {target}: {e}")


def type_text(text, delay=0.1):
    """Types text with a small delay between characters."""
    time.sleep(2)  # give user time to focus app
    pyautogui.write(text, interval=delay)


def click_position(x, y):
    """Clicks at specific (x,y) screen coordinates."""
    pyautogui.click(x=x, y=y)


def rename_file(old_path, new_path):
    """Renames a file if it exists."""
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} → {new_path}")
    else:
        print("File not found.")


if __name__ == "__main__":
    # Demo 1: open app
    open_target("notepad.exe")  # Windows example
    time.sleep(2)
    type_text("Hello from Universal Automator!")

    # Demo 2: open file
    # open_target("C:/Users/you/Documents/sample.pdf")

    # Demo 3: open URL
    # open_target("https://google.com")
