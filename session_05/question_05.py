t = input('enter text : ')
l = t.split()
long = l[0]
for i in l :
    if len(i)>len(long):
        long = i
print(long,len(long))