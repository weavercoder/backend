

#from unicodedata import digit

def sum_digit (num):
    
    return sum(int(digit)for digit in str(num))

result= sum_digit(2167789)


print(result)
