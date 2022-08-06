# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?

def factors(number):
    result = []
    for value in range(1, number+1):
        if number % value == 0:
            result.append(value)
    return result

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))

print()
# we can use while loop also

def factors(number):
    value = 1
    result = []
    while value <= number:
        if number % value == 0:
            result.append(value)
        value += 1
    return result

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))