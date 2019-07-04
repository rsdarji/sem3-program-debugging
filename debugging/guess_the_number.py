import random

answer = random.randint(0, 100)

print('Welcome to GUESS THE NUMBER!')

while True:
    user_guess = input('Enter a number: ')
    if not user_guess.isnumeric():
        print('This is not a valid number...')
        continue

    user_guess = int(user_guess)

    if user_guess > answer:
        print('Your number is too big!')
    elif user_guess < answer:
        print('You number is too small...')
    else:
        print('Good job, it was', answer)
        break
