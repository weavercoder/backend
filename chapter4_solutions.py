#1 See if user entry is "Python"
ans = input('Enter a programming language: ')
if ans == 'python':
    print('This program was written in Python.')



#2 Square root if positive, else error message
from math import sqrt

num = eval(input('Enter a number: '))
if num < 0:
    print('You cannot enter a negative.')
else:
    print('Square root is', sqrt(num))



#3 Temperatures
temp = eval(input('Enter a temperature: '))
if temp <= 0:
    print('Warning: Low temperature.')
elif 0 < temp < 35:
    print('Temperature is okay.')
else:
    print('Warning: High temperature.')



#4 Days in a month
days = eval(input('Enter number of days: '))
if days == 28 or days == 29:
    print('Feb')
elif days == 30:
    print('Apr, Jun, Sep, Nov')
elif days == 31:
    print('Jan, Mar, May, Jul, Aug, Oct, Dec')
else:
    print('Error')



#5 Feet conversion
feet = eval(input('Enter a length in feet: '))
unit = input('Enter unit to convert to (inches, centimeters, or meters): ')
if unit == 'inches':
    print('In inches, that is', feet*12)
elif unit == 'centimeters':
    print('In centimeters, that is', feet*30.48)
elif unit == 'meters':
    print('In meters, that is', feet*.3048)
else:
    print('Not a valid unit.')



#6 Spanish numbers
num = eval(input('Enter a number from 20 through 99: '))
if 20 <= num < 30:
    print('veinte')
elif 30 <= num < 40:
    print('treinta')
elif 40 <= num < 50:
    print('cuarenta')
elif 50 <= num < 60:
    print('cincuenta')
elif 60 <= num < 70:
    print('sestenta')
elif 70 <= num < 80:
    print('setenta')
elif 80 <= num < 90:
    print('ochenta')
elif 90 <= num <= 99:
    print('noventa')
else:
    print('Number needs to be from 20 to 99.')



#7 Number not satisfying a variety of conditions
num = eval(input('Enter a number: '))
if not (num==0 or num==2 or num==5 or 10<num<15 or 20<num<25):
    print('Okay.')



#8 Divisibility by 7
num = eval(input('Enter a number: '))
if num % 7 == 0:
    print('It is divisible by 7.')
else:
    print('Not divisible by 7.')



#9 Numbers from 1 to 100 divisible by 3 or 7, but not both
for i in range(1, 101):
    if (i%3 == 0 or i%7==0) and not (i%3 == 0 and i%7 == 0):
        print(i, end=' ')
print()



#10 100 random question marks and asterisks
from random import randint
for i in range(100):
    r = randint(0,1)
    if r == 0:
        print('?', end='')
    else:
        print('*', end='')
print()



#11 100 random As, Bs, Cs, Ds, or Es
from random import randint
for i in range(100):
    r = randint(0,4)
    if r == 0:
        print('A', end='')
    elif r == 1:
        print('B', end='')
    elif r == 2:
        print('C', end='')
    elif r == 3:
        print('D', end='')
    else:
        print('E', end='')
print()



#12 100 random zeros and ones, zeroes twice as likely
from random import randint
for i in range(100):
    r = randint(0,2)
    if r == 2:
        print('1', end='')
    else:
        print('0', end='')
print()



#13 Billing program
start = eval(input('Enter starting hour (0-23): '))
end = eval(input('Enter ending hour (0-23): '))
if end >= start:
    print('Total: ', (end-start)*5.50)
else:
    print('Total: ', (24-start + end)*5.50)



#14 file0.jpg, file1.jpg, ... file199.jpg, nothing ending in 8
for i in range(200):
    if i % 8 != 0:
        print('file', i, '.jpg', sep='')



#15 Collatz sequences
x = eval(input('Enter a number: '))
print(x, end = ' ')
for i in range(30):
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3*x + 1
    print(x, end = ' ')
print()



#16 Trial and error math equation
for x in range(1,101):
    if 21*x**2 - x**3 + 21904 == 0:
        print(x)



#17 Multiplication game
from random import randint
for i in range(10):
    a = randint(20, 50)
    b = randint(20, 50)
    c = randint(20, 50)
    print(a, '+', b, '+', c, '= ?')
    ans = eval(input('Enter answer: '))
    if a+b+c == ans:
        print('Correct!')
    elif abs(a+b+c - ans) <= 5:
        print('Close!')
    else:
        print('Wrong.')
