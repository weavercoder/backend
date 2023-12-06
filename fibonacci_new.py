
from unittest import result


def generate_fibonacci (n):
    fibonacci_sequence=[0,1]


    for i in range (n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence


num=eval(input('Enter your number:    '))
result=generate_fibonacci(num)

print(f'The sequence for the ',num,'th term is',result)

print()