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