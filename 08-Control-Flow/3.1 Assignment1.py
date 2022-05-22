# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.

def even_or_odd(a):
    if a % 2 == 0:
        return 'even'
        
    return 'odd'       #no need to right whole 'if statmnt' for a%2 != 0 coz if python reached this line
                       #that means above 'if statement' is false
print(even_or_odd(2))   
print(even_or_odd(5))

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______" 
# where the first space is the argument and the second space 
# is either 'truthy' or 'falsy'.

def truthy_or_falsy(value):
    if bool(value):
        return f'The value {value} is Truthy'

    return f'The value {value} is Falsy'
print(truthy_or_falsy(0))
print(truthy_or_falsy(3))
print(truthy_or_falsy('hi'))
print(truthy_or_falsy(''))