o=int(input('tell hour 0 to 23:'))
if 6>o>=0:
    print('midnight')
elif 12>o>=6:
    print('morning')
elif 18>o>=12:
    print('noon')
elif 23>o>=18:
    print('night')
else:
    print('are you sure you entered correct time?')