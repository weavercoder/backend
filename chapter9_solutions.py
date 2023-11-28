#1 Print 2, 5, 8, 11, 14, 17, 20 with a while loop.
i = 2
print(i, end=' ')
while i < 20:
    i += 3
    print(i, end=' ')
print()



#2 Print 100, 99, 98, ... 1 with a while loop.
i = 100
print(i, end=' ')
while i > 1:
    i -= 1
    print(i, end=' ')
print()



#3 User enters numbers until a negative.  Then sum is printed, excluding negative.
num = 0
total = 0
while num >= 0:
    num = eval(input('Enter a number (negative to stop): '))
    if num >= 0:
        total += num
print(total)



#4 User enters numbers from 1 to 10, stopping with a 5.  Print out how many numbers and whether a 3 was entered.
num = 0
count = 0
flag = False
while num != 5:
    num = eval(input('Enter a number (5 to stop): '))
    count += 1
    if num == 3:
        flag = True
print(count)
if flag:
    print('Yes')
else:
    print('No')



#5 User enters a string of at least five chars, keep prompting until they do so properly.  Print out fifth char of their string.
s = ''
while len(s) < 5:
    s = input('Enter a string of at least 5 characters: ')
print(s[4])



#6 User enters a string of a least five chars, keep prompting until they do.  Then they enter an index in that string.  Keep prompting until it's valid.  Then print out char of their string at that index.
s = ''
while len(s) < 5:
    s = input('Enter a string of at least 5 characters: ')
i = -1
while i < 0 or i >= len(s):
    i = eval(input('Enter an index into that string: '))
    if i < 0 or i >= len(s):
        print('Please enter a valid index.')
print(s[i])



#7 Repeatedly ask the user for a string and print out if it is a palindrome or not.  User stops by pressing enter.
s = 'a'
while s != '':
    s = input('Enter a string: ')
    if s == s[::-1]:
        print('It\'s a palindrome!')
    else:
        print('Not a palindrome.')



#8 Ask for a number between 20 and 100.  Then repeatedly subtract random numbers from 1 to 10 until the number becomes negative.
from random import randint

num = eval(input('Enter a number between 20 and 100: '))
print(num, end=' ')
while num >= 0:
    num -= randint(1,10)
    print(num, end=' ')
print()



#9 Ask for a number, print Collatz sequence starting at that number until 1.
num = eval(input('Enter a positive integer: '))
print(num, end=' ')
while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3*num + 1
    print(num, end=' ')
print()



#10 Create list of random numbers from 1 to 10, stopping when fifth 10 is generated.
from random import randint

L = []
count = 0
while count < 5:
    r = randint(1, 10)
    if r == 10:
        count += 1
    L.append(r)
print(L)


#11 Create a list of 50 random numbers from 1 to 5 with no number appearing twice in a row.
from random import randint

L = [randint(1, 5)]
for i in range(49):
    r = randint(1, 5)
    while r == L[i]:
        r = randint(1, 5)
    L.append(r)
print(L)



#12 Ask for a list, replace first negative with 0.
L = eval(input('Enter a list: '))
i = 0
while i < len(L) and L[i] >= 0:
    i += 1
if i < len(L):
    L[i] = 0
print(L)



#13 Ask for a list, replace first three negatives with 0.
L = eval(input('Enter a list: '))
count = 0
i = 0
while count < 3 and i < len(L):
    while i < len(L) and L[i] >= 0:
        i += 1
    count += 1
    if i < len(L):
        L[i] = 0
print(L)



#14 Ask for string of letters and non-letters, print out string of all the letters up to but not including first non-letter.
s = input('Enter a string with some letters and some non-letters: ')
i = 0
while i < len(s) and s[i].isalpha():
    i += 1
print(s[:i])



#15 Guessing game.
from random import randint

points = 100
while 0 < points < 200:
    r = randint(1, 10)
    guess = eval(input('Your guess: '))
    if guess < r:
        points -= 10
        print('Too low.', end=' ')
    elif guess > r:
        points -= 20
        print('Too high.', end=' ')
    else:
        points += 100
        print('Right!', end=' ')
    print('Score:', points)
if points >= 200:
    print('You win!')
else:
    print('You lose.')



#16 Multiplication game.
from random import randint

guesses = 3
score = 0
while guesses > 0 and score < 200:
    x = randint(2, 99)
    y = randint(2, 99)
    print(x, 'x', y)
    ans = eval(input('Your guess: '))
    if ans == x * y:
        score += x + y
        print('Right!', end=' ')
    else:
        guesses -= 1
        print('Wrong.', end=' ')
    print('Score:', score, '  Guesses left:', guesses)
if guesses == 0:
    print('You lose.')
else:
    print('You win!')



#17 Another guessing game.
from random import randint

money = 50
turn = 10
guess = 1
while guess != 0 and money > 0 and turn >= 2:
    r = randint(1, turn)
    print('Guessing from 1 to', turn)
    guess = eval(input('Your guess: '))
    if guess == 0:
        print('You walk away with this much:', money)
    elif guess != r and 1 <= guess <= turn:
        money *= 2
        print('Computer guessed:', r)
        print('You\'re still alive. You have this much money:', money)
    elif guess < 1 or guess > turn:
        print('Invalid entry')
        print('Game over.  You owe the computer this much:', money)
        money = 0
    else:
        print('Computer guessed:', r)
        print('Game over.  You owe the computer this much:', money)
        money = 0
if turn == 1:
    print('Wow, you made it all the way through and earned this much:', money)
  


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



#19 Create list of the first n primes
n = eval(input('How many primes? '))
Primes = []
p = 2
while n > 0:
    for i in range(2, p//2+1):
        if p % i == 0:
            break
    else:
        Primes.append(p)
        n -= 1
    p += 1
print(Primes)    
        

    
#20 Generate random numbers until a repeat happens.
from random import randint
n = eval(input('Enter n: '))
Previous = []
i = 1
while True:
    r = randint(1, n)
    print(i, '. ', r, sep='')
    if r in Previous:
        break
    Previous.append(r)
    i += 1



#21 Birth policy problem.
from random import choice

boys = 0
girls = 0
for i in range(10000):
    child = choice('BG')
    while child == 'G':
        girls += 1
        child = choice('BG')
    boys += 1
print('Boys:', 100*boys/(boys+girls), '  Girls:', 100*girls/(boys+girls))



#22 How long it takes for a 6 to come up.
from random import randint

max_seq_len = 0
for i in range(10000):
    n = 0
    r = randint(1, 6)
    while r != 6:
        n += 1
        r = randint(1, 6)
    if n > max_seq_len:
        max_seq_len = n
print(max_seq_len)



#23 Collecting all the items of a set.
from random import sample
T = [i for i in range(1,101)]
C = []
n = 0
while len(C) != 100:
    P = sample(T, 20)
    for p in P:
        if p not in C:
            C.append(p)
    n += 1
print(n)



#24 Merge two lists
L1 = eval(input('Enter list 1: '))
L2 = eval(input('Enter list 2: '))
L1.sort()
L2.sort()

M = []
i = 0
j = 0
while i < len(L1) and j < len(L2):
    if L1[i] < L2[j]:
        M.append(L1[i])
        i += 1
    else:
        M.append(L2[j])
        j += 1

if i < len(L1):
    for k in range(i, len(L1)):
        M.append(L1[k])
elif j < len(L2):
    for k in range(i, len(L2)):
        M.append(L2[k])
print(M)
                   
 
