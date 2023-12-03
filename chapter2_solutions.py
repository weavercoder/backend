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

    
