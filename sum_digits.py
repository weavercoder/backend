

#A function that is given an integer (num) returns the sum of (num)


def sum_digits(num):


#str(num):: converts the numerical value 'number' into its string repesentation
#for digit in str(number):iterates over each character in the string representation of the number
#int(digit)converts each character(digit) back into its integer repesentation(this is necessesary)
#because when you iterate over a string each character is treated as a string
#sum(....):add up all the integers obtained fro the previous step


    return  sum(int(digit) for digit in str(num))


result =sum_digits(123)
print(result)

   

   