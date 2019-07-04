import random

win_table = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

def beats(hand1, hand2):
    if win_table[hand1] == hand2:
        return True
    else:
        return False

def play_once():
    choices = list(win_table.keys())
    user_hand = input("Enter your choice [{}]: ".format('/'.join(choices)))
    cpu_hand = random.choice(choices)

    while user_hand.lower() not in choices:
        print('Invalid choice!')
        user_hand = input("Enter your choice [{}]: ".format('/'.join(choices))).lower()

    print('Your hand: {}\t Computer hand: {}'.format(user_hand, cpu_hand))

    if beats(user_hand, cpu_hand):
        print('You win!')
        return 1
    elif beats(cpu_hand, user_hand):
        print('You lost...')
        return -1
    else:
        print('Draw.')
        return 0

def play():
    score = 0
    while True:
        score += play_once()
        print('Your current score:', score)
        command = input('Play again? [y/n]: ').lower()
        while command not in ('y', 'n'):
            command = input('Play again? [y/n]: ').lower()

        if command == 'n':
            break

if __name__ == "__main__":
    play()