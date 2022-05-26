#7 and keyword: used to give more than one condition or if statements:

if 5<10 and 'garry' == 'garry':
    print('both conditions are true')

if 5>10 and 'garry' == 'garry':  #here 1st condition is false, so python ignores 2nd condition it is
    print('one condition is false so it will not print') #called Short Circuit evaluation

if 'garry' == 'garry' and 4>3 and 5==5: #we can add as many conditions as we want
    print('more than two conditions can be applied using and keyword')

value = 100
# if value > 50 and < 200: #both conditions should be correct independently
if 50 < value and value < 200:                #OR   if 50 < value < 200:         
    print('thats true')