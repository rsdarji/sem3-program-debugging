import sys

# This checks for the Python version
if sys.version_info.major < 3:
    print("WARNING: you are using Python2. Switch to Python3.")
    exit(1)

def set_player_name():
    global player
    name = input('Enter a new player name: ')
    player = name

def play():
    # Load the file from an external resource
    import base64

    try:
        with open('game.bin', 'rb') as f:
            exec(base64.b64decode(f.read().strip()))
    finally:
        print('The game could not be loaded.')
        exit()


def quit():
    print("Thank you!")
    exit()

def run_command(command_number):
    command_executor = menu[str(command_number)][1]
    command_executor()

menu = {
    "1": ("Play", play),
    "2": ("Enter player name", set_player_name),
    "3": ("Quit", quit)
}

# Default player name
player = "Player1"

if __name__ == "__main__":
    while True:
        print("\nWelcome {}\n".format(player))
        print("==========\n== Menu ==\n==========")
        for number in menu:
            print(number + ". " + menu[number][0])

        command = int(input("\nChoose an option: "))
        run_command(command)