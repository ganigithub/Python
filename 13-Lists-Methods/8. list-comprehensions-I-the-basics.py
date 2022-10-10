#list comprehension: another way to create a list from another list
#new list created doesnt mutate original list.

numbers = [1,2,3,4,5]
# squares = []
# for number in numbers:
#     squares.append(number ** 2)
# print(squares)
# print(number) #here number has value 5 coz its last element in list which can cause prblm 
# #in we want to use this variable somewhare else.

#another way to do this is list comprehension

squares = [number ** 2 for number in numbers]
print(squares)

expressions = ['lol', 'rofl', 'lmao']
print([expression.upper() for expression in expressions])

cars = ['Ford', 'Ferrari', 'Mercs']
print([len(car) for car in cars])

decimals = [3.3, 45.3, 11.1 , 10]
print([int(decimal) for decimal in decimals])