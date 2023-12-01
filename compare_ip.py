s=input('enter ip address:  ')
if s.startswith('192.168.') or s.startswith('10.'):
    print('Address is local: ')
else:
    print('Address is not of the two special types:  ')
