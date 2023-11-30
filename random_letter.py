#12 Print user-entered letter a random number of times
from random import randint

letter = input('Enter a letter: ')
num_times = randint(1, 10)
for i in range(num_times):
    print(letter ,end='')

print()