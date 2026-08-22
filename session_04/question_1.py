import random
c = random.randint(1,123)
while True:
    u = int(input('یک عدد بگو از 1 تا 123 : '))
    if c<u:
        print('عددی که مد نظر ماست کوچیک تره')
    elif c>u:
        print('عددی که مد نظر ماست بزرگتره -_- ')
    else:
        print('ماشالا به هوشو زکاوتت ^_^')
        break