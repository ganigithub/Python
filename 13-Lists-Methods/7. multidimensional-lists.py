#multidimentional list: lists having multiple lists within. Nested lists

cars = [
    ['Mercs', 'Ferrari', 'Ford'],
    ['Toyota', 'Skoda'],
    ['Suzuki', 'Tata', 'Jaguar', 'Land Rover']
]

print(len(cars)) #length of cars is 3
print(cars[0]) #frist nested list is at index position 0
print(cars[1])
print(cars[-1])

print(len(cars[2]))

print()
print(cars[0][2]) #gives third element of first nested list
print(cars[1][0])
print(cars[2][-1])

print()
print(cars[:]) #see output
print(cars[:2]) 
print(cars[2][1:3])

print()
#we can iterate over each element of multidimentional list and each element of nested list.

all_cars = []
for lists in cars:
    for car in lists:
        all_cars.append(car)
print(all_cars) #see output