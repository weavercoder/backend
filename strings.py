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