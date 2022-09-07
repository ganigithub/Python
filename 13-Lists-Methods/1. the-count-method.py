#count method: .count(arg): counts how many times an element is in list. gives 0 if element doesn't exist

fruit = ['mango', 'banana', 'apple', 'banana', 'pineapple', 'mango', 'mango']
print(fruit.count('banana'))
print(fruit.count('mango'))
print(fruit.count('Mango')) #count method is case sensetive
print(fruit.count('grapes'))

print()
float = [4.3, 7.3, 7.3, 9.0, 9, 4.3, 4.3]
print(float.count(4.3))
print(float.count(7.3))
print(float.count(9))