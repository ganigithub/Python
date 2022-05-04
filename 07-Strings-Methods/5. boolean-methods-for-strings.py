#5. Boolean methods = islower, isupper, istitle :Ture OR False

print('hello'.islower()) #True if all letters are in lowercase
print('hello 12#$'.islower()) # 12#$ are not alphabets and python ignores them
print('Hello'.islower())

print()
print('HELLO'.isupper()) #True if all letters are in uppercase
print('HeLLO'.isupper())

print()
print('Once Upon A Time'.istitle()) #Ture if every letter of word is uppercase
print('Once upon A time'.istitle())

print()
print('Gani'.isalpha()) #True if all characters in string are alphabets
print('Gani23'.isalpha()) 
print('Gani la'.isalpha()) #even if there is empty space, False will be given

print()
print('98299'.isnumeric()) #True if all characters are  numeric
print('98ABC'.isnumeric()) 
print('98 98'.isnumeric()) #empty space gives False

print()
print('Area51'.isalnum()) #True if characters are alphanumeric
print('Area 51'.isalnum()) # even empty space will give False
print('Area51!@'.isalnum()) #!@ are not alphanumric

print()
print(' '.isspace()) #True if all characters are empty space
print('    '.isspace())  #no matter how many spaces are there its True
print(''.isspace()) #false as there is no space
print(' 3 '.isspace())  #False if even one character other than space is present
print(' @#$ '.isspace())