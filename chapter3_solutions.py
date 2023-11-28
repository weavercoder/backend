#1 x^y
x = eval(input('Enter x: '))
y = eval(input('Enter y: '))
print(x ** y)



#2 calculation
print((9 + 3) / (8 - 2))



#3 board game card reduction
num_cards = eval(input('How many cards do you have? '))
print('After reducing, you now have:', num_cards // 2)



#4 distance
x = eval(input('Enter one number: '))
y = eval(input('Enter another number: '))
print('Distance between them is', abs(x-y))



#5 rounded square root of a number
from math import sqrt

x = eval(input('Enter a positive number: '))
print('To 2 decimal place, its square root is', round(sqrt(x),2))



#6 rounded square roots of numbers from 1 to 20
from math import sqrt

for i in range(1,21):
    print(i, round(sqrt(i), 4))



#7 angle of a triangle
from math import degrees, atan2

x = eval(input('Enter width: '))
y = eval(input('Enter height: '))
print('Angle is:', round(degrees(atan2(y, x)), 1))



#8 hours into the future
hour = eval(input('What hour is it now? '))
delta = eval(input('How many hours into the future do you want to go? '))
print('New hour is', (hour + delta) % 24)



#9 inches to feet & inches
inches = eval(input('What is the height in inches? '))
print('That is', inches // 12, 'feet, and', inches % 12, 'inches.')



#10 add two random numbers
from random import randint

x = randint(1,10)
y = randint(1,10)
print('x =', x, 'y =', y, 'x+y =', x+y)



#11 100 numbers from 50 to 60 on the same line
from random import randint

for i in range(100):
    print(randint(50, 60), end=' ')
print()



#12 Print user-entered letter a random number of times
from random import randint

letter = input('Enter a letter: ')
num_times = randint(1, 10)
for i in range(num_times):
    print(letter)



#13 Print letter A a random number of times based on user input
from random import randint

num = eval(input('Enter a positive integer: '))
num_times = randint(num, num+10)
for i in range(num_times):
    print('A', end='')
print()



#14 50 lines of random zeros and ones, each line longer than previous
from random import randint

for i in range(10, 61):
    for j in range(i):
        print(randint(0,1), end='')
    print()



#15 Day of the week calculation
y = eval(input('Enter year: '))
m = eval(input('Enter month: '))
d = eval(input('Enter day: '))

p = (14-m) // 12
q = y - p
r = q + q//4 - q//100 + q//400
s = m + 12*p - 2
t = (d + r + (31*s)//12) % 7 

print(t)
