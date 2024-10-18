import subprocess
import time
import threading
def install_pynput():
    try:
        import pynput  
    except ModuleNotFoundError:
        subprocess.run(["apt", "install", "python3-pynput", "-y"])

install_pynput()

from pynput.keyboard import Key, Controller
from pynput import keyboard

def open_terminal_with_text(text):
    # Using a shell command that maintains the terminal open
    command = f'bash -c "echo \'{text}\'; read -p \'keep touching grass\'"'
    subprocess.Popen(['x-terminal-emulator', '-e', command])


def grass():
    ascii_grass = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣇⠀⣀⠀⠀⢀⣠⡶⢟⣩⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⢤⣤⣄⡀⠀⢀⡿⣿⣼⣻⢁⣴⠟⢥⣿⠟⠁⠀⠀⠀⠀⠀⠀⣄⠀⢠⣾⡏⢀⣠⣾⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠻⣝⠳⣾⡇⣿⠃⣯⠞⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⢠⠀⢿⢧⣺⠉⣿⠞⣹⣏⣤⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⠀⠁⠈⠐⠏⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡾⠌⠳⠀⠈⠀⠙⠁⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣷⠀⠀⠀⠀⡄⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣾⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⡿⠀⢹⠀⢀⣴⡾⢻⡆⠀⢸⡿⣆⠀⠀⢀⣠⢀⣴⠞⣩⡾⣁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢦⣄⢸⡇⠀⢸⣶⢿⡿⠀⡌⠳⠀⣼⠇⣿⢠⡼⣿⣿⡟⠁⢠⣟⣥⣼⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣌⣷⠙⢿⡇⠀⢸⠇⣿⣠⡾⠻⡕⣴⡏⠀⣽⠏⠀⣿⠋⠀⠀⣿⡟⢩⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠙⡇⠀⠀⠀⠈⠀⠹⠏⠀⠀⠙⠟⠀⠀⠀⠀⠀⠉⠀⠀⠀⠸⠷⣾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣄⠀⢰⡏⣸⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⢠⣧⠀⠀⢀⣀⠀⠀
⠀⢠⣿⠙⣦⡟⢠⣿⣿⢏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣀⠀⠀⣿⢿⡄⣸⡿⣿⣤⡶⣿⠏⠀⠀
⣐⣟⢹⡆⠘⡇⢸⠟⣿⡼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡏⠛⢦⡏⠀⢻⠏⠀⣽⠛⢱⣿⣴⣷⠄
⠉⢻⡟⠓⠀⡇⠃⢸⡟⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣬⣧⡀⠀⠃⠀⠀⠀⠀⠁⠀⠀⠟⠿⠃⠀
⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠶⠶⣬⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    open_terminal_with_text(ascii_grass)  # Open a terminal to show the grass message
    
def alert():
    # Alert for telling blue team to take a break
    print("Time to take a break!")
    
def on_press(key):
    if key == keyboard.Key.enter:
        grass()
def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running
    grass()
    