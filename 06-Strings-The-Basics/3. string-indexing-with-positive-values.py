# 3. String indexing
#string indexing ie. counting starts with zero and not one.

word = 'python'
print(word[0]) # P is the 0th character
print(word[1]) # y is the 1st character
print(word[5]) # n is the 5th character
print(word[2*2]) 
print(word[2+2])
print(word[2-2])

#however the length of the word starts with one
print(len(word))

#since strings are immutable, any character cannot be assigned to different character
# word[0] = 'B'  #this raises type error as string doesnt support item assignment

#print(word[100]) #this will raise index error coz only 6 characters are there

print(type(word[3])) #the output character is also a string datatype