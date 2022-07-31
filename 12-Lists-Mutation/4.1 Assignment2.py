# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.

def only_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(only_evens([1,2,3,4,5,6,12,80,13]))
print(only_evens([13,45,23,7]))
print(only_evens([]))

# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.

def long_strings(strings):
    result = []
    for string in strings:
        if len(string) >= 5:
            result.append(string)
    return result
print(long_strings(['garry', 'gani', 'abcdef', 'hi', 'laptop']))
print(long_strings(['cat' , 'dog', 'odd']))
print(long_strings([]))