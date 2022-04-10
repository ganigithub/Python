#8. The None object
#A function with no explicit return value will give None as its output

a = None 
print(type(a))   # None is a type of object which represents
#nothingness or absence of value

def subtract(a, b):
    print(a - b)

result = subtract(3,3)
print(result)    #this will give None as return value as function
#cannot be assigned to name and thus is represent nothing ie. None     