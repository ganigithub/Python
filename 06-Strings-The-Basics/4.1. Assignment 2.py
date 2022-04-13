# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters

def same_first_and_last_letter(text):
    return text[0] == text[-1]
print(same_first_and_last_letter('python'))
print(same_first_and_last_letter('Runner'))
print(same_first_and_last_letter('runner'))
print(same_first_and_last_letter('A'))

# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.

def three_number_sum(text):
    return int(text[0]) + int(text[1]) + int(text[2])
print(three_number_sum('123'))
print(three_number_sum('234'))
print(three_number_sum('000'))
print(three_number_sum('999'))