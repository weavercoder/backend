#A program that generates a fibonacci sequence of the nth term:input by the User

def generate_fibonacci (n):
    fibonacci_sequence=[0,1]

    for i in range(2,n):

        next_term=fibonacci_sequence[-1] +fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

n_term=eval(input('Enter your number:  '))
result=generate_fibonacci(n_term)
 
print=(f'The fibonacci sequence for',n_term,'th term is',result)
