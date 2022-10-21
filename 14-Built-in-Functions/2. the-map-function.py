#map function: map(func, iterable): whatever we can do with a number or string, we can do it with a function
#map function accepts two arguments one is function itself and other an iterable like list or str
#first argument will invoke on every element of second argument.

#return cubes of numbers using list comprehension method and map function

numbers = [1,2,3,4,5]
cubes = [number ** 3 for number in numbers]
print(cubes)
#above method is list comprehension.
#another way to do this is by using map function:

def cube(number):         #we need to define cube function as its not a builtin funciton
    return number ** 3
print(map(cube, numbers)) #this will return map iterator object
print(list(map(cube, numbers))) #to create a list, we use list function

cars = ['mercs', 'ford', 'benz', 'totyota', 'ferrari']
print([len(car) for car in cars]) #list comprehension
print(list(map(len, cars))) #map function. we dont need to define len function coz its builtin.