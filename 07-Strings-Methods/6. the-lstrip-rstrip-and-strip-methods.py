#6. strip methods:

sentence = '        ganesh        '
print(sentence.lstrip()) #lstrip removes empty spaces from left side of string
print(sentence.rstrip()) #rstrip removes empty spaces from right side of string
print(sentence.strip()) #strip removes empty spaces from both sides of string

print('         ga    nesh      '.lstrip()) #however the spaces between the strings are uneffected
print('         ga    nesh      '.rstrip())
print('         ga    nesh      '.strip())

print()
#we can also remove particular characters from left, right or from both sides of string.
website = 'www.python.org'
print(website.lstrip('w'))
print(website.rstrip('org'))
print(website.strip('.worg'))

print('www.compu in ter.in'.strip('.win')) #however the characters between strings are uneffected