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
    
