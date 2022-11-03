#lambda function: anonymous funciton: funciton without name
#they dont exist after using them. we can't access them later

animals = ['cat', 'dog', 'donkey', 'lion', 'cheetah', 'elephant']
print(list(filter(lambda animal : len(animal)> 5, animals)))
#using lambda function we dont need to define a first argument for filter function

#return list of animals having letter 'e' in them.
print(list(filter(lambda animal: 'e' in animal, animals)))

#how many times character 'e' appears in each element: use map function and lambda function
print(list(map(lambda animal: animal.count('e'), animals)))

#replace d with $ using lambda function
# print(list(map(lambda animal: animal.replace('d', '$'), animals)))
print(list(map(lambda animal: animal.replace('d', '$'), animals)))