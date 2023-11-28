#1 Validate a course code in the form of some letters, a space, and then some numbers.  Numbers must be in range 100 to 499.
code = input('Enter course code: ')
num = int(code.split(' ')[1])
if num < 100 or num > 499:
    print('Invalid course code.')



#2 User enters numbers separated by semicolons, then add up numbers.
s = input('Enter some numbers separated by semicolons: ')
total = 0
for n in s.split(';'):
    total += int(n)
print(total)



#3 User enters a comma-separated number, print its square root.
from math import sqrt

num = input('Enter a number that has commas in it: ')
print(sqrt(float(num.replace(',', ''))))



#4 Create the list ['a1', 'b2', ..., 'z26']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = []
for i in range(26):
    L.append(alphabet[i] + str(i+1))
print(L)


#5 Replace all the numbers in a sentence with one more than their values.
s = input('Enter a sentence: ')
L = s.split()
M = []
for x in L:
    if x.isdigit():
        M.append(str(int(x)+1))
    elif x[:-1].isdigit():
        M.append(str(int(x[:-1])+1) + x[-1]) # handle punctuation after a number
    elif x[1:].isdigit():
        M.append(x[0] + str(int(x[1:])+1)) # handle punctuation before a number
    elif x[1:-1].isdigit():
        M.append(x[0] + str(int(x[1:-1])+1) + x[-1]) # handle punctuation on both sides of a number
    else:
        M.append(x)
print(' '.join(M))
print(L, M)


#6 Loop from 100 to 120, randomly rearrange the digits of each of them
from random import shuffle

for i in range(100, 121):
    L = list(str(i))
    shuffle(L)
    print(i, ''.join(L))



#7 Generate a random password with at least one capital, lowercase, digit, and special char.
from random import choice, shuffle

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
digits = '1234567890'
special = '!@#$%^&*()'
chars = lower + upper + digits + special

n = eval(input('How long do you want your password: '))
s = choice(lower) + choice(upper) + choice(digits) + choice(special)
for i in range(n - 4):
    s += choice(chars)
L = list(s)
shuffle(L)
print(''.join(L))



#8 Randomly choose 10 valid dates
#(a) Done by randomly choosing a month and then a day
from random import randint

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i in range(10):
    r = randint(0, 11)
    print(months[r], randint(1, days[r]))

#(b) Done by creating a list of all 365 days and using sample()
from random import sample

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

L = []
for i in range(12):
    for j in range(days[i]):
        L.append(months[i] + ' ' + str(j+1))
for s in sample(L, 10):
    print(s)



#9 Generate random multiplication problems and answers, then use them in a quiz.
from random import randint

Prob = []
Ans = []
for i in range(10):
    x = randint(2, 12)
    y = randint(2, 12)
    Prob.append(str(x) + ' x ' + str(y))
    Ans.append(x*y)

count = 0
for i in range(10):
    guess = eval(input(Prob[i] + '? '))
    if guess == Ans[i]:
        print('Right!')
        count += 1
    else:
        print('Wrong.  Answer is', str(Ans[i]) + '.')
print('You got', count, 'right.')



#10 Generate 20 random multiplication problems with numbers from 2 to 12, but no 10s
#(a) Using randint and a while loop to avoid 10
from random import randint

L = []
for i in range(20):
    x = randint(2, 12)
    while x == 10:
        x = randint(2, 12)
    y = randint(2, 12)
    while y == 10:
        y = randint(2, 12)
    L.append(str(x) + ' x ' + str(y))
print(L)

#(b) Using choice
from random import choice

P = [2,3,4,5,6,7,8,9,11,12]
L = [str(choice(P)) + ' x ' + str(choice(P)) for i in range(20)]
print(L)



#11 User enters day in month/day format, then print out if date is real.
Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = input('Enter a numerical date in month/day format: ')
L = s.split('/')
month = int(L[0])
day = int(L[1])
if not (1 <= month <= 12) or not (1 <= day <= Days[month-1]):
    print('Invalid date.')



#12 Convert degrees-minutes-seconds form to decimal form
s = input('Enter angle: ')
L = s.split('d')
degrees = int(L[0])
M = L[1].split("'")
minutes = int(M[0])
seconds = int(M[1])
print(degrees + minutes/60 + seconds/3600)



#13 Ask for list of product costs and print out costs w/ 6% tax added, right-justified and displayed to two decimal places.
L = eval(input('Enter a list of product costs: '))
for x in L:
    print('{:6.2f}'.format(x*1.06))



#14 Print out table of sines and cosines of angles from 0 to 360 by 30s, with angles right justified and sines and cosines shown to 4 decimal places.
from math import sin, cos, radians

for a in range(0, 361, 30):
    print('{:3d}    {:6.3f}   {:6.3f}'.format(a, sin(radians(a)), cos(radians(a))))



#15 Given some lists, display them nicely with birthdays formatted with leading zeroes if single digits, and add commas to the salaries.
Names = ['Alice', 'Bob', 'Caroline']
Birthdays = ['2/7/86', '11/12/66', '8/17/72']
Salaries = [72000, 144300, 43200]

for i in range(len(Names)):
    day, month, year = Birthdays[i].split('/')
    day = int(day)
    month = int(month)
    print('{:10s}  {:02d}/{:02d}/{:2s}  {:,d}'.format(Names[i], day, month, year, int(Salaries[i])))



#16 Use nested loops to print table from (1,1) to (9,9).
for i in range(9):
    for j in range(9):
        print('(', i, ',', j, ')', sep='', end=' ')
    print()



#17
#(a) Like previous, but don't display things above the diagonal.  
for i in range(9):
    for j in range(i+1):
        print('(', i, ',', j, ')', sep='', end=' ')
    print()

#(b) Like previous, but don't display things below the diagonal.  
for i in range(9):
    for j in range(i, 9):
        print('(', i, ',', j, ')', sep='', end=' ')
    print()



#18 Use nested loops to find all integer solutions to 37x+14y=11 for x and y between -100 and 100.
for x in range(-100, 101):
    for y in range(-100, 101):
        if 37*x+14*y == 11:
            print(x, y)



#19 Given a list of integers, print out first index of a repeat and stop.  Print out a message if there are no repeats.
L = eval(input('Enter a list of integers: '))
i = 1
while i < len(L) and L[i-1] != L[i]:
    i += 1
if i < len(L):
    print(i)
else:
    print('No repeats.')



#20 Ask user to enter a list and sort it according to a particular algorithm (selection sort).
L = eval(input('Enter a list of integers: '))
for i in range(len(L)-1):
    for j in range(i+1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
print(L)
