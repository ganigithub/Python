#give index position of each character in a string in a form of list using list comprehesion
alphabets = 'abcdefghijklmnopqrstuvwxyz'
new = []
for char in 'garry':
    chars = alphabets.index(char)
    new.append(chars)
print(new)

# #another way to do this is:

print(['abcdefghijklmnopqrstuvwxyz'.index(char) for char in 'garry'])

# #give a list of each number divided by 2 in range 0 to 20:
print([number / 2 for number in range(20)])

print()
creams = [
    'vanilla cream',
    'chocolate cream',
    'apple',
    'orange'
]

#give a list of strings having cream in it
print([flavor for flavor in creams if 'cream' in flavor])

#give a list of strings not having cream in it
print([flavor for flavor in creams if 'cream' not in flavor])

#give a list of lengths of strings not having cream in it
print([len(flavor) for flavor in creams if 'cream' not in flavor])

#give a list of strings having cream in it minus the word cream
print([flavor.split(' ')[0] for flavor in creams if 'cream' in flavor])