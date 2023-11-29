temp=eval(input('Enter temparature   : '))
unit=eval(input('ferenheit or celcius    :'))
f_temp = 9/5 *temp +32
c_temp = 5/9 * temp - 32

if unit == ('celcius'):

    f_temp = 9/5 *temp +32
    
    print(f'the temparature in farenheit,{f_temp}')

elif unit == ('ferenheit'):
    c_temp = 5/9 * temp - 32
    print(f'the temparature in celcius,{c_temp}')






 
   

    







