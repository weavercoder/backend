while True:
    number = float(input("enter your number "))
    if number % 2 == 0:
        print("you have entered an even number")
        break
    elif number %2 !=0:
        print("you have entered an odd number:_")

    else:
        print("invalid input.Please enter a valid number")
