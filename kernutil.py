import subprocess
import time

def disableKeyboard():
    #disable their keyboard for 30ish seconds
    result = subprocess.run(["xinput", "list", "| grep",  "-i",  "'keyboard'", "| grep", "-o", "[0-9]*", "| grep", "-o", "[0-9]*"], shell=False)
    result = result.decode()
    result = result.split().strip()
    keyboard_id = result[0] # The master keyboard will be the first number
    disable_cmd = subprocess.run(["xinput", "disable", "{keyboard_id}"])
    time.wait(5)

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
	disableKeyboard
	
	


if __name__ == "__main__":
	main()
