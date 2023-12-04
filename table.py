#16 Use nested loops to print table from (1,1) to (9,9).
for i in range(9):
    for j in range(9):
        print('(', i, ',', j, ')', sep='', end=' ')
    print()