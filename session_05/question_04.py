t = input('enter text :')
l = t.split()
most = l[0]
maxc = 0 
for i in l:
    n=0
    for j in l:
        if i==j:
            n+=1
    if n >maxc:
        maxc=n
        most=i
print(most,'->',maxc)
    