# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become 'C'
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in string:
        x = (alphabets.index(letter) + 2) % 26
        encrypted += alphabets[x]
    return encrypted

print(encrypt_message('abc'))
print(encrypt_message('def'))
print(encrypt_message('xyz'))

#the reason we used modulo operator in line 14 is we get the correct remainder index if index is
#going out of range.
#see explanation of Boris if line 14 is not understood