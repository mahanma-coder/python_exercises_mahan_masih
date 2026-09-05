t = input('enter text : ')
l = t.split()
w = ['hack','froud','scam','password','atack']
for i in w:
    n=0
    for j in l:
        if i==j:
            n+=1
    if n>0:
        print(i,'->',n)
        