# A program that gets the sum of all multiples of 3 or 5 below 1000

# Initialize a variable to store the sum
sum_of_multiples = 0

# Initialize a variable for the current number
number = 1

while number <= 1000:
    if number % 3 == 0 or number % 5 == 0:
        # Add multiples to the sum
        sum_of_multiples += number

    # Increment the number for the next iteration
    number += 1

print(f"The sum of multiples of 3 and 5 below 1000: {sum_of_multiples}")
