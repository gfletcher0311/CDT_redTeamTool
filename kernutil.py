import subprocess
import time
import sys
import threading
message = "You cannot type right now, you are resting."
message_index = 0
pause_duration = 10 # duration to activate (in seconds)
keyboard_blocked = True

def install_pynput():
    try:
        import pynput  
    except ModuleNotFoundError:
        subprocess.run(["apt", "install", "python3-pynput", "-y"])
        
install_pynput()        
from pynput import keyboard # We can now import pynput
from pynput.keyboard import Controller
keyboard_control = Controller()

def open_terminal():
    #Simple function which will open a terminal on a linux machine
    subprocess.Popen(["x-terminal-emulator"])

def typing_replacement():
    # Replaces all keystroeks with the characters to the global varaibale message
    threading.Thread(target=typing_replacement_helper).start()
    time.sleep(1)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
def typing_replacement_helper():
    global keyboard_blocked
    time.sleep(pause_duration)
    keyboard_blocked = False  # Unblock the keyboard after the pause
    
def on_press(key):
    global message
    global message_index
    global keyboard_blocked
    if keyboard_blocked:
        try:
            char = message[message_index]
            keyboard_control.type(char)
            message_index = (message_index+1) % len(message)
        except:
            print("error printing character")
        
 


def grass():
    ascii_grass= """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡇⠀⠀⡆⠀⠀⠀⠀⠀⢀⠀⠀⣼⣿⠀⠀⠀⢰⠀⠀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⢸⡇⠀⠀⣷⠀⠀⢠⠀⠀⣸⡀⠀⣿⣿⠀⠀⠀⣼⡇⠀⠀⣼⠀⠀⢠⡆⠀
⠀⠀⣼⡇⠀⠀⣿⡆⠀⣾⠀⠀⣿⡇⢀⣿⣿⠀⠀⠀⣿⣿⠀⢀⣿⡇⠀⢸⡇⠀
⠀⠀⣿⣇⠀⢠⣿⣧⢀⣿⠀⢰⣿⡇⢸⣿⣿⡇⠀⢠⣿⣿⡆⢸⣿⡇⠀⣿⣷⠀
⠀⢀⣿⣿⠀⢸⣿⣿⢸⣿⡄⣼⣿⣷⢸⣿⣿⣿⣀⣾⣿⣿⡇⣿⣿⣷⢰⣿⣿⠀
⠀⢸⣿⣿⡇⢸⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀
		Touch Grass please. . .
    """
    #Open a terminal that tells them to cut grass, if closed it opens again until the tiemr runs out
    pass



def alert():
    #Alert for telling blue team to take a break
    pass




def main():
    typing_replacement()
	


if __name__ == "__main__":
	main()
