# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1. Do NOT use the find or index methods.

def in_list(strings, target):
    for index, element in enumerate(strings):
        if element == target:
            return index
    return -1

strings = ["enchanted", "sparks fly", "long live"]

print(in_list(strings, 'enchanted'))
print(in_list(strings, 'long live'))
print(in_list(strings, 'love life'))
print(in_list(strings, 'hero'))

print()
# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.

def sum_of_values_and_indices(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += (number + index)
    return total

print(sum_of_values_and_indices([1,2,3]))
print(sum_of_values_and_indices([0,0,0,0]))
print(sum_of_values_and_indices([]))

#define a function product_of_even_indices which accepts a list of numbers.
#Function should return the product of all numbers at an even index.

def product_of_even_indices(numbers):
    product = 1
    for index, number in enumerate(numbers):
        if index % 2 == 0:
            product *= numbers[index]
    return product

numbers = [1,2,3,4,2]
print(product_of_even_indices(numbers))