def generate_fibonacci(n):
    fibonacci_sequence=[0,1]

    for i in range(2,n):
        next_term=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence
nth_term= eval(input('Enter your number:    '))
    
result=generate_fibonacci(nth_term)

print('The fibonacci sequence for',nth_term,'is',result)