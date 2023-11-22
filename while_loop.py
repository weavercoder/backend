
#A program that gets sum of all multiples of  3 or 5 below 1000

#initialize a variable to store the sum
sum_of_multiples = 0

#initialize a variable for the current number
number = 1

while number <= 1000:
    
    if number % 3  == 0 or  number % 5  == 0:
    
    #Add multiples to the sum
        sum_of_multiples += number

#increament of  the number for the next alteration
number += 1


print(f"the sum of multiples of 3 and 5 below 1000: {sum_of_multiples}")


    
    
