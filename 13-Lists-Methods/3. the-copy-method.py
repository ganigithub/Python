#copy method: .copy(): creates a copy of 1Dimentional list. 1D list: list that doesn't have nested lists in it
fruits = ['mango', 'banana', 'guava', 'grapes', 'apple', 'pineapple']
print(fruits.copy())

copied_fruits = fruits.copy()
print(copied_fruits)

copied_fruits.remove('banana')
print(copied_fruits)
print(fruits)  #the change in copied list doesn't affect the original list

#another way to create a copy  list is:
cars = ['mercs', 'ferrari', 'ford']
new = cars[:]
print(new)