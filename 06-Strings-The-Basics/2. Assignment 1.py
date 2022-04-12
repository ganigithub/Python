# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True

def long_word(text):
    return len(text) > 7

print(long_word('Python'))
print(long_word('wonderful'))


# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False

def first_longer_than_second(first_text, second_text):
    return len(first_text) > len(second_text)

print(first_longer_than_second('python', 'ruby'))
print(first_longer_than_second('cat', 'mouse'))
print(first_longer_than_second('hi', 'hi'))