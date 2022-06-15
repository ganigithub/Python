# Define a first_and_last function that accepts a list of strings. 
# The function should return a concatenation of the first element and the last element. 

def first_and_last(string_adder):
    return string_adder[0] + string_adder[-1]

print(first_and_last(string_adder = ['race', 'tyre', 'car']))
print(first_and_last(string_adder = ['a']))

# Define a product_of_even_indices function that accepts a list of numbers. 
# The list will always have 6 total elements. 
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4)

def product_of_even_indices(numbers):
    return numbers[0] * numbers[2] * numbers[4]

print(product_of_even_indices(numbers = [1,2,3,4,5,6]))
print(product_of_even_indices(numbers = [1,23,3,5,67,6]))
print(float(product_of_even_indices(numbers = [1,23,3,5,67,6])))

# Define a first_letter_of_last_string function that accepts a list of strings. 
# It should return one character — the first letter of the last string in the list. 
# Assume the list will always have at least one string.

def first_letter_of_last_string(strings):
    return strings[-1][0]

print(first_letter_of_last_string(strings = ['garry', 'gani', 'reeves']))
print(first_letter_of_last_string(strings = ['garry', 'gani']))