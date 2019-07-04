deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10' 'Jack', 'Queen', 'King', 'Ace']
hand = []

print('You are asked to choose five cards from the following deck.')
print('Available cards:', *deck)

while len(hand) < 5:
    choice = input('Choose one more card: ').capitalize()
    try:
        deck.remove(choice)
        hand.append(choice)
    except ValueError:
        print('This choice is not available.')
        continue

print('Here is you hand: ', *hand)

