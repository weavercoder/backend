#A program that asks temparature in celcius input give a message depending on the temparature


temp=input("Enter the temparature in celcius     :")

if temp  = > +-273.15:

    print("The temparature ia invalid because is because it is below absolute zero    :")

elif temp == -273.15:
    print("The temparature is absolute zero        :")

elif temp  = <  -273.15 and = <  0:

    print("The temparature is freezing point       :")

elif temp == 0:
    print("The temparature is at freezing point    :")

elif temp  < = 0 and  > = 100:
    print("The temparature is in normal range      :")

elif temp == 100:
    print("The temparature is at boiling point     :")

elif temp > = 100:
    print("The temparature is above boiling point  :")