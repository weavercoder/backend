while True:
    number = float(input("enter the number:-  "))
    if number % 2 == 0:
        print("you have entered an even number")
        break
    elif number % 2 !=0:
        print("You have entered an odd number:- ")
    else:
        print("Invalid input enter ane even number:- ")