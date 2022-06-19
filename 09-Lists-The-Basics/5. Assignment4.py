# Declare a nested_extraction function that accepts a list of lists and an index position.
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.

def nested_extraction(number, string):
    return string[number][number]

string=[[1,2,3], [4,5,6], [7,8,9]]
print(nested_extraction(0, string ))
print(nested_extraction(1, string))
print(nested_extraction(2, string))

#Declare a beginning_and_end function that accepts a list of elements.
#It should return True if the first and last elements in the list are equal and False if they are
#unequal. Assume the list will always have at least 1 element.

def beginning_and_end(element):
    return element[0] == element[-1]
print(beginning_and_end(['hi', 'bye', 'hi']))
print(beginning_and_end(['hi', 'bye', 'goodbye']))
print(beginning_and_end([1,2,3,4,1]))
print(beginning_and_end([1,2,3,4]))

print()
# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.

def long_word_in_collection(elements, target):
    return target in elements and len(target)>4

elements = ['clothes', 'glasses', 'cap', 'tye']
print(long_word_in_collection(elements, 'clothes'))
print(long_word_in_collection(elements, 'cap'))
print(long_word_in_collection(elements, 'glasses'))
print(long_word_in_collection(elements, 'tye'))