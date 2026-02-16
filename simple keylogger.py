import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym
    
    # Convert special keys to readable format
    if key == "space":
        key = " "
    elif key == "Return":
        key = "\n"
    elif len(key) > 1:
        key = f"[{key}]"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} : {key}")

def main():
    root = tk.Tk()
    root.title("Educational Key Logger (Safe Version)")
    root.geometry("400x200")

    label = tk.Label(root, text="Type inside this window.\nKeys will be logged to key_log.txt",
                     font=("Arial", 12))
    label.pack(pady=40)

    root.bind("<Key>", log_key)

    root.mainloop()

if __name__ == "__main__":
    main()
