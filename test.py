import subprocess
import time
import threading
message = "You cannot type right now, you are resting."
message_index = 0
pause_duration = 5  # duration to activate (in seconds)
keyboard_blocked = True # if true = script running

def install_pynput():
    try:
        import pynput  
    except ModuleNotFoundError:
        subprocess.run(["apt", "install", "python3-pynput", "-y"])

install_pynput()

from pynput.keyboard import Key, Controller  # Ensure pynput is installed
from pynput import keyboard

keyboard_control = Controller()

def open_terminal():
    # Simple function which will open a terminal on a linux machine
    subprocess.Popen(["x-terminal-emulator"])

def typing_replacement():
    # Replaces all keystrokes with the characters to 'message' variable
    threading.Thread(target=typing_replacement_helper).start()
    
    

def typing_replacement_helper():
    global keyboard_blocked
    time.sleep(pause_duration)
    keyboard_blocked[0] = False  # Unblock the keyboard after the pause
    

    

def on_press(key):
    pass
    
    
def alert():
    # Alert for telling blue team to take a break
    print("Time to take a break!")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running
    typing_replacement()
    
    

if __name__ == "__main__":
    main()
