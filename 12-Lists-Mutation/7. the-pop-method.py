#pop method: .pop(index): removes the last element from list

countries = ['India', 'Bangladesh', 'Nepal', 'SriLanka']
countries.pop()  #defalt argument in pop is -1 ie. last element in list
print(countries)

last = countries.pop() #Here Nepal bacomes the last element in new list
print(last) 

print()

fruits = ['mango', 'apple', 'banana', 'guava']
fruits.pop(1)  #removes the element at index position 1 ie apple
print(fruits)
print(fruits.pop(1))  #now banana is at position 1 in new list