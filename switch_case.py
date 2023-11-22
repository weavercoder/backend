#switch_case function
#a function is  like a first citzen class

def odd_even(number):
    if number == 0:
        return "even"
    else:
        return "odd"
    
  
num = float(input("enter the number "))
result = odd_even(num)
print(f"The number is {result}")
  

