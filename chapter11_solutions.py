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
