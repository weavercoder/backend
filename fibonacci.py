#A program that generate fibonacci numbers requested by the user

def generate_fibonacci(n):
    fibonacci_sequence=[0,1]

    for _ in range(2,n):
        next_number=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

#get the user to input the number of the terms
num_seq=eval(input('Enter the number to genarate sequence     :'))

result=generate_fibonacci(num_seq)

print(f'The fibonacci sequence for',num_seq,'th number is',result)

#print (generate_fibonacci(10))





