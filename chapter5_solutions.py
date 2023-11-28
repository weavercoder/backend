#1 50 random numbers from 1 though 9, print out the numbers and how many fives
from random import randint

count = 0
for i in range(50):
    r = randint(1, 9)
    print(r, end='')
    if r == 5:
        count += 1
print()
print('There were', count, 'fives.')



#2 Add up 1 through 100
total = 0
for i in range(1, 101):
    total += i
print(total)



#3 Add up the sines of the numbers 1 to 100
from math import sin

total = 0
for i in range(1, 101):
    total += sin(i)
print(total)



#4 Add up 1+3+5+7+...+999
total = 0
for i in range(1,1000,2):
    total += i
print(total)



#5 Ask for 10 numbers, print sum and how many positives
total = 0
count = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    total += num
    if num > 0:
        count += 1
print('There were', count, 'positives, and the sum is', total)


#6 Generate 10 random numbers, user guesses, print out how many right and wrong
from random import randint

right = 0
for i in range(10):        
    r = randint(1, 5)
    guess = eval(input('Your guess (1-5): '))
    if guess == r:
        print('Right!')
        right += 1
    else:
        print('Wrong.')
print('You got', right, 'right and', 10-right, 'wrong.')



#7 Generate 10 random numbers, user guesses, keep score (+5 for right, +2 for close, -1 for wrong)
from random import randint

score = 0
for i in range(10):        
    r = randint(1, 10)
    guess = eval(input('Your guess (1-10): '))
    if guess == r:
        print('Right!')
        score += 5
    elif abs(guess-r) == 1:
        print('Close!')
        score += 2
    else:
        print('Wrong.')
        score -= 1
    print('Current score:', score)



#8 Simulation to estimate probability of rolling doubles
from random import randint

count = 0
for i in range(10000):
    r1 = randint(1, 6)
    r2 = randint(1, 6)
    if r1 == r2:
        count += 1
print('Percentage of doubles:', 100*count/10000)



#9 Simulation to estimate probability of a Yahtzee
from random import randint

count = 0
for i in range(10000):
    r1 = randint(1, 6)
    r2 = randint(1, 6)
    r3 = randint(1, 6)
    r4 = randint(1, 6)
    r5 = randint(1, 6)
    if r1 == r2 == r3 == r4 == r5:
        count += 1
print('Percentage of Yahtzees:', 100*count/10000)
    


#10 Swap the smaller of w and x with the smaller of y and z
w = eval(input('Enter w: '))
x = eval(input('Enter x: '))
y = eval(input('Enter y: '))
z = eval(input('Enter z: '))

if w < x and y < z:
    w, y = y, w
elif w < x and z <= y:
    w, z = z, w
elif x < w and y < z:
    x, y = y, x
else:
    x, z = z, x
print('w x y z:', w, x, y, z)


#11 Generate 20 random numbers and print out if any 10s appeared
from random import randint

got10 = False
for i in range(20):
    r = randint(1, 10)
    print(r, end=' ')
    if r == 10:
        got10 = True
print()
if got10:
    print('A 10 was generated.')
else:
    print('No 10 appeared.')



#12 Generate 20 random numbers and print out whether any value was generate twice in a row          
from random import randint

repeat = False
previous = randint(1, 10)
print(previous, end=' ')
for i in range(19):
    r = randint(1, 10)
    print(r, end=' ')
    if previous == r:
        repeat = True
    previous = r
print()
if repeat:
    print('The same number appeared twice in a row.')
else:
    print('There were no numbers that appeared twice in a row.')



#13 Get 10 numbers between 0 and 100, print out smallest number entered between 50 and 100
smallest = 100
for i in range(10):
    num = eval(input('Enter a number between 0 and 100: '))
    if 50 < num < 100:
        if num < smallest:
            smallest = num
if smallest == 100:
    print('No numbers between 50 and 100 were entered.')
else:
    print('Smallest between 50 and 100:', smallest)




#14 Get 10 numbers from user, print out two smallest
a = eval(input('Enter a number:'))
b = eval(input('Enter a number:'))
if a < b:
    small1 = a
    small2 = b
else:
    small1 = b
    small2 = a
for i in range(8):
    a = eval(input('Enter a number:'))
    if small1 < a < small2:
        small2 = a
    elif a < small1:
        small2 = small1
        small1 = a
print('Two smallest:', small1, small2)



#15 Generate sequence a_n = 2a_{n-1}+a_{n-2}, a_0=a_1=1
n = eval(input('Enter n: '))
a = 1
b = 1
print(b, a, end=' ')
for i in range(n-2):
    hold = a
    a = 2*a + b
    b = hold
    print(a, end=' ')
print()




#16 Generate sequence that starts w/ 1, 2, 3 and each term is average of three previous
n = eval(input('Enter n: '))
a = 3
b = 2
c = 1
print(b, c, a, end=' ')
for i in range(n-2):
    hold = a
    a = (a + b + c) / 3
    c = b
    b = hold
    print(a, end=' ')
print()
    
