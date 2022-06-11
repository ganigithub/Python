#1. List: a data structure that stores an ordered sequence of objects also called Array

empty = []  #here empty is a list with no objects in it. Its an empty list
empty = list() #list can also be created like this but line 3 is preferred

juice = ['mango', 'apple', 'orange']  #objects in list are called elements
print(len(juice))                     # length of list is number of elements it holds

marks = [100, 98, 35, 88]             #elements are stored in order in list
print(len(marks))

pointer = [6.38, 8.87, 9.3, 9.5, 10]
print(len(pointer))

settings = [True, False, True]    #elements of all same type are called homogenous list
print(len(settings))

mixed = ['garry', 99.99, 78, True] #list with different element types can also be created
print(len(mixed))