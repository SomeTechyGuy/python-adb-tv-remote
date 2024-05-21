import subprocess
import tkinter as tk
import pyautogui

# Replace with your Fire TV's IP address
FIRE_TV_IP = "10.0.0.76"

def send_key(key_code):
    command = f"adb shell input keyevent {key_code}"
    subprocess.run(command, shell=True)

def send_text():
    text = entry.get()
    # Replace spaces with "%s" for adb shell input text
    text_for_adb = text.replace(" ", "%s")
    command = f"adb shell input text \"{text_for_adb}\""
    subprocess.run(command, shell=True)
    entry.delete(0, tk.END)  # Clear the text box

def create_button(parent, text, key_code, row, column, padx=5, pady=5):
    button = tk.Button(parent, text=text, command=lambda: send_key(key_code), width=4, height=1)
    button.grid(row=row, column=column, padx=padx, pady=pady)

def handle_key_press(event):
    key = event.keysym
    if key == "Up":
        send_key(19)
    elif key == "Down":
        send_key(20)
    elif key == "Left":
        send_key(21)
    elif key == "Right":
        send_key(22)
    elif key == "Return":
        send_key(23)  # Enter key for "OK"
    elif key == "BackSpace":
        send_key(67)  # Backspace key
    elif key == "Escape":
        send_key(4)  # Escape for "Back"
    elif key == "space":
        send_key(85)  # Space for "Play/Pause"
    elif key == "Super_L":
        send_key(3)  # Windows key for "Home"


root = tk.Tk()
root.title("Fire TV Remote")

# Main buttons area
frame = tk.Frame(root)
frame.pack()

# Top row (Navigation)
create_button(frame, "Up", 19, 0, 1)
create_button(frame, "Left", 21, 1, 0)
create_button(frame, "Select", 23, 1, 1)
create_button(frame, "Right", 22, 1, 2)
create_button(frame, "Down", 20, 2, 1)

# Middle row (Play/Pause, Back, Home)
create_button(frame, "Play/Pause", 85, 3, 0)
create_button(frame, "Back", 4, 3, 1)
create_button(frame, "Home", 3, 3, 2)

# Bottom row (Volume)
create_button(frame, "Volume+", 24, 4, 0)
create_button(frame, "Volume-", 25, 4, 2)

# Text box and send button
entry = tk.Entry(root)
entry.pack(pady=5)
send_button = tk.Button(root, text="Send", command=send_text)
send_button.pack()

# Bind keyboard events
root.bind("<KeyPress>", handle_key_press)

root.mainloop()
