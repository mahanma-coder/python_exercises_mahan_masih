c1=input('coler1 : ')
c2=input('coler2 : ')
c3=input('coler3 : ')
if c1==c2==c3:
    print('سه رنگ یکسان هستن')
elif c1==c2 or c1==c3 or c2==c3:
    print('دو رنگ یکسان هستند')
else:
    print('رنگ ها یکسان نیستند')