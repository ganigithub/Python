# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]

def word_length(string):
    lengths = []
    list = string.split(' ')
    for word in list:
        lengths.append(len(word))
    return lengths   

print(word_length('Mary Poppins was a nanny'))
print(word_length('I am learning python'))

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string

# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup(strings):
    final = []
    for word in strings:
        if word.isspace() or len(word) == 0:
            continue
       
        final.append(word)

    return ' '.join(final)

print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", '     ', "er", "pillar"]))
print(cleanup(["",'', " "]))