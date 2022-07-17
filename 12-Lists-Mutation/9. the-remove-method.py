# remove method: .remove(arg): removes or deletes the first occurance of an element in list. it removes by value
# and not index position unlike pop method and del keyword

fruits = ['mango', 'apple', 'banana', 'guava']

fruits.remove('mango')
print(fruits)

fruits = ['mango', 'apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)  #here only the first occurance of apple is removed. last element is still in list