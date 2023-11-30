#convert celcius into farenheit

def convert(t):
    return t*9/5+32

temp=(eval(input('Enter temparature in celcius      :')))
        
result=convert(temp)

print('The conversion of',temp,'celcius is',result,'farenheit')




