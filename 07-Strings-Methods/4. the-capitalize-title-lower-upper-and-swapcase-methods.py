#4 capitalize, title, lower, upper, swapcase methods

sentence = 'once upon a time'
print(sentence.capitalize()) #capitalizes first letter of string
print(sentence.title()) #makes all first letters of each word in string capital like a title
print(sentence.upper()) #converts all cases to upper case
print('HELLO'.lower()) #converts all cases to lower case
print('AbCdE'.swapcase()) #converts capital letters to lower and vice versa

#Method Chaining: applying multiple methods on same string

print('SUBHASH CHANDRA BOSE'.lower().title()) #first strig will be converted to lower, then title

print()

#untill now the real string of sentence is not changed. it remains the same as declared on line 3
print(sentence) #because strings are immutable
#But if we want to change original string to new string we have to assign the new string to old one
sentence = sentence.title()
print(sentence)#now the string is changed to new string ie 'Once Upon A Time

print(sentence.swapcase())