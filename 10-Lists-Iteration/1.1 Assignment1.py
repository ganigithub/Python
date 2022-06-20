# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.

def sum_of_lengths(string):
    total = 0
    for string in string:
        total += len(string)
    return total

string = ['garry', 'gani']
print(sum_of_lengths(string))

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value

def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
numbers = [1,2,3,4,5]
print(product(numbers))