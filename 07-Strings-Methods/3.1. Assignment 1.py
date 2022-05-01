# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.

def vowel_count(text):
    return text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
print(vowel_count('queueing'))
print(vowel_count('stop'))
print(vowel_count('garry'))

print()
# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string

def find_my_letter(text, a):
    return text.find(a)
print(find_my_letter('hello', 'l'))
print(find_my_letter('bazooka', 'o'))
print(find_my_letter('lollipop', 'z'))