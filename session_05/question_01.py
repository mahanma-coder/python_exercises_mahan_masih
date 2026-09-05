p = input('enter your pass : ')
u = False
l = False
n = False
s = False
for i in p:
    if i.isupper():
        u=True
    if i.islower():
        l=True
    if i.isdigit():
        n=True
    if i in '!@#$%^&*':
        s=True
if len(p) < 8:
    print('Pass must contain at least 8 characters')
if u == False:
    print('Pass must contain an uppercase letter')
if l == False:
    print('Pass must contain a lowercase letter')
if n == False:
    print('Pass must contain a number')
if s == False:
    print('Pass must contain a special character')
if len(p)>=8 and u==True and l==True and n==True and n==True and s==True :
    print('pass is valid')
else:
    print('pass is invalid')