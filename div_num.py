#9 Numbers from 1 to 100 divisible by 3 or 7, but not both
for i in range(1, 101):
    if (i%3 == 0 or i%7==0) and not (i%3 == 0 and i%7 == 0):
        print(i, end=' ')
print()