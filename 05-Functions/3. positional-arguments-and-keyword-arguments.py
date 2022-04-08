# 3. positional and keyword arguments

def add(a, b):
    print('sum of',a , 'and', b, 'is', a+b)

add(3, 4)  # Positional arguments: position is important, here a =3, b = 4
add(a = 3, b = 4) # Keyword argument:name is assigned, position doenst matter
add(b = 4, a = 3)


def add(a, b, c):
    print('sum of three numbers is', a + b + c)

add(3, 5 ,2)
add(a = 3, b = 5, c = 2)
add(3, b = 5, c = 2) # here python automaticaly considers a = 3 this is 
# positional argument followed by keyword argument
add(3, 5, c = 2)

# keyword arguments should always come after positional arg as in line 16 & 18