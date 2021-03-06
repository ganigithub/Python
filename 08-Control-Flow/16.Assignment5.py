# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number. 
# For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kind of loops. 
# Instead, utilize recursion. Your function MUST call itself.

def factorial(number):
    if number <= 1:
        return number

    return number * factorial(number-1)

print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(3))