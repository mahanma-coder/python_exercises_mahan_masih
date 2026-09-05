s1=input('enter sentence 1 : ')
s2=input('enter sentence 2 : ')
w1=s1.split()
w2=s2.split()
c=[]
for i in w1:
    for j in w2:
        if i==j and i not in c:
            c.append(i)
print('Common words:')
for i in c:
    print(i)            