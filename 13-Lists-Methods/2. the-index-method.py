#index method: .index(arg, index) gives the index position of first occurrence of value in list
#can accept one or two arguments

fruits = ['mango', 'banana', 'apple', 'mango', 'apple', 'pineapple', 'guava']
print(fruits.index('banana'))
print(fruits.index('mango'))
print(fruits.index('apple'))

print(fruits.index('mango', 1)) #second argument is position from which we want to start search
print(fruits.index('apple', 3))
print(fruits.index('apple', 2)) #second argument is inclusive in search
# print(fruits.index('grapes')) #valueError is raised if value doesn't exist

# print(fruits.rindex('apple')) #AttributeError is raised here coz, python doesnt seartch apple
#from right side like it does in case of a string. find, rfind, rindex method are not available
#for lists.