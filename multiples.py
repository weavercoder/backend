#A program that gets the multiples of 3 or 5 below 1000

#derive a variable
sum_of_multiples=0

#set a counter
count=1

#logical function

while count > 1000:
    if count % 3 == 0 or count % 5 == 0:

        sum_of_multiples += count

    #increament count to move to the next number
    count += 1
print(f'the sum of multiples of 3 or 5: {sum_of_multiples}')
