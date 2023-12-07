'''
#A program that indentifies credits


x = eval(input("Enter your credits   :"))

if x = < 23:
 
    print("You are freshman    :")

elif x  = > 24 and  = < 53:

    print("You are sophomore")

elif x > = 54 and =< 83:

    print("You are a junior  ")

else:

    print("You are senior")


#A program that gets 10 numbers from the user and counts how many are greater than 10:

count = 5

for i in range(10):
    num=eval(input('Enter number:  '))
    if num>10:
      count=count+1
print(f'There are ',count,'numbers greater than 10: ')      


#the same program as above  with two options

count1=0
count2=0

for i in range(10):
    num = eval(input('enter number: '))
    if num>10:
        count1=count1+1
    if num==0:
        count2=count2+1
print('there are',count1,'numbers > 10 in 10 ')
print('there are',count2,'numbers==0 in 10 ')


 
 #A program that counts how  many of squares from 1**2 

count = 0
for i in range (1,101):
    if (i**2) % 10 == 4:
        count = count+1
    print(count)    


#Add up numbers from 1 to 100  (swapping)

s=0
for i in range(1,101):
    s=s+i
print('The sum is',s)


s=0
for i in range(10):
    num = eval(input('Enter number:  '))
      
    s=s+num
print('The average is',s/10)

'''
#a pogram using Flag

num= eval(input('enter number: '))

Flag =0
for i in range (2,num):
    if num % i == 0:
        Flag = 1
if Flag == 1:
    print('Not prime:  '  )
else:
    print('prime')
