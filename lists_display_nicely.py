#15 Given some lists, display them nicely with birthdays formatted with leading zeroes if single digits, and add commas to the salaries.

Names = ['Alice', 'Bob', 'Caroline']
Birthdays = ['2/7/86', '11/12/66', '8/17/72']
Salaries = [72000, 144300, 43200]

for i in range(len(Names)):
    day, month, year = Birthdays[i].split('/')
    day = int(day)
    month = int(month)
    print('{:10s}  {:02d}/{:02d}/{:2s}  {:,d}'.format(Names[i], day, month, year, int(Salaries[i])))