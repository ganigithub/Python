#4. Return Funcion

def add(a, b):
    print( a + b )
result = add(3, 4)
print(result)   # this line will give 'none' as returnvalue, coz a
# function cannot be assigned to a name.

#To do that we use return function 

def add(a, b):
    return a + b  # paranthesis is not necessary
    print('addition of two no is', result) #this line will be ignored
    #coz, return function concludes the body & nothing runs after it.

result = add(3, 4)
print(result)

def modulus(a, b):
    return a // b
result = modulus(658, 7)
print('the quotient is', result)