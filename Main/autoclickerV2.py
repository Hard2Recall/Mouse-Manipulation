from pyautogui import *
import pyautogui
import time
import threading
import win32api, win32con
import tkinter as tk
from tkinter import ttk
import keyboard as kb

# Global variable to control clicking
clicking = False
stop_thread = False

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def autoclick_thread():
    global clicking, stop_thread
    while not stop_thread:
        if clicking:
            if use_current_pos.get():
                current_x, current_y = pyautogui.position()
                click(current_x, current_y)
            else:
                # Use manually entered coordinates
                try:
                    x = int(x_entry.get())
                    y = int(y_entry.get())
                    click(x, y)
                except ValueError:
                    pass  # Ignore if coordinates are invalid
            
            # Calculate delay based on CPS
            delay = 1.0 / cps_slider.get()
            time.sleep(delay)
        else:
            time.sleep(0.01)

def keyboard_listener():
    global clicking
    while not stop_thread:
        if kb.is_pressed('q'):
            clicking = not clicking
            update_gui_status()
            time.sleep(0.5)
        if kb.is_pressed('space'):
            # Update position fields with current mouse position
            x, y = pyautogui.position()
            x_entry.delete(0, tk.END)
            x_entry.insert(0, str(x))
            y_entry.delete(0, tk.END)
            y_entry.insert(0, str(y))
            time.sleep(0.5)  # Debounce
        time.sleep(0.01)

def update_gui_status():
    if clicking:
        status_label.config(text="RUNNING", foreground="#2ecc71")
        toggle_button.config(text="Stop (Q)", style="Accent.TButton")
        root.configure(background="#f0f9f0")
    else:
        status_label.config(text="STOPPED", foreground="#e74c3c")
        toggle_button.config(text="Start (Q)", style="TButton")
        root.configure(background="#f9f0f0")

def toggle_clicking():
    global clicking
    clicking = not clicking
    update_gui_status()

def update_cps_label(value):
    cps_value_label.config(text=f"{int(value)} CPS")

def on_closing():
    global stop_thread
    stop_thread = True
    root.destroy()

# Create GUI window with modern styling
root = tk.Tk()
root.title("AutoClicker")
root.geometry("400x420")  # Increased height to fit all elements
root.resizable(False, False)
root.configure(background="#f5f7fa")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Configure styles
style.configure('TFrame', background=root.cget('bg'))
style.configure('TLabel', background=root.cget('bg'), font=('Segoe UI', 9))
style.configure('TButton', font=('Segoe UI', 9), padding=6)
style.configure('Accent.TButton', font=('Segoe UI', 9, 'bold'), 
                background="#e74c3c", foreground="white")
style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'), 
                foreground="#2c3e50")
style.configure('TScale', background=root.cget('bg'))
style.configure('TEntry', font=('Segoe UI', 9), padding=5)
style.configure('TLabelframe', background=root.cget('bg'))
style.configure('TLabelframe.Label', background=root.cget('bg'), 
                font=('Segoe UI', 10, 'bold'))

# Create a main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Header
header = ttk.Label(main_frame, text="AutoClicker", style="Header.TLabel")
header.pack(pady=(0, 20))

# CPS Control Frame
cps_frame = ttk.LabelFrame(main_frame, text="Click Speed", padding="10")
cps_frame.pack(fill=tk.X, pady=(0, 15))

cps_slider = ttk.Scale(cps_frame, from_=1, to=20, orient=tk.HORIZONTAL)
cps_slider.set(10)
cps_slider.pack(fill=tk.X, pady=(5, 0))
cps_slider.bind("<Motion>", lambda e: update_cps_label(cps_slider.get()))

cps_value_frame = ttk.Frame(cps_frame)
cps_value_frame.pack(fill=tk.X, pady=(5, 0))

ttk.Label(cps_value_frame, text="Slow").pack(side=tk.LEFT)
cps_value_label = ttk.Label(cps_value_frame, text="10 CPS", 
                           font=('Segoe UI', 9, 'bold'))
cps_value_label.pack(side=tk.RIGHT)
ttk.Label(cps_value_frame, text="Fast").pack(side=tk.RIGHT)

# Position Frame
pos_frame = ttk.LabelFrame(main_frame, text="Click Position", padding="10")
pos_frame.pack(fill=tk.X, pady=(0, 15))

use_current_pos = tk.BooleanVar(value=True)
current_pos_radio = ttk.Radiobutton(pos_frame, text="Current Mouse Position", 
                                   variable=use_current_pos, value=True)
current_pos_radio.pack(anchor=tk.W, pady=(0, 10))

fixed_pos_radio = ttk.Radiobutton(pos_frame, text="Fixed Position:", 
                                 variable=use_current_pos, value=False)
fixed_pos_radio.pack(anchor=tk.W)

# Coordinates input frame
coord_frame = ttk.Frame(pos_frame)
coord_frame.pack(fill=tk.X, pady=(5, 0))

ttk.Label(coord_frame, text="X:").pack(side=tk.LEFT, padx=(20, 5))
x_entry = ttk.Entry(coord_frame, width=8)
x_entry.pack(side=tk.LEFT)

ttk.Label(coord_frame, text="Y:").pack(side=tk.LEFT, padx=(20, 5))
y_entry = ttk.Entry(coord_frame, width=8)
y_entry.pack(side=tk.LEFT)

get_pos_button = ttk.Button(coord_frame, text="Get Position (Space)", 
                           command=lambda: [x_entry.delete(0, tk.END), 
                                           x_entry.insert(0, str(pyautogui.position()[0])),
                                           y_entry.delete(0, tk.END),
                                           y_entry.insert(0, str(pyautogui.position()[1]))])
get_pos_button.pack(side=tk.RIGHT)

# Control Frame
control_frame = ttk.Frame(main_frame)
control_frame.pack(fill=tk.X, pady=(15, 10))

toggle_button = ttk.Button(control_frame, text="Start (Q)", 
                          command=toggle_clicking, width=15)
toggle_button.pack(side=tk.LEFT)

status_label = ttk.Label(control_frame, text="STOPPED", 
                        font=('Segoe UI', 10, 'bold'), foreground="#e74c3c")
status_label.pack(side=tk.RIGHT)

# Instructions
instructions_frame = ttk.Frame(main_frame)
instructions_frame.pack(fill=tk.X, pady=(20, 0))

ttk.Label(instructions_frame, text="Press 'Q' to start/stop clicking", 
         font=('Segoe UI', 9), foreground="#7f8c8d").pack(anchor=tk.W)
ttk.Label(instructions_frame, text="Press 'Space' to get current mouse position", 
         font=('Segoe UI', 9), foreground="#7f8c8d").pack(anchor=tk.W)
ttk.Label(instructions_frame, text="Close window to exit", 
         font=('Segoe UI', 9), foreground="#7f8c8d").pack(anchor=tk.W)

# Start the threads
autoclick_thread = threading.Thread(target=autoclick_thread, daemon=True)
keyboard_thread = threading.Thread(target=keyboard_listener, daemon=True)

autoclick_thread.start()
keyboard_thread.start()

# Set initial position to current mouse position
x, y = pyautogui.position()
x_entry.insert(0, str(x))
y_entry.insert(0, str(y))

# Initialize the CPS label
update_cps_label(cps_slider.get())

root.mainloop()