text = input('enter text : ')
leters = {}
for i in text:
    if i.isalpha():
        if i in leters:
            leters[i] = leters[i] + 1
        else:
            leters[i] = 1
print(leters)