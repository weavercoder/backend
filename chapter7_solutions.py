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
