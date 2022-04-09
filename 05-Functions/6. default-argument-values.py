# 6 Default argument values

def add(a = 0, b = 0):  #by setting values of a & b to 0, we are
# giving a and b default values of 0.
    print (a+b)
add(3,3) #here a & b are 3 & 3 repectively
add(3)  #here a = 3, b is default value that was set in line 3 ie 0
add()    # here both a & b are default values ie 0


def name(text = 'garry'):  #default string here is 'garry'
    return(text)

print(name('gani'))
print(name())  #default string here is garry that we set in line 12


# def add(a=3, b): #this wll be error coz default arg must come after non default
#     print(a + b)
# add(8)