# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.

def divisible_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return True
    else:
        return False

    # return number % 3 == 0 and number % 4 == 0 (another way to write line 6,7,8,9)

print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(24))

# Declare a string_theory function that accepts a string as an argument. 
# It should return True if the string has more than 3 characters 
# and starts with a capital “S”. It should return False otherwise.

def string_theory(string):
    if len(string) > 3 and string[0] == 'S':
        return True
    else:
        return False
    # return len(string) > 3 and string[0] == 'S' (another way to write line 23-26)

print(string_theory('Same'))
print(string_theory('Semi'))
print(string_theory('sam'))
print(string_theory('Sam'))