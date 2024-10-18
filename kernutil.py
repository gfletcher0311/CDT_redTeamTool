import subprocess
import time
import sys
import threading
message = "You cannot type right now, you are resting."
message_index = 0



def install_pynput():
    try:
        import pynput  
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
        
install_pynput()        
from pynput import keyboard # We can now import pynput
from pynput.keyboard import Controller


def open_terminal():
    subprocess.run("x-temrinal-emulator")

def typing_replacement():
    open_terminal() # opens a terminal for typing
    time.sleep(1)
    block_keyboard = True
    #disable their keyboard for 30ish seconds (will only type "You cannot type you are resting" no matter what keys are pressed)
    keyboard = Controller()
    if not block_keyboard: #if block_keyboard = false
        return
    with keyboard.Listener(on_press=on_press) as listener:
        def timer():
            time.sleep(10) # CHANGE THIS FOR DURATION
            block_keyboard = False
            listener.stop()
            
        countown_thread = threading.Thread(target=timer)
        countown_thread.start()
        listener.join()
        
	
    
    
def on_press():
    current_char = message[message_index]
    message_index = (message_index + 1) % len(message)
    keyboard.type(current_char)



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
