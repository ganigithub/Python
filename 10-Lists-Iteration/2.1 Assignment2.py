# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
print(smallest_number([2,3,4,0,-1,5,5]))

print()
# Define a concatenate function that accepts a list of strings. 
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.

def concatenate(strings):
    final_string = ''
    for string in strings:
        if len(string)>2:
            final_string += string
    return final_string

print(concatenate(['garry', 'hi', 'gani', 'bye']))
print(concatenate(['abcd', 'ef', 'gh']))
print(concatenate(['ab', 'ef', 'gh']))

print()
# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.

def super_sum(strings):
    total = 0
    for string in strings:
        if 's' in string:
            total += string.index('s')         
    return total
    
print(super_sum(['sit', 'pasta', 'garry', 'movies']))
print(super_sum(['']))
print(super_sum(['mustache', 'almost','hi']))