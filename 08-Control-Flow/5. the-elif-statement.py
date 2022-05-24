# #5 elif statement: statements that runs after 'if statement'

def positive_or_negative(value):
    if value > 0:
        return 'Positive'
    elif value < 0:         #we can do this by usign 'if statement' but elif is preferred 
        return 'negative'
    elif value == 0:        #we can add as many as elif statements we want. Thats an advantage
        return 'Neither'
print(positive_or_negative(4))
print(positive_or_negative(-2))
print(positive_or_negative(0))

def calculator(operation, a, b):
    if operation == 'add':
        return a+b
    elif operation == 'subt':
        return a-b
    elif operation == 'mult':
        return a*b
    elif operation == 'div':
        return a/b
    else:
        return 'invalid operation'

print(calculator('add', 2, 8))
print(calculator('subt', 8, 2))
print(calculator('mult', 8, 2))
print(calculator('div', 8, 2))
print(calculator('floorDiv', 2, 3))