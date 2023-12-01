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
