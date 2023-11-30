#Days per month
days=eval(input('Enter number of days     : '))
if days == 28 or days == 29:
    print('Feb')
elif days== 30:
    print('April.jun,sep,Nov')
elif days == 31:
    print('Jan,Mar,May,Jul,Aug,Oct,Dec')
else:
    print('Error')

