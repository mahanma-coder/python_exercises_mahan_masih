t = input('enter : ')
b=0
u=0
l=0
d=0
s=0
spe=0
for a in t:
    if a.isalpha():
        b+=1
    if a.isupper():
        u+=1
    if a.islower():
        l+=1
    if a.isdigit():
        d+=1
    if a==' ':
        s+=1
    if a in '!@#$%^&*':
        spe+=1
print('letters:',b)
print('up: ',u)
print('low : ',l)
print('num :',d)
print('space:',s)
print('speshial:',spe)
