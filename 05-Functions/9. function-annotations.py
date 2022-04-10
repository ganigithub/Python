#9. Function annotation: we use this to document what datatype a 
#parameter should be by using colon sign ":"
# function annotation is just documentation or a note. its not mandatory

def word_multiplier(word: str, type: int) -> str :
#word: str represents word must be a string though its not mandatory
# -> represents final datatype of output again not mandatory
    return word * type

print(word_multiplier('dog', 3))
print(word_multiplier(3, 3))   #here word is in form of integer and we will get the 
#output which shows its just for note and not mandatory.