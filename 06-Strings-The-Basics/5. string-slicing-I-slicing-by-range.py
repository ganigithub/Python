# 6. slicing by range I 
#to slice the sentence or word we use start_index:end_index where, start_index is included
# and end_index is excluded

address = 'subhash, Mumbai, Maharashtra'
print(address[0:10]) #index 0 ie s is included and index 10 ie u is excluded
print(address[9:20])
print(address[0:100]) #though there are less than 100 characters, python will be friendly
# and assume we want to go all the way to last character, thus whole expression is printed.

print()  # used to add space in return valued in output to avoid confusion

print(address[9:-6]) #also here, index -6 i.e. a is excluded, a letter before it is included
print(address[-19:100])
print(address[-11:-1])

print()

print(address[9:]) # no end_index after colon means from index 9 to the end of string
print(address[:10]) # no start_index before colon means from start of string to index 10
print(address[:-3])
print(address[-11:])

print(address[:]) #this will give whole string as output as no indexing is provided. python
#creates a copy of string in this case and gives as output.