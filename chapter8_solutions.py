#1 Demoing the choice(), sample(), and shuffle() functions.
from random import choice, sample, shuffle
L = eval(input('Enter a list of at least four items: '))
print('(a) A random item:', choice(L))
print('(b) Three random items:', sample(L, 3))
shuffle(L)
print('(c) Shuffled list:', L)



#2 50 coin flips.
from random import choice

s = ''
for i in range(100):
    s += choice('HT')
print(s)



#3 1000 random As, Bs, Cs, and Ds, where 60% chance of A, 30% chance of B, 8% chance of C, 2% chance of D.
from random import choice

letters = 'A'*60 + 'B'*30 + 'C'*8 + 'D'*2
s = ''
for i in range(1000):
    s += choice(letters)
print(s)



#4 Generate a random password.
from random import choice

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
n = eval(input('How long do you want your password: '))
s = ''
for i in range(n):
    s += choice(chars)
print(s)



#5 Generate random sentences.
from random import choice

Verbs = ['goes', 'takes', 'gets', 'opens', 'sees', 'lifts',
         'tries', 'smells', 'sets up', 'leaves']
Nouns = ['dog', 'cat', 'house', 'toy', 'hair', 'water',
         'door', 'sky', 'sun', 'box']
Adjectives = ['old', 'new', 'dirty', 'shiny', 'red', 'cold',
              'fake', 'happy', 'funny', 'heavy']
print('The', choice(Adjectives), choice(Nouns), choice(Verbs), 'the', choice(Nouns)+'.')



#6 Generate random sentences, make sure the nouns are different.
from random import choice, sample

Verbs = ['goes', 'takes', 'gets', 'opens', 'sees', 'lifts',
         'tries', 'smells', 'sets up', 'leaves']
Nouns = ['dog', 'cat', 'house', 'toy', 'hair', 'water',
         'door', 'sky', 'sun', 'box']
Adjectives = ['old', 'new', 'dirty', 'shiny', 'red', 'cold',
              'fake', 'happy', 'funny', 'heavy']
N = sample(Nouns, 2)
print('The', choice(Adjectives), N[0], choice(Verbs), 'the', N[1]+'.')



#7 Create and shuffle a deck of cards.
from random import shuffle

L = []
for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
    for value in ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven'
                  'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']:
        L.append(value + ' of ' + suit)
shuffle(L)
print(L[:5])



#8 Replace 3 indices in a word with asterisks.
from random import sample

s = input('Enter a word: ')

Indices = []
for i in range(len(s)):
    Indices.append(i)
Spots = sample(Indices, 3)

t = ''
for i in range(len(s)):
    if i in Spots:
        t += '*'
    else:
        t += s[i]
print(t)



#9 One-by-one replace the characters in a word with asterisks.
from random import choice

s = input('Enter a word: ')
Indices = []
for i in range(len(s)):
    Indices.append(i)
for i in range(len(s)):
    c = choice(Indices)
    Indices.remove(c)
    s = s[:c] + '*' + s[c+1:]
    print(s)



#10 Randomly swap three pairs of elements in a list.
L = []
Indices = []
for i in range(1, 21):
    L.append(i)
    Indices.append(i-1)

for i in range(3):
    S = sample(Indices, 2)
    L[S[0]], L[S[1]] = L[S[1]], L[S[0]]
    # note a better way is this:
    # a, b = sample(Indices)
    # L[a], L[b] = L[b], L[a]
print(L)



#11 Create a list of words from a string.
s = input('Enter a bunch of words separated by spaces: ')
print('A list of the individual words:', s.split())



#12 Join emails with semicolons.
L = eval(input('Enter a list of emails as a list of strings: '))
print('Joined by semicolons:', ';'.join(L))



#13 Pick out month, day, and year from a date
s = input('Enter a date in the month/day/year format: ')
L = s.split('/')
print('month: ', L[0])
print('day: ', L[1])
print('year: ', L[2])



#14 Capitalize first letter of each word.
s = input('Enter a bunch of words separated by spaces: ')
L = []
for word in s.split():
    L.append(word[0].upper() + word[1:])
print(' '.join(L))



#15 List of rearrangements.
from itertools import permutations
for x in permutations('abcd'):
    print(''.join(x))



#16 Print out the last word of every sentence.
s = input('Enter several sentences ending with periods (with no periods except at the end of sentences): ')
for sentence in s.split('.'):
    words = sentence.split(' ')
    print(words[-1])



#17 List comprehensions.
#(a) List of square roots
from math import sqrt
L = [round(sqrt(i), 2) for i in range(1,100)]
print('(a):', L)

#(b) Add 1 to everything in a list
L = eval(input('Enter a list of integers: '))
M = [x+1 for x in L]
print('(b):', M)

#(c) Only the evens from a list
L = eval(input('Enter a list of integers: '))
M = [x for x in L if x%2==0]
print('(c):', M)

#(d) All the entries from a list with negatives replaced by 0
L = eval(input('Enter a list of integers: '))
M = [max(x, 0) for x in L]
print('(d):', M)

#(e) All the letters (but not other characters) of a string
s = input('Enter a string:')
L = [c for c in s if c.isalpha()]
print('(e):', L)

#(f) Given a list of lists, create a list of the last items in each list
L = eval(input('Enter a list of lists: '))
M = [S[-1] for S in L]
print('(f):', M)

#(g) Create list of frequencies of letters in a string
s = input('Enter a string of lowercase letters: ')
L = [s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz']
print('(g):', L)

#(h) List of indices in which two strings differ
s = input('Enter a string: ')
t = input('Enter another string of the same length: ')
L = [i for i in range(len(s)) if s[i] != t[i]]
print('(h):', L)



#18 Given a list of test scores, break them into As, Bs, etc.
L = eval(input('Enter a list of test scores: '))
M = [[], [], [], [], []]
for x in L:
    if x >= 90:
        M[0].append(x)
    elif x >= 80:
        M[1].append(x)
    elif x >= 70:
        M[2].append(x)
    elif x >= 60:
        M[3].append(x)
    else:
        M[4].append(x)
print(M)



#19 Create 6 x 6 list of random integers from 0 to 9 and do stuff with it.
from random import randint

L = [[randint(0,9) for j in range(6)] for i in range(6)]

#alternate solution if you don't like list comprehensions:
#L = []
#for i in range(6):
#    M = []
#    for j in range(6):
#        M.append(randint(0,9))
#    L.append(M)

#(a) Print the list
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

#(b) How many zeroes are in the list
count = 0
for i in range(6):
    for j in range(6):
        if L[i][j] == 0:
            count += 1
print(count)

#(c) Smallest thing in first row (row 0)
print(min(L[0]))

#(d) Largest thing in the third column (column 2)
print(max(L[i][2] for i in range(len(L))))

#(e) Sum of the entries in the last row
print(sum(x for x in L[-1]))

#alternate solution not using list comprehensions
#total = 0
#for i in range(6):
#    total += L[5][i]
#print(total)

#(f) Flatten the list
M = [L[i][j] for i in range(len(L)) for j in range(len(L[i]))]
print(M)

#(g) Transpose list
M = [[0]*len(L) for i in range(len(L))]
for i in range(len(L)):
    for j in range(len(L)):
        M[j][i] = L[i][j]

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=' ')
    print()



#20 Battleship tell if a cell is a hit or miss on a 10 x 10 list.
from random import randint

L = [[randint(0,1) for j in range(10)] for i in range(10)]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

r = eval(input('Enter row: '))
c = eval(input('Enter column: '))

if L[r][c] == 1:
    print('Hit')
else:
    print('Miss!')
        


#21 Create 6 x 6 list and add up entries in a range specified by user.
from random import randint

L = [[randint(0,2) for j in range(6)] for i in range(6)]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()
    
r1 = eval(input('Enter starting row: '))
r2 = eval(input('Enter ending row: '))
c1 = eval(input('Enter starting column: '))
c2 = eval(input('Enter ending column: '))

total = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        total += L[i][j]
print(total)



#22 Add up entries on or below the main diagonal of a 15 x 15 list of 1s, 2s, and 3s. 
from random import randint

L = [[randint(0,2) for j in range(15)] for i in range(15)]

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

total = 0
for i in range(len(L)):
    for j in range(i, len(L[i])):
        total += L[i][j]
print(total)



#23 Determine if there are consecutive horizontal or vertical zeroes in a random 6x6 list of integers from 0 to 5.
from random import randint

L = [[randint(0,5) for j in range(6)] for i in range(6)]

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

flag = False
# check horizontal
for i in range(len(L)):
    for j in range(1,len(L[i])):
        if L[i][j] == L[i-1][j] == 0:
            flag = True
# check vertical
for i in range(1,len(L)):
    for j in range(len(L[i])):
        if L[i][j-1] == L[i][j] == 0:
            flag = True

if flag:
    print('There are consecutive zeroes.')
else:
    print('No consecutive zeroes.')



#24 Create an n x n shape of an X in a box.
n = eval(input('Enter the size: '))
L = [[' ']*n for i in range(n)]
for i in range(n):
    L[0][i] = L[-1][i] = L[i][0] = L[i][-1] = L[i][i] = L[i][n-i-1] = '#'

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=' ')
    print()

#25 10 x 10 list of exactly 10 zeroes and 90 ones, randomly ordered.
from random import shuffle

L = [0]*10 + [1]*90
shuffle(L)
M = [[0]*10 for i in range(n)]
for i in range(len(L)):
    M[i // 10][i % 10] = L[i]

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=' ')
    print()



#26 10 x 10 list of zeroes and ones where each entry has a 90% chance of being 0 and a 10% chance of being 1.
from random import choice

L = [0]*10 + [1]*90
M = [[choice(L) for j in range(10)] for i in range(10)]

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=' ')
    print()
