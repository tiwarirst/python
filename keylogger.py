from pynput import keyboard
def on_press(key):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')
# Function to stop listener when 'esc' is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
