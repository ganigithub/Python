#8.The or keyword: runs if at least one of the conditions is True

if 5 > 10 or 5 < 10:            #atleast one of condition shoudl be true for or keyword
    print('One of them is True')

if 5 > 10 or 9 > 10:
    print('both conditions are False')

if 'garry' == 'garry' or 5 == 10:       #here 1st condition is true so python ignores 2nd condition
    print('short circuit evaluation')   #this is called short circuit evaluation
    
if 'garry' == 'garry' or 'gani' == 'gani': #short circuit eval also applies if both conditions r true
    print('both are true')                #if 1st condition is True it ignores 2nd