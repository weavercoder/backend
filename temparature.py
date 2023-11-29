#A program that asks temparature input and converts to either celcius/ferenheit

temp=eval(input('Enter temparature   : '))
unit=input('ferenheit or celcius    :')

if unit == 'celcius':  
     

     f_temp = 9/5 *temp +32
    
     print(f'the temparature in farenheit,{f_temp}')
 
elif unit == 'ferenheit':

     c_temp = 5/9 * temp - 32
     print(f'the temparature in celcius,{c_temp}')
else:
     print("Enter the correct details (ferenheit or celcius)      :")






 
   

    







