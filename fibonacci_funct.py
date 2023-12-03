#fibonacci_sequence
def generate_sequence(n):
    fibonacci_sequence=[0,1]

    for _ in range(2,n):
        next_term=fibonacci_sequence[-1] + fibonacci_sequence[-2]
    
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence
    
num=eval(input('enter the Number: '))
    
result=generate_sequence(num)

print('The fibonacci sequence for the ',num, 'th term is',result)

print()
          
