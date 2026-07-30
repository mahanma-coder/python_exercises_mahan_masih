a=float(input('enter the amount:'))
if a>1000000:
    d=a*15/100
    a=a-d
    print('payment:',a)
elif 1000000>a>500000:
    d=a*10/100
    a=a-d
    print('payment:',a)
else:
    print('payment:',a)