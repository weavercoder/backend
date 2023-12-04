
#A program to generate a fibonacci sequence for the nth term

def generate_sequence(n):
    fibonacci_sequence=[0,1]
    
    for _ in  range(2,n):
        next_term = fibonacci_sequence[-1] +fibonacci_sequence[-2]

        fibonacci_sequence.append(next_term)
    return fibonacci_sequence
    
new_term=eval(input('Enter the number: '))

result=generate_sequence(new_term)

print('The fibonacci sequence generated from',new_term,'th term is',result)
