import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import keyboard
from win32 import win32gui

CONTROL_KEYS = [
    'nach-links',
    'nach-rechts',
    'nach-oben',
    'nach-unten',
    'strg',
    'umschalt',
    'feststell',
    'tab',
    'shift',
    'enter',
    'backspace',
    '*',
    'f1',
    'f2',
    'f3',
    'f4',
    'f5',
    'f6',
    'f7',
    'f8',
    'f9',
    'f10',
    'f11',
    ',',
    '.',
    '-',
    '+',
    '<',
    'linke windows',
    'alt',
    'alt gr'
    'rechte windows',
    'anwendung',
    'strg-rechts'
]

window = tk.Tk()
window.title("Shortcut-Viewer")

# Set the window size and position
window.geometry("100x1500+0+0")

# Set the window to have a blurred background
window.attributes("-alpha", 0.6)

# Set the window to be on top of other programs
window.attributes("-topmost", True)

# Set the window background color
window.config(bg="#f0f0f0")

# Get the window handle
hwnd = win32gui.GetParent(window.winfo_id())

# Make the window visible on all virtual desktops
# TODO: get correct values for the defines
# (needed to show window on all virtual desctops)
# win32gui.SetWindowLong(hwnd, win32gui.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32gui.GWL_EXSTYLE) | win32gui.WS_EX_TOOLWINDOW | win32gui.WS_EX_APPWINDOW)


win32gui.SetWindowLong(hwnd, -20, win32gui.GetWindowLong(hwnd, -20) | 0x00000080 | 0x00040000)

def display_text(text, timeout="3000"):
    # Create a label widget with the given text
    label = tk.Label(window, text=text, font=("Helvetica", 12, "bold"))
    
# Pack t                he label widget into the window
    label.pack()

    def clear_text():
        label.destroy()

    # Schedule the label text to be cleared after the specified timeout
    window.after(timeout, clear_text)



def on_key_press(event):
    current_keys = keyboard.get_hotkey_name()
    
    if not any(key in current_keys.split("+") for key in CONTROL_KEYS):
        return
    
    print(f"{current_keys}")
    # Update the overlay image with the current key combination
    display_text(current_keys.replace("+", " + "))

keyboard.on_press(on_key_press)

# Start the Tkinter event loop
window.mainloop()

keyboard.wait()
