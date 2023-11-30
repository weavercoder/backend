#12 100 random zeros and ones, zeroes twice as likely
from random import randint
for i in range(100):
    r = randint(0,2)
    if r == 2:
        print('0', end='')
    else:
        print('', end='')
print()