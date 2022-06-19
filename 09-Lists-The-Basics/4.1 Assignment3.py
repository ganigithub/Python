# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)

def split_in_two(number, object):
    if number%2==0: return object[2:]
    return object[:2]

print(split_in_two(2, object = ['hi', 'bye', 'why', 'who']))
print(split_in_two(3, object = ['hi', 'bye', 'why', 'who']))
print(split_in_two(2, object = ['a', 'b', 'c', 'd', 'e', 'f']))
print(split_in_two(3, object = ['a', 'b', 'c', 'd', 'e', 'f']))