b=int(input('enter you card balance : '))
w=int(input('enter you withdraw : '))
p=b-w
if w<=0 :
    print('eror')
elif w<=b:
    print(p)
else: 
    print('insuffictient balance')
     