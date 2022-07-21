# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.

def length_match(strings, integer):
    count = 0
    for string in strings:
        if len(string) == integer:
            count += 1
    return count

print(length_match(['cat', 'dog', 'pigeon', 'mouse', 'moose'], 3))
print(length_match(['cat', 'dog', 'pigeon', 'mouse', 'moose'], 5))
print(length_match(['cat', 'dog', 'pigeon', 'mouse', 'moose'], 4))
print(length_match([], 1))

#Declare a sum_from function that accepts two numbers as arguments.
#The second number will always be greater than the first number.
#The function should return the sum of all numbers from first number to second number(inclusive).

def sum_from(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total    

print(sum_from(1,2))
print(sum_from(1,5))
print(sum_from(0,1))

#Declare a same_index_values function that accepts two lists.
#function should return a list of the index positions in which the two lists have equal elements

def same_index_values(list_1, list_2):
    final = []
    for index, element in enumerate(list_1): #we dont need to iterate elements of both lists. by keeping track
        if element == list_2[index]: #of one index position in one list, we can correspondingly keep track of other
            final.append(index)
    return final

print(same_index_values([1,2,3], [3,2,1]))
print(same_index_values(['a', 'b', 'c', 'd'], ['c', 'b', 'a', 'd']))