# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

def is_long(values):
    return len(values)>5

print(is_long(values = [1,1,3,5,1,1]))
print(is_long(values = [1,1,3]))
print(is_long(values = ['hi', 'bye', 9.88, True, False, 100]))