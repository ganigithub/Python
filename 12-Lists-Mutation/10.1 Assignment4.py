# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it

def delete_all(strings, target):
    result = []
    for idx, string in enumerate(strings):
        if string == target:
            continue
        else:
            result.append(string)
    return result

print(delete_all([1,3,5], 3))
print(delete_all([1,2,2], 2))
print(delete_all([1,2,3], 1))
print(delete_all([4,4,4], 4))

# another efficient way to do above code is

def delete_all(strings, target):
    while target in strings:
        strings.remove(target)
    return strings
print(delete_all([1,3,5], 3))
print(delete_all([4,4,4], 4))


print()
# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list

def push_or_pop(numbers):
    result = []
    for number in numbers:
        if number > 5:
            result.append(number)
        elif number <= 5:
            result.pop()
    return result

print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))