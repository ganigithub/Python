#9. not keyword : inverse or opposite of something

print(True)
print(not True)    #not will print opposite of True
print(False)
print(not False)

if 'g' in 'garry':
    print('yes')

if 'z' not in 'garry':   #here z isn't in garry which is false but not converts it to true and prints
    print('z is not in garry')

value = 100
if value < 200:
    print('Thats true')

if value > 200:
    print('Thats false')

#in above case we dont get output coz its false. But if we want to know the result anyways we can 
#use not keyword to print something

if not value > 200: 
    print('100 is not more than 200')
#to simply understand this, value > 200 -> False, not False -> True, so body runs