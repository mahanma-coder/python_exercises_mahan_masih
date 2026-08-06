x=input('enter text : ')
l=len(x)
if l%2==0:
    print(x[:l//2])
else:
    print(x[l//2:])