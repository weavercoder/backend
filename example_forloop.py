#A program that sums the multiples of 3 or 5 below 1000

#derive a variable to store the sum
sum_of_multiples = 0

#logical 
for i in range(1000):
    if i % 3 == 0 or i or i % 5 == 0:
        sum_of_multiples += i
        i += 1

print(f"The sum of multiples of 3 or 5:{sum_of_multiples}")
