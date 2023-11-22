#for loop example using odd_even case scenerio

start = int(input("enter the first number in the range"))
end = int(input("enter the last number in the range"))

for number in range(start,end):
       #to check even numbers on that range
 
    if  number % 2 == 0:
        print("your number is even")
    elif number % 2!= 0:
        print("your number is odd")
    else:
        print("enter a valid number")

              

