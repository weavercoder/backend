#18 Get a string of letters and non-letters, randomly remove non-letters one at a time until there are no more
from random import choice

s = input('Enter a string with some letters and some non-letters: ')
while True:
    Indices = []
    for i in range(len(s)):
        if not s[i].isalpha():
            Indices.append(i)
    if len(Indices) == 0:
        break
    j = choice(Indices)
    s = s[:j] + s[j+1:]
    print(s)

