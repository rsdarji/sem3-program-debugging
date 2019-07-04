import random
import time

hidden_number = random.randint(0, 10)
start = time.time()

print('The computer randomly chose a number from 0 to 10.')
print('Try to guess it as fast a possible!')
print(hidden_number)
guess = int(input('>>> '))
while guess != hidden_number:
   print('Try again!')
   guess = (input('>>> '))

total_time = time.time() - start

print('Well, it took you {:.2f}s'.format(total_time))