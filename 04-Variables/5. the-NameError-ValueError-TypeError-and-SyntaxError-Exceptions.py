#6 Errors
# 1. Name error - occurs when some object is not defined
first_name = 'gani'
print(firstname) #here the 'firstname' is not defined 'first_name' is defined thats why error 

# 2. Type error = occurs when operation is applied to inappropriate types
 
print('hi' + 4) #string cannot be concatenated with integer. 
#in above line python thinks a string is to be concatenated because there
# is a string first and integer later. TypeError: str cannot concatenate with int
print(4 + 'hi')
#in above line python thinks a number is trying to add because there is
# an integer first and string later. TypeError: unsupported operand for int and str

# 3. Value error: right type but inappropriate value
int('xyz') # cannot convert a string 'xyz' into an integer hence valueError
int('33') # No error as string '33' can be converted into integer

# 4. Syntax Error: occurs when comma or bracket or inverted comma is missing or extra
print('hi)