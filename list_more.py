'''from random  import choice
s='abcdefhgijklmnopqrstvuwxyz&*&^%'
for i in range(100000):
  print(choice(s),end='')'''

from random import shuffle
players = ['joe','ben','rich']
shuffle(players)

for p in players:
    print(p)
 

