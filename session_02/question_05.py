d=float(input('what is the distance?'))
if d<=2:
    r=20000
    print('Rent:',r)
else:
    r=((d-2)*5000)+20000
    print('Rent:',r)