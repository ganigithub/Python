#filter function: filter(func, iterable): extracts subset of values from a list based on condition being met.
#accepts two arguments. one is the function which must return a bool and other iterable like a list

#return elements that has length more than 5 using list comprehension and filter funciton

animals = ['cat', 'dog', 'giraffe', 'elephant', 'cheetah']
print([animal for animal in animals if len(animal) > 5]) #list comprehension

def is_long_word(animal):
    return len(animal) > 5

print(filter(is_long_word, animals)) #this will return a filter object
print(list(filter(is_long_word, animals)))

#remember, the first argument in filter function ie function must return a bool
#in short, filter function decides which element should be kept depending on bool value(True/False) of 
#first argument