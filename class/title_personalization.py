a=int(input('how old are you : '))
g=input('male or female : ')
if g =='male':
    if 40>=a>=1:
        print('boy')
    if 60>=a>40:
        print('dad')
    if a>60:
        print('grandpa')
    
if g == 'female':
    if 40>=a>=1:
        print('girl')
    if 60>=a>40:
        print('mom')
    if a>60:
        print('grandma')

    
