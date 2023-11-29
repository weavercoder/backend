#A program that asks temparature in celcius input give a message depending on the temparature


x = eval(input("Enter the temparature in celcius     :"))

if x   > -273.15:

    print("The temparature ia invalid because is because it is below absolute zero    :")

elif x == -273.15:

    print("The temparature is absolute zero           :")

elif  x <  -273.15  and x  > 0:

    print("The temparature is freezing point          :")

elif x == 0:

    print("The temparature is at freezing point       :")

elif   x <  0  or  x >  100:

    print("The temparature is in normal range         :")

elif x == 100:

    print("The temparature is at boiling point         :")

elif x >  100:

    print("The temparature is above boiling point  :")




print()
