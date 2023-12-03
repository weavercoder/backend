#1 printing a triangle
print('*')
print('**')
print('***')
print('****')



#2 printing the letter A
print('    *')
print('   * *')
print('  *****')
print(' *     *')
print('*       *')



#3 printing a computation
print((14*12) / (33*144 - 187))



#4 km to miles
distance = eval(input('Enter a distance in km: '))
print('That is', distance*.621371, 'miles.')



#5 name three times
name = input('Enter your name: ')
print(name, name, name)



#6 add two numbers
num1 = eval(input('Enter a number: '))
num2 = eval(input('Enter another number: '))
print('The sum is: ', num1 + num2)



#7 BMI
w = eval(input('Enter weight: '))
h = eval(input('Enter height: '))
print('The BMI is: ', 703*w/(h*h))



#8 5 numbers separated by 3 spaces
n1 = eval(input('Enter first number: '))
n2 = eval(input('Enter second number: '))
n3 = eval(input('Enter third number: '))
n4 = eval(input('Enter fourth number: '))
n5 = eval(input('Enter fifth number: '))
print(n1, n2, n3, n4, n5, sep='   ')



#9 variables
c = eval(input('Enter a number: '))
c = c + 2
print(c)

#1 print word 25 times
word = input('Enter a word: ')
for i in range(25):
    print(word)

#2 print word 200 times on same line
word = input('Enter a word: ')
for i in range(200):
    print(word, end=' ')
print()


#3 print 5,6,7,8,9,...,89,90
for i in range(5,91):
    print(i, end=' ')
print()

#4 print 2,6,10,14,18,...,98,102
for i in range(2,103,4):
    print(i, end=' ')
print()

#5 print 29,28,27,26,25,...5,4
for i in range(29,3,-1):
    print(i, end=' ')
print()

#6 print 1. A 2. A ... 5. A
for i in range(1,6):
    print(i, '. A', sep='')

#7 perfect squares
for i in range(1,21):
    print(i*i, end=' ')
print()    


#8 40 A's, then 50 B's
for i in range(40):
    print('A', end='')
for i in range(50):
    print('B', end='')
print()    

#9 ABC 100 times
for i in range(100):
    print('ABC', end='')
print()    


#10  AAAAAAAAAABCDBCDBCDBCDBCDEFFFFFFFFFFFFFFF
for i in range(10):
    print('A', end='')
for i in range(5):
    print('BCD', end='')
print('E')
for i in range(15):
    print('F', end='')
print()


#11 user says how many A's to print
num = eval(input('How many As to print? '))
for i in range(num):
    print('A', end='')
print()        


#12 user enters 10 numbers, print squares of them
for i in range(10):
    num = eval(input('Enter a number: '))
    print('Its square is', num*num)


#13 print box
height = eval(input('Enter height: '))
for i in range(height):
    print('**********')


#14 print big C
size = eval(input('Enter size: '))
for i in range(size):
    print('*', end='')
print()    
for i in range(size-2):
    print('*')
for i in range(size):
    print('*', end='')
print()    

    
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
    
#1 Create string: Didn't Hamlet say "To be or not to be"?
s = 'Didn\'t Hamlet say "To be or not to be"?'
print(s)


#2 Multiline string
s = """A
B
\\
C\tD"""
print(s)



#3 Long multipart problem
s = input('Enter a string of at least 6 characters: ')
print('(a) Length:', len(s))
print('(b) 2nd char:', s[1])
print('(c) Last char', s[-1])
print('(d) First 5 chars:', s[:5])
print('(e) Last 2 chars:', s[-2:])
print('(f) Backwards:', s[::-1])
print('(g) All chars except last:', s[:-1])
print('(h) All chars except first and last:', s[1:-1])
if 'a' in s:
    print('(i) There is a lowercase a.')
else:
    print('(i) No lowercase a.')
print('(j) All caps:', s.upper())
print('(k) Replace spaces with underscores:', s.replace(' ', '_'))



#4 Ask for two strings, repeat first 10 times, concatenate the two
s = input('Enter a string: ')
t = input('Enter another string: ')

print('Repeated 10 times:', s*10)
print('Concatenation:', s+t)



#5 Float or integer?
s = input('Enter a number: ')
if '.' in s:
    print('That\'s a floating point number.')
else:
    print('That\'s an integer.')


#6 Ask for programming language, recognize "Python" regardless of capitalization
s = input('Enter a programming language: ')
if s.lower() == 'python':
    print('You selected the Python programming language.')

#7 Check for punctuation and print out a message or the count of spaces
s = input('Enter a string: ')
if '.' in s or ',' in s or ';' in s:
    print('There is some punctuation.')
else:
    print('Number of spaces:', s.count(' '))

#8 Get sentence, remove spaces, convert to uppercase
s = input('Enter a sentence: ')
s = s.replace(' ', '')
s = s.upper()
print(s)

#9 Get string, replace spaces with *, replace every 5th char with !, take three copies
s = input('Enter a string: ')
s = s.replace(' ', '*')
t = ''
for i in range(len(s)):
    if i % 5 == 0:
        t += '!'
    else:
        t += s[i]
t = t*3
print(t)

#10 User enters string.  If at least 5 chars, take first 5 and 3 asterisks, else add exclamation points
s = input('Enter a string: ')
if len(s) >= 5:
    t = s[:5] + '***'
else:
    t = s + '!' * (5-len(s))
print(t)

#11 User enters string.  Loop through and print out each letter followed by a space.
s = input('Enter a string: ')
for c in s:
    print(c, end=' ')
print()

#12 User enters string.  Create new string containing each letter followed by a space.
s = input('Enter a string: ')
t = ''
for c in s:
    t += c + ' '
print(t)


#13 User enters string.  Say if there are more As or Bs.
s = input('Enter a string: ')
if s.count('A') > s.count('B'):
    print('More As than Bs.')
elif s.count('A') < s.count('B'):
    print('More Bs than As.')
else:
    print('Same number of As and Bs.')

#14 Count how many letters are in a string
s = input('Enter a string: ')    
count = 0
for c in s:
    if c.isalpha():
        count += 1
print('Number of letters:', count)

#15 Determine if there are more capitals or lowercases in a string
s = input('Enter a string: ')
count_lower = 0
count_upper = 0
for c in s:
    if c in 'abcdefghijklmnopqrstuvwxyz':
        count_lower += 1
    elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        count_upper += 1
if count_lower < count_upper:
    print('More uppercase letters.')
elif count_lower > count_upper:
    print('More lowercase letters.')
else:
    print('Same number of lowercase as uppercase.')

#16 Print out all the lowercase letters not in a string
s = input('Enter a string of lowercase letters: ')
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in s:
        print(c, end='')
print()        

#17 Determine if a string contains any characters not in another
s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
flag = False
for c in s1:
    if c not in s2:
        flag = True
if flag:
    print('First string has some characters that are not in the second.')
else:
    print('Every character of first string is also in the second.')
  

#18 Determine if strings differ in exactly one position
s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')

if len(s1) != len(s2):
    print('Strings are of different lengths.')
else:
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    if count == 1:
        print('They differ in exactly one position.')
    else:
        print('They don\'t differ in exactly one position.')


#19 Print 10 random lowercase letters
from random import randint

s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(10):
    print(s[randint(0, len(s)-1)], end='')
print()

#20 Create a random string of 10 characters from a user's string
from random import randint

s = input('Enter a string: ')
t = ''
for i in range(10):
    t += s[randint(0, len(s)-1)]
print(t)

#21 Given string of lowercase letters, print out first occurence of each letter and message if letter is missing
s = input('Enter a string of lowercase letters: ')
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in s:
        print(c, 'is not in the string')
    else:
        print(c, 'first occurs at index', s.index(c))
        
   
#22 Breaking up an email address
s = input('Enter a email address: ')
breakpoint = s.index('@')
print('User name:', s[:breakpoint])
print('Domain name:', s[breakpoint+1:])

#23 Addressing a person
name = input('Name: ')
gender = input('Gender: ')
formality = input('Formal/Informal: ')

breakpoint = name.index(' ')
first = name[:breakpoint]
last = name[breakpoint+1:]

if formality.lower() == 'formal':
    if gender.lower() == 'male':
        print('Hello, Mr. ', last, '.', sep='')
    else:
        print('Hello, Ms. ', last, '.', sep='')
else:
    print('Hello, ', first, '.', sep='')

#24 Print first letter of each word in a sentence.
s = input('Enter a sentence: ')
print(s[0], end='')
for i in range(len(s)):
    if s[i] == ' ':
        print(s[i+1], end='')
print()


#25 Print out the locations of all the letters in a string.
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i].isalpha():
        print(i, end=' ')
print()


#26 String changing from all As to all Bs.
n = eval(input('Enter n: '))
for i in range(n+1):
    print('A'*(n-i) + 'B'*i)

#27 Determine whether an IP address is of form 10.*.*.* or 192.168.*.*
s = input('Enter an IP address: ')
if s.startswith('192.168.') or s.startswith('10.'):
    print('Address is local.')
else:
    print('Address is not of the two special types.')

#28 Replace each character of user's name with the letter after it
alpha = 'abcdefghijklmnopqrstuvwxyz'
name = input('Enter your name in lowercase: ')
new_name = ''
for c in name:
    location = alpha.index(c)
    new_name += alpha[(location+1) % 26]
print(new_name)
    
#1 Long problem
L = eval(input('Enter a list of at least 5 items: '))
print('(a) Number of items:', len(L))
print('(b) Fourth item:', L[3])
print('(c) Last 3 items:', L[-3:])
print('(d) Everything but first 2 items:', L[2:])
print('(e) Reversed:', L[::-1])
print('(f) Largest:', max(L), '  Smallest:', min(L))
print('(g) Sum:', sum(L))
if 0 in L:
    print('(h) First zero is at:', L.index(0))
else:
    print('(h) No zeroes in the list.')
L.sort()
print('(i) Now sorted:', L)
del L[0]
print('(j) After deleting first item:', L)
L[-2] = 9876
print('(k) After changing second-to-last item:', L)
L.append(-500)
print('(l) After appending -500 to list:', L)



#2 Create list of 100 zeroes
L = [0] * 100
print(L)



#3 Copying lists
#(a)
L = [1, 2, 3, 4, 5]
copy = L
L[0] = 9
print('(a) copy=', copy)

#(b)
L = [1, 2, 3, 4, 5]
copy = L[:]
L[0] = 9
print('(a) copy=', copy)



#4 Create list of square roots of the integers from 1 to 100, rounded to 4 decimal places.
from math import sqrt

L = []
for i in range(1, 101):
    L.append(round(sqrt(i), 4))
print(L)



#5 Generate a list of 10 random numbers from 1 to 20.
from random import randint

L = []
for i in range(10):
    L.append(randint(1, 20))
print(L)



#6 Generate list of 20 random 0s and 1s, print out how many zeros.
from random import randint

L = []
for i in range(20):
    L.append(randint(0, 1))
print(L)
print('Number of zeroes:', L.count(0))



#7 Count number of evens in a user's list.
L = eval(input('Enter a list: '))
count = 0
for x in L:
    if x % 2 == 0:
        count += 1
print('Number of evens:', count)



#8 Given a list, create a new list containing only the entries greater than 50.
L = eval(input('Enter a list: '))
M = []
for x in L:
    if x > 50:
        M.append(x)
print(M)



#9 Given a list, find the smallest thing and the first index at which it occurs.
L = eval(input('Enter a list: '))
best = 0
for i in range(len(L)):
    if L[i] < L[best]:
        best = i
print('Smallest item is', L[best], 'first occuring at index', best)



#10 Given a list with some items greater than 10, print out smallest thing larger than 10.
L = eval(input('Enter a list with some items greater than 10: '))

smallest = max(L)
for x in L:
    if 10 < x < smallest:
        smallest = x
print('Smallest thing greater than 10:', smallest)



#11 Given a list, replace evens with zeroes and odds with two ones.
L = eval(input('Enter a list: '))
M = []
for i in range(len(L)):
    if L[i] % 2 == 0:
        M.append(0)
    else:
        M.append(1)
        M.append(1)
L = M
print('Modified list:', L)



#12 Given list, print out average, three smallest things, average when dropping smallest
L = eval(input('Enter a list:'))
print('(a) Average:', sum(L)/len(L))
L.sort()
print('(b) Three smallest:', L[:3])
print('(c) Average, dropping smallest:', sum(L[1:])/len(L[1:]))




#13 Given month number, print out the month name

#a Tedious way
month = eval(input('Enter a month number: '))
if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
elif month == 4:
    print('April')
elif month == 5:
    print('May')
elif month == 6:
    print('June')
elif month == 7:
    print('July')
elif month == 8:
    print('August')
elif month == 9:
    print('September')
elif month == 10:
    print('October')
elif month == 11:
    print('November')
elif month == 12:
    print('December')

#b List way
Months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
month = eval(input('Enter a month number: '))
print(Months[month-1])



#14 Create list [1,2,2,3,3,3,4,4,4,4,...,10,10,10,10,10,10,10,10,10,10]
L = []
for i in range(1, 11):
    L += [i]*i
print(L)




#15 Given two lists, create a list by going element-by-element and taking the larger one from the two lists.
L = eval(input('Enter first list: '))
M = eval(input('Enter second list (same size as first): '))
N = []
for i in range(len(L)):
    if L[i] > M[i]:
        N.append(L[i])
    else:
        N.append(M[i])
print(N)



#16 Given list, create a list of cumulative sums from it
L = eval(input('Enter a list: '))
Sums = []
for i in range(len(L)):
    Sums.append(sum(L[:i+1]))
print(Sums)



#17 List of triangular numbers
n = eval(input('How many triangular numbers do you want? '))
L = []
total = 0
for i in range(1,n):
    total += i
    L.append(total)
print(L)



#18 Riffle shuffle two lists
L = eval(input('Enter a list: '))
M = eval(input('Enter another list (same size as first): '))
N = []
for i in range(len(L)):
    N.append(L[i])
    N.append(M[i])
print(N)



#19 Rotate items in a list left.
L = eval(input('Enter a list: '))
save = L[0]
for i in range(len(L)-1):
    L[i] = L[i+1]
L[-1] = save
print(L)



#20 Create random list of 0s, 1s, and 2s, then create a new list of indices that repeats occur.
from random import randint

L = []
for i in range(20):
    L.append(randint(0, 2))
print(L)

Repeats = []
for i in range(1, len(L)-1):
    if L[i] == L[i-1]:
        Repeats.append(i)
print(Repeats)




#21 Given list, create new list containing first 5 things in reverse order and rest as they were.
L = eval(input('Enter a list of at least five items: '))
M = L[:5][::-1] + L[5:]
print(M)



#22 Given string of lowercase letters, create a list of how many times each letter occurs.
s = input('Enter a string of lowercase letters: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = []
for c in alphabet:
    L.append(s.count(c))
print(L)



#23 Random grader with all grades from 90 to 100 except one random 0.
from random import randint

n = eval(input('How many students? '))
L = []
for i in range(n):
    L.append(randint(90, 100))
lucky_index = randint(0,n-1)
L[lucky_index] = 0
print(L)



#24 Generate 100 random numbers from 1 to 50, then change first two 50s to -999
from random import randint

L = []
for i in range(100):
    L.append(randint(1, 50))
print(L)

count = 0
for i in range(len(L)):
    if L[i] == 50 and count < 2:
        L[i] = -999
        count += 1
if count == 0:
    print('There were no 50s.')
else:
    print('New list:', L)



#25 Estimate probabilty of a large straight in Yahtzee
from random import randint

count = 0
for i in range(10000):
    L = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    L.sort()
    if L == [1,2,3,4,5] or L == [2,3,4,5,6]:
        count += 1
print(100*count/10000)



#26 Given list, shuffle it according to a particular algorithm
from random import randint

L = eval(input('Enter a list: '))
for i in range(len(L)-1):
    j = randint(1, len(L))
    L[i], L[j] = L[j], L[i]
print(L)




#27 Given list of strings and list of indices create a new list of all the strings from the list that are not at those indices.
L = eval(input('Enter a list of strings: '))
I = eval(input('Enter a list of indices: '))
M = []
for i in range(len(L)):
    if i not in I:
        M.append(L[i])
print(M)
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
#1 Dictionary given in problem, then do several things.
d = {'abc':7, 'def':11, 'ghi':13, 'jkl':17, 'mno':19}

#a Print value associated with key 'def'.
print(d['def'])

#b Use keys() method.
print(list(d.keys()))

#c Loop over the dictionary.
for k in d:
    print(k, d[k])

#d Check if 'pqr' is a key.
if 'prq' in d:
    print('Yes')
else:
    print('No')

#e Change value associated with 'abc' to 23, print values.
d['abc'] = 23
print(list(d.values()))



#2 Dictionary of elements in periodic table
d = {'H' : 'Hydrogen',
     'He' : 'Helium',
     'Li' : 'Lithium',
     'Be' : 'Beryllium',
     'B' : 'Boron',
     'C' : 'Carbon',
     'N' : 'Nitrogen',
     'F' : 'Fluorine',
     'Ne' : 'Neon'}
s = input('Enter element symbol: ')
print('It\'s name is:', d[s])



#3 Create dictionary of conversions, use it to do conversions.
d = {'cm':2.54, 'm':.0254, 'ft':1/12, 'yd':1/36}
x = eval(input('Enter distance in inches: '))
u = input('Enter unit to convert to (abbreviation): ')
print(d[u]*x)



#4 Dictionary from user entered words, where keys are how many vowels in that word.
d = {}
s = 'a'
while s != '':
    s = input('Enter a word: ')
    d[s] = sum(s.count(c) for c in 'aeiou')
print(d)



#5 Use a loop to creae a dictionary of letters and their ASCII codes
d = {}
s = 'abcdefghiklmnopqrstuvwxyz'
for c in s + s.upper():
    d[c] = ord(c)
print(d)



#6 Create a dictionary of character frequencies in a user's word.
s = input('Enter a word: ')
d = {}
for c in s:
    if c not in d:
        d[c] = s.count(c)
print(d)



#7 Use maps like in the previous problem to tell if two diffferent words contain the same characters with the same frequencies.
s1 = input('Enter word 1: ')
s2 = input('Enter word 2: ')
d1 = {}
d2 = {}
for c in s1:
    if c not in d1:
        d1[c] = s1.count(c)
for c in s2:
    if c not in d2:
        d2[c] = s2.count(c)
same = True
for c in s1:
    if c not in d2 or d1[c] != d2[c]:
        same = False

if same:
    print('Same characters with same frequencies.')
else:
    print('Something is different.')



#8 Determine if a date is valid.
d = {'january':31, 'february':29, 'narch':31, 'april':30,
     'may':31, 'june':30, 'july':31, 'august':30,
     'september':30, 'october':31, 'november':30, 'december':31}
s = input('Enter a date: ')
L = s.split()
month = L[0].lower()
day = int(L[1])
if not (1 <= day <= d[month]):
    print('Invalid date.')
else:
    print('Seems okay.')



#9 Ask for names and lists of courses that person took.  Create a dictionary from it and use it to print out all the people who took a specific course.
d = {}
for i in range(5):
    s = input('Enter name: ')
    L = eval(input('Enter list of course numbers: '))
    d[s] = L

course = eval(input('Enter course: '))
for p in d:
    if course in d[p]:
        print(p)



#10 Create quiz using a dictionary whose keys are questions and whose values are their answers.
from random import shuffle

d = {'What is the capital of Lithuania?': 'Vilnius',
     'What number in the periodic table is Gold?': '79',
     'What is the Latin name of the genus of oak trees?': 'Quercus',
     'What does m stand for in Newton\'s second law equation F=ma?' : 'mass',
     'What does A stand for in RAM memory? ': 'access'}

keys = list(d.keys())
shuffle(keys)

for k in keys:
    guess = input(k + ' ')
    if guess.lower() == d[k].lower():
        print('Right!')
    else:
        print('Wrong.')



#11 Sparse array
d = {}        
for i in range(3):
    x = eval(input('Enter index: '))
    y = eval(input('Enter value: '))
    d[x] = y

x = eval(input('Enter index to check: '))
if x in d:
    print(d[x])
else:
    print(0)



#12 substitution cipher
from random import shuffle
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = list(alphabet)
shuffle(L)
key = ''.join(L)
encrypt = {}
decrypt = {}
for i in range(len(alphabet)):
    encrypt[alphabet[i]] = key[i]
    decrypt[key[i]] = alphabet[i]

    
print('Key:', key)

s = input('Enter a lowercase word: ')
t = ''
for c in s:
    t += encrypt[c]
print('Encrypted:', t)

u = ''
for c in t:
    u += decrypt[c]
print('Decrypted:', u)
#1 Read expenses.txt and print out all the expenses over $2000.
lines = [line.strip() for line in open('expenses.txt')]
for item in lines:
    if int(item) > 2000:
        print(item, end=' ')
print()



#2 Read expenses.txt, add 10% tax to each and write to a new file.
output_file = open('new_expenses.txt', 'w')
lines = [line.strip() for line in open('expenses.txt')]
for item in lines:
    print('{:.2f}'.format(int(item)*1.1), file=output_file)
print()



#3 Read secret_message.txt and print out the first letter of each line.
lines = [line.strip() for line in open('secret_message.txt')]
s = ''
for item in lines:
    s += item[0]
print(s)



#4 Use wordlist.txt to do a few things
words = [line.strip() for line in open('wordlist.txt')]

#a words that contain "quo".
for word in words:
    if 'quot' in word:
        print(word, end=' ')
print()

#b Percentage of words the contain all the vowels.
count = 0
for word in words:
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        count += 1
print(count/len(words)*100)

#c Average word length
total = 0
for word in words:
    total += len(word)
print(total/len(words))

#d All words >= 6 letters that start and end with same three letters.
for word in words:
    if len(word) >= 6 and word[:3] == word[-3:]:
        print(word, end=' ')
print()        

#e Longest word that starts and ends with the same letter.
longest = 'a'
for word in words:
    if word[0] == word[-1] and len(word) > len(longest):
        longest = word
print(longest)

#f All words that contain four alphabetically consecutive letters.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for word in words:
    for i in range(23):
        if alphabet[i:i+3] in word:
            print(word, end=' ')
            break
print()


#5 Read from wordlist.txt and create a new file of all the words that are 5 letters or less
output_file = open('new_wordlist.txt', 'w')
lines = [line.strip() for line in open('wordlist.txt')]
for line in lines:
    if len(line) <= 5:
        print(line, file=output_file)
output_file.close()



#6 Given files of first and last names, create 10 random names.
from random import choice
first = [line.strip() for line in open('first_names.txt')]
last = [line.strip() for line in open('last_names.txt')]

for i in range(10):
    print(choice(first), choice(last))



#7 Given population.txt that has country names and populations, print all countries whose names start with G and have at least 500,000 people.
lines = [line.strip() for line in open('population.txt')]
for line in lines:
    L = line.split('\t')
    country = L[0]
    population = int(L[1])
    if country[0] == 'G' and population >= 500000:
        print(country, population)



#8 Grade paragraphs from ~studentParagraphs.txt~ based on length.
text = open('studentParagraphs.txt').read()
L = text.split('\n\n')
for x in L:
    name, paragraph = x.split(': ')
    if len(paragraph) >= 200:
        grade = 'A'
    elif len(paragraph) >= 150:
        grade = 'B'
    elif len(paragraph) >= 100:
        grade = 'C'
    elif len(paragraph) >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(name, grade)
    
    

#9 Read elements.txt and reformat, writing to a new file.
output_file = open('new_elements.txt', 'w')
lines = [line.strip() for line in open('elements.txt')]
for line in lines:
    L = line.split(' - ')
    print(L[1], L[0], sep=',', file=output_file)
output_file.close()

    

#10 Given a file baseball.txt of baseball stats, print out all the players that hit at least 20 homeruns with an average of at least .300.
lines = [line.strip() for line in open('baseball.txt')]
for line in lines:
    L = line.split('\t')
    name = L[0]
    team = L[1]
    home_runs = L[8]
    average = L[14]
    if int(home_runs) >= 20 and float(average) >= .300:
        print(name, team, home_runs, average)



#11 Read from high_temperatures.txt, reformat, and rewrite to new file.
output_file = open('new_high_temperatures.txt', 'w')
lines = [line.strip() for line in open('high_temperatures.txt')]
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
for line in lines:
    L = line.split()
    month, day = [x for x in L[0].split('/')]
    temp = round(5/9*(int(L[1])-32), 0)
    print(month_names[int(month)-1] + ' ' + day + ' ' + str(temp), file=output_file)
output_file.close()



#12 Read countries.txt and create a list of lists of all the A countries, B countries, etc.
lines = [line.strip() for line in open('countries.txt')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = [[] for i in range(26)]
for line in lines:
    L[alphabet.index(line[0].lower())].append(line)
print(L)



#13 Use wordlist.txt to find all the words that can be made from a user's string
words = [line.strip() for line in open('wordlist.txt')]
s = input('Enter a string of lowercase letters: ')
d = {} # dictionary of frequencies in user's word
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
for word in words:
    e = {} # dictionary of frequencies in current word
    for c in word:
        if c in e:
            e[c] += 1
        else:
            e[c] = 1
    okay = True
    for c in e:
        if c not in d or e[c] > d[c]:
            okay = False
    if okay:
        print(word, end=' ')
print()



#14 Use countries.txt, ask for country name and a number, find country that is n lines before given country, wrapping around if needed.
lines = [line.strip() for line in open('countries.txt')]
country = input('Enter a country name: ')
country = country.lower().capitalize()
if country not in lines:
    print('That name is not in the list.')
else:    
    n = eval(input('Enter a number: '))
    print('N countries before:', lines[(lines.index(country)-n)%len(lines)])



#15 Using football_teams.txt and basketball_teams.txt, find NFL team nickname where if you remove a single letter, you get a basketball team nickname.    
football = [line.strip() for line in open('football_teams.txt')]
basketball = [line.strip() for line in open('basketball_teams.txt')]

for team in football:
    for i in range(len(team)):
        if team[:i] + team[i+1:] in basketball:
            print(team, team[:i] + team[i+1:])



#16 Create word frequency dictionary for romeoandjuliet.txt.
text = open('romeoandjuliet.txt').read()
for c in '!@#$%^&*()+=[{]}|\\;:",<>.?/':
    text = text.replace(c, '')
text = text.replace('\n', ' ')    
text = text.lower()
d = {}
for word in text.split():
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(sorted(list(d.items()), key=lambda x:-x[1])[:10])



#17 Guess-a-number with a save-game feature.
from random import randint

restart = input('Restart a game (r) or start from scratch (s)? ')
if restart == 'r':
    text = open('guess_a_number.txt').read()
    right, wrong = [int(x) for x in text.split()]
else:
    right = wrong = 0
keep_going = True
while keep_going:
    r = randint(1, 5)
    guess = eval(input('Enter your guess: '))
    if guess == r:
        print('Right!')
        right += 1
    else:
        print('Wrong.')
        wrong += 1
    print('You have gotten', right, 'right, and', wrong, 'wrong.')
    response = input('Keep going? (y/n): ')
    if response == 'n':
        keep_going = False
        output_file = open('guess_a_number.txt', 'w')
        print(right, wrong, file=output_file)
        output_file.close()



#18 continents.txt has country names arranged by continent.  Use it to write a quiz giving a country and asking what continent it is on.
from random import choice

lines = [line.strip() for line in open('continents.txt')]
current_continent = ''
d = {}
for line in lines:
    if len(line) > 0 and line == line.upper():  # Continent names are in upper case
        current_continent = line
    elif len(line) > 0: # not a blank line
        d[line] = current_continent

country = choice(list(d.keys()))
ans = input('What continent is ' + country + ' on? ')
if ans.upper() == d[country]:
    print('Right!')
else:
    print('Wrong.  Answer is', d[country])



#19 Read multiple_choice.txt and reorder the answer choices of each question.
from random import shuffle

alphabet = 'abcdefghijklmnopqrstuvwxyz'
output_file = open('new_multiple_choice.txt', 'w')
lines = [line.strip() for line in open('multiple_choice.txt')]
for line in lines:
    if len(line) > 0 and line[0].isdigit():
        print(line, file=output_file)
        choices = []
    elif len(line) > 0 and line[0] == '(':
        choices.append(line[4:]) # only include answer, not letter
    else: # blank line signals question is done
        shuffle(choices)
        for i in range(len(choices)):
            print('(' + alphabet[i] + ')', choices[i], file=output_file)
        print(file=output_file) # blank line
# These three lines are for the last question, since there won't be a blank line at the end of the file to signal that a question is done.
shuffle(choices)
for i in range(len(choices)):
    print('(' + alphabet[i] + ')', choices[i], file=output_file)
output_file.close()



#20 Read high_temperatures.txt and find the 30-day period over which there is the biggest increase in high temperature.
lines = [line.strip() for line in open('high_temperatures.txt')]

largest = 0
values = []
for i in range(len(lines)):
    date, temp = lines[i].split(' ')
    date30, temp30 = lines[(i-30)%365].split(' ')
    diff = int(temp) - int(temp30)
    if  diff > largest:
        largest = diff
        values = [date30 + ' to ' + date + '   ' + temp30 + '-' + temp]
    elif diff == largest:
        values.append(date30 + ' to ' + date + '   ' + temp30 + '-' + temp)

for x in values:
    print(x)
    


#21 Ask user to enter two NFL team names, read nfl1978-2013.csv, and print out all the games where either one of the two teams shut out the other.
lines = [line.strip() for line in open('nfl1978-2013.csv')]
t1 = input('Enter team 1 (full name required): ').lower()
t2 = input('Enter team 2 (full name required): ').lower()
for line in lines[1:]:
    date, team1, score1, team2, score2 = line.split(',')
    if ((team1.lower() == t1 and team2.lower() == t2) or\
        (team2.lower() == t1 and team1.lower() == t2)) and\
       (int(score1) == 0 or int(score2) == 0):
        print(line)



#22 Read the file nfl_scores.txt and print out all the scores that have never happened.
lines = [line.strip() for line in open('nfl_scores.txt')]
d = {}
for line in lines[1:]:
    L = line.split(',')
    winning_score = int(L[2])
    losing_score = int(L[3])
    if winning_score in d:
        d[winning_score].append(losing_score)
    elif winning_score < 20: 
        d[winning_score] = [losing_score]
for i in range(20):
    if i not in d and i != 1:
        for j in range(i+1):
            print(i, j, sep='-', end=', ')
for x in d:
    for y in range(x+1):
        if y not in d[x] and  y != 1:
            print(x, y, sep='-', end=', ')
print()
#1 triangular --- Takes an integer n and returns n(n+1)/2.
def triangular(n):
    return n*(n+1)//2

print(triangular(5))



#2 get_bill_total --- Takes a bill amount and sales tax percentage and returns new total.
def get_bill_total(amount, tax):
    return round(amount * (1+tax/100), 2)

print(get_bill_total(43.25, 6))



#3 distance --- Uses the distance formula to return distance.
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x2**2-x1**2)+(y2**2-y1**2))

print(distance(2, 3, 5, 8))



#4 print_blank_lines --- Takes an integer and prints that many blank lines.
def print_blank_lines(n):
    for i in range(n):
        print('\n'*(n-1))

print_blank_lines(4)



#5 print_perfect_squares --- Takes an integer and prints perfect squares from 1 to that integer.
def print_perfect_squares(n):
    for i in range(1, n+1):
        print(i*i)

print_perfect_squares(5)



#6 add_up_range --- adds up all the numbers in a range
def add_up_range(start, end, step):
    total = 0
    for i in range(start, end, step):
        total += i
    return total

print(add_up_range(3, 10, 2))



#7 phi --- Returns Euler phi function (how many numbers are relatively prime to a number)
from fractions import gcd

def phi(n):
    count = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            count += 1
    return count

print(phi(12), phi(13))




#8 Easter --- Returns the date of Easter in any year.
def easter(Y):
    C = Y // 100
    m = (15 + C - C//4 - (8*C+13)//25) % 30
    n = (4 + C - C//4) % 7
    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = (19*c+m) % 30
    e = (2*a+4*b+6*d+n) % 7

    if d==29 and e==6:
        return 'April 19'
    elif d==28 and e==6 and m in [2,5,10,13,16,21,34,39]:
        return 'April 18'
    elif 22+d+e <= 31:
        return 'March ' + str(22+d+e)
    else:
        return 'April ' + str(d+e-9)

print(easter(2018))



#9 is_upper() --- Returns if a string of letters is all uppercase.
def is_upper(s):
    return s == s.upper()

print(is_upper('ABC'), is_upper('ABc'))



#10 rand_lower_string() --- Returns a random string of lowercase letters
from random import choice

def rand_lower_string(n):
    return ''.join(choice('abcdefghijklmnopqrstuvwxyz')
                   for i in range(n))
        
print(rand_lower_string(10))



#11 contains_a_letter --- Returns whether a string contains any letters.
def contains_a_letter(s):
    for c in s:
        if c.isalpha():
            return True
    return False

print(contains_a_letter('12abc'), contains_a_letter('#341&&'))



#12 simplify_text --- converts a string to lowercase and removes all common punctuation except hyphens and apostrophes.
def simplify_text(s):
    for c in '!@#$%^&*()+=[{]}|\\;:",<>.?/':
        s = s.replace(c, '')
    return s.lower()

print(simplify_text('This is a test. (Or is it?)'))



#13 convert_time --- Converts Martian time from 25-hour time to a bizarre system.
def convert_time(t):
    h, m = t.split(':')
    h = int(h)
    x = str(h%5 + 1)
    y = 'ABCDE'[h//5]
    return x + y + ':' + m

print(convert_time('3:30'), convert_time('19:45'))



#14 next_name() --- Names are A, B, ... Z, AA, AB, ..., ZZ, AAA, AAB.  Given a name, this returns the next name in the sequence.
def next_name(name):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = len(name) - 1
    while i >= 0:
        if name[i] != 'Z':
            return name[:i] + alphabet[alphabet.index(name[i])+1] + 'A'*(len(name)-(i+1))
        i -= 1
    return 'A' * (len(name)+1)

print(next_name('ABC'), next_name('ABZ'), next_name('ABZZ'), next_name('ZZZ'))



#15 reverse_only_letters --- Takes a string and reverses the letters, but no other characters.
def reverse_only_letters(s):
    reverse_letters = [c for c in s[::-1] if c.isalpha()]
    t = ''
    i = 0
    for c in s:
        if c.isalpha():
            t += reverse_letters[i]
            i += 1
        else:
            t += c
    return t

print(reverse_only_letters('ab#c&&de!f?'))



#16 average --- Return average of a list of integers.
def average(L):
    return sum(L) / len(L)

print(average([10, 20, 30, 40, 50]))



#17 mid_range --- Given list, return average of its min and max.
def mid_range(L):
    return (max(L) + min(L)) / 2

print(mid_range([10, 15, 20, 40, 60]))



#18 closest --- Given list of integers and an integer n, find thing in list closest to n, returning smaller one in case of a tie.
def closest(L, n):
    best = L[0]
    for x in L:
        if abs(x-n) < abs(best-n) or (abs(x-n) == abs(best-n) and x < best):
            best = x
    return best

print(closest([1, 2, 11, 6, 9], 4))



#19 changes_by_one --- Given list of integers, return a list of all indices where values change by +1.
def changes_by_one(L):
    return [i for i in range(1, len(L)) if L[i] == L[i-1]+1]

print(changes_by_one([1, 2, 4, 8, 9, 10, 15, 20, 21]))



#20 string_sort --- Sorts a string of lowercase letters, returning a string
def string_sort(s):
    L = list(s)
    L.sort()
    return ''.join(L)

print(string_sort('thisisatest'))



#21 telephone_match --- Determines if a string matches a telephone number using the letters typically associated with numbers in phone numbers.
def telephone_match(s, num):
    d = {'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3',
         'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5',
         'M':'6', 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':7,
         'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':9}
    t = ''
    for c in s.upper():
        t += d[c]
    return t == num.replace('-', '')

print(telephone_match('INTEGER', '468-3437'), telephone_match('INTEGER', '456-7821'))



#22 integer_lengths --- Given list of integers, return the sum of their lengths.
def integer_lengths(L):
    return sum(len(str(x)) for x in L)

print(integer_lengths([2, 14, 126, 11, 4096]))



#23 union --- Union together two lists, making sure there are no repeats.
def union(L, M):
    U = []
    for x in L:
        if x not in U:
            U.append(x)
    for x in M:
        if x not in U:
            U.append(x)
    return U

print(union([1,1,2,3,8], [2,3,3,6,10]))



#24 teams --- groups a list of names into teams of two
from random import shuffle

def teams(L):
    M = L[:] # make a copy so we don't change the caller's list
    shuffle(L)
    for i in range(0, len(L), 2):
        print('Team ', i//2, ': ', L[i], ', ', L[i+1], sep='')

teams(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])



#25 triple_shuffle --- Takes three lists and shuffles them concurrently
from random import shuffle

def triple_shuffle(L, M, N):
    I = list(range(len(L)))
    shuffle(I)
    for i in range(len(I)):
        L[i], L[I[i]] = L[I[i]], L[i]
        M[i], M[I[i]] = M[I[i]], M[i]
        N[i], N[I[i]] = N[I[i]], N[i]

A = [1,2,3,4,5]
B = [11,22,33,44,55]
C = [9,8,7,6,5]
triple_shuffle(A, B, C)
print(A, B, C)



#26 print_2d --- Print a 2d list nicely.
def print_2d(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            print(L[i][j], end=' ')
        print()

L = [[1,2,3], [4,5,6], [7,8,9]]
print_2d(L)



#27 random_2d_list --- Returns a 2d list of a given size with random numbers from a given range.
from random import randint

def random_2d_list(m, n, x, y):
    return [[randint(x, y) for j in range(n)] for i in range(m)]

print_2d(random_2d_list(3, 5, 10, 20))



#28 number_of_lines --- Given a filename, return how many lines are in hat file.
def number_of_lines(filename):
    return len([line for line in open(filename)])

print(number_of_lines('wordlist.txt'))



#29 find_words --- Given a string of consonants, return all words that have those consonants and only them in that order, excluding vowels.
def find_words(s):
    words = [line.strip() for line in open('wordlist.txt')]
    L = []
    for word in words:
        t = word
        for v in 'aeiou':
            t = t.replace(v, '')
        if t == s:
            L.append(word)
    return L

print(find_words('bt'))



#30 words_in_word --- Given a string, return all groups of contiguous letters in that word that are real words.
def words_in_word(s):
    words = [line.strip() for line in open('wordlist.txt')]
    L = []
    for word in words:
        if word in s:
            L.append(word)
    return L

print(words_in_word('restaurant'))
#1 BankAccount
class BankAccount:
    def __init__(self, name, amount, interest_rate):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.amount *= (1 + self.interest_rate / 100)

account = BankAccount('Juan De Hattatime', 1000, 3)
account.apply_interest()
print(account.amount)
account.interest_rate = 2
account.apply_interest()
print(account.amount)



#2 Item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '{:s}, {:.2f}'.format(self.name, self.price)

item = Item('hat', 12.40)
print(item)



#3 ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove_items(self, name):
        self.items = [item for item in self.items if item.name != name]
        
    def __str__(self):
        return '\n'.join(str(item) for item in self.items)
        
cart = ShoppingCart()
cart.add(Item('shirt', 18.99))
cart.add(Item('shirt', 22.59))
cart.add(Item('car', 22400))
cart.add(Item('lettuce', 1.49))
print(cart)
cart.remove_items('shirt')
print(cart)



#4 RestaurantCheck
class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number, server_name):
        self.check_number = check_number
        self.sales_tax_percent = sales_tax_percent
        self.subtotal = subtotal
        self.table_number = table_number
        self.server_name = server_name

    def calculate_total(self):
        return self.subtotal * (1+self.sales_tax_percent/100)

    def print_check(self):
        output_file = open('check' + str(self.check_number) + '.txt', 'w')
        print('Check Number:', self.check_number, file=output_file)
        print('Sales tax: ', self.sales_tax_percent, '%', sep='', file=output_file)
        print('Subtotal: {:.2f}'.format(self.subtotal), file=output_file)
        print('Total: {:.2f}'.format(self.calculate_total()), file=output_file)
        print('Table Number:', self.table_number, file=output_file)
        print('Server:', self.server_name, file=output_file)
        output_file.close()

check = RestaurantCheck(443, 6, 23.14, 'Sonic the Hedgehog', 17)
check.print_check()



#5 Ticket
class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time

    def __str__(self):
        return 'Ticket(' + str(self.cost) + ', ' + str(self.time) + ')'

    def is_evening_time(self):
        hour = int(self.time.split(':')[0])
        return 18 <= hour <= 23

    def bulk_discount(self, n):
        if 5 <= n < 9:
            return 10
        elif n >= 10:
            return 20
        else:
            return 0

ticket = Ticket(49.99, '19:00')
print(ticket)
print(ticket.is_evening_time())
print(ticket.bulk_discount(15))



#6 MovieTicket
class MovieTicket(Ticket):
    def __init__(self, cost, time, movie_name):
        self.cost = cost
        self.time = time
        self.movie_name = movie_name

    def __str__(self):
        return 'Ticket(' + str(self.cost) + ', ' + str(self.time) + ', ' + str(self.movie_name) + ')'

    def afternoon_discount(self):
        hour = int(self.time.split(':')[0])
        if 12 <= hour <= 17:
            return 10
        else:
            return 0
        
m_ticket = MovieTicket(49.99, '14:25', 'Snakes on a Plane')
print(m_ticket)
print(m_ticket.afternoon_discount())
print(m_ticket.is_evening_time())



#7 Course
class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.student_IDs = []

    def is_full(self):
        return len(self.student_IDs) >= self.capacity
    
    def add_student(self, x):
        if not self.is_full() and x not in self.student_IDs:        
            self.student_IDs.append(x)

course = Course('CompSci', 3)
course.add_student('123')
course.add_student('123')
course.add_student('456')
course.add_student('789')
course.add_student('9999')
print(course.is_full())
print(course.student_IDs)



#8 Avatar
from random import randint, sample
from time import sleep

class Avatar:
    def __init__(self, name, hit_points, attack_power, defense_power):
        self.name = name
        self.hit_points = hit_points
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self):
        return randint(1, self.attack_power)

    def defend(self, attack_amount):
        damage = max(attack_amount - self.defense_power, 0)
        self.hit_points -= damage
        return damage

    def is_alive(self):
        return self.hit_points > 0

L = [Avatar('Ogre', 40, 30, 3),
     Avatar('Warrior', 100, 20, 5),
     Avatar('Paladin', 80, 10, 8)]

while len(L) > 1:
    attacker, defender = sample(L, 2)
    attack_amount = attacker.attack()
    damage = defender.defend(attack_amount)
    print(attacker.name, 'attacks!')
    print(defender.name, 'takes', damage, 'damage.')
    if not defender.is_alive():
        print(defender.name, 'is defeated.')
        L.remove(defender)
    for x in L:
        print(x.name, '---', x.hit_points)
    print()
    sleep(.5)



#9 Fighter and Mage
from random import randint

class Fighter(Avatar):
    def special_power(self):
        if randint(1, 5) == 1:
            return 2*self.attack_power
        else:
            return 0

class Mage(Avatar):
    def special_power(self):
        self.hit_points += 10

fighter = Fighter('Fighter', 100, 40, 5)
mage = Mage('Mage', 100, 40, 5)
attacker = fighter
defender = mage

while fighter.is_alive() and mage.is_alive():
    decision = input(attacker.name + ' -- attack (1) or special power (2): ')
    if decision == '2' and attacker == fighter:
        attack_amount = fighter.special_power()
        if attack_amount == 0:
            print('Failed.')
        else:
            damage = defender.defend(attack_amount)
            print(attacker.name, 'attacks!')
            print(defender.name, 'takes', damage, 'damage.')
    elif decision == '2' and attacker == mage:
        attacker.special_power()
        print(attacker.name, 'adds 10 hit points.')
    else:
        attack_amount = attacker.attack()
        damage = defender.defend(attack_amount)
        print(attacker.name, 'attacks!')
        print(defender.name, 'takes', damage, 'damage.')

    if not defender.is_alive():
        print(defender.name, 'has been defeated.')
    else:
        print(fighter.name, ' --- ', fighter.hit_points)
        print(mage.name, ' --- ', mage.hit_points)
        print()
    if attacker == fighter:
        attacker = mage
        defender = fighter
    else:
        attacker = fighter
        defender = mage
    


#10 Timer
import time

class Timer:
    def start(self):
        self.initial_time = time.time()
        
    def elapsed_seconds(self):
        return time.time() - self.initial_time
    
    def formatted_time(self, seconds):
        seconds = int(round(seconds, 0))
        minutes = seconds // 60
        seconds = seconds % 60
        return '{:d}:{:02d}'.format(minutes, seconds)

timer = Timer()
timer.start()
input('Enter something: ')
print(timer.elapsed_seconds())
timer2 = Timer()
timer2.start()
input('Enter something else: ')
print(timer2.elapsed_seconds())
print(timer.formatted_time(timer.elapsed_seconds()))



#11 Calendar
class Calendar:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        return self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)

    def first_day(self, m):
        p = (14-m) // 12
        q = self.year - p
        r = q + q//4 - q//100 + q//400
        s = m + 12*p - 2
        t = (1 + r + (31*s)//12) % 7
        return t

    def print_calendar(self, m):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and m == 2:
            days = 29
        else:
            days = month_days[m-1]

        c = 0
        for i in range(self.first_day(m)):
            c += 1
            print('    ', end='')
            
        for i in range(1, days+1):
            print('{:4d}'.format(i), end='')
            c += 1
            if c % 7 == 0:
                print()
        print()

calendar = Calendar(2018)
print(calendar.is_leap_year())
print(calendar.first_day(2))
calendar.print_calendar(2)

