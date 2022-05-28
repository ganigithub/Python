#10 nested if statements:

dish1 = 'maggi'
dish2 = 'rice'

if dish1 == 'maggi':
    if dish2 == 'rice':              #this will only run if line 6 is True                   
        print('make maggi and rice') 
    else:                            #this will only run if line 7 is False
        print('make just maggi')
else:                                #this will only run if line 6 is False
    print(F'make {dish2}')