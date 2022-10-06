# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(lists):
    total = 0
    for numbers in lists:
        for number in numbers:
            total += number
    return total
print(nested_sum([[1,2,3], [4,5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])       => "ABC"

def fancy_concatenate(lists):
    final = ''
    for row in lists:
        if len(row) == 3:
            for string in row:
                final += string
    return final

print(fancy_concatenate([['a', 'b', 'c']]))        
print(fancy_concatenate([['a', 'b', 'c'], ['d', 'e', 'f']]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B"], ['C', 'D']]))