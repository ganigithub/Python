# 1. Method: a fucntion that acts on a specific object
#Find method: It gives the index position from where the substring starts in the main string.

sentence = 'Google Chrome'
print(sentence.find('C')) #this will give index position of letter C
print(sentence.find('c')) #Find method is case Sensitive so -1 will be output
print(sentence.find('X'))
print(sentence.find('Chr'))
print(sentence.find('o')) #Here letter o is repeated thrice in string. No matter how many times 
# the letter or string is repeated, it will give the first position

print()

print(sentence.find('o'))
print(sentence.find('o', 2)) # here python searches letter o starting from index position 2 and
# not from begenning. 
print(sentence.find('o', 5,9)) #python searches for o from index 5 to 9
print(sentence.find('o', 5))

#Remember, in above case, python will search o from 5th index position but index that we will get
# in output will be index position from begenning. 
print()

#Index Method: Similar to find method
print(sentence.index('C'))
# print(sentence.index('c')) #If string or character doesnt exist, ValueError will be raised.

print()

#rfind method: similar to find method. but searches from right or gives last occurence of the string.

print('Sameer samera'.rfind('s')) #however indexing that we will get will start from beginning
print('Sameer samera'.rfind('x')) #gives -1 if string not found

#rindex method: similar to rfind method. but raises ValueError if string not found
print('Sameer samera'.rindex('s')) 
# print('Sameer samera'.rindex('x'))