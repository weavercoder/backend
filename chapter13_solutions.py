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
