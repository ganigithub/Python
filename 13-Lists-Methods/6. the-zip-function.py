# zip function:zip(arguments): if we want to iterate all elements in multiple lists at same time, we use zip funciton.

breakfasts = ['Eggs', 'Bread', 'Cereal']
lunches = ['Chicken', 'Rice', 'Biryani']
dinners = ['Fried rice', 'Pasta', 'Noodles']

# elements of all lists at common index positions can be accessed using zip function.

print(zip(breakfasts, lunches, dinners))
print(type(zip(breakfasts, lunches, dinners))) #zip function has zip class. which is iterable one sequence at a time.
print(list(zip(breakfasts, lunches, dinners))) #by passing list function, we can get separate lists of elements at common
# index positions called tuple. see output

print()

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners): #we need 3 variables to represent each brkfst,lunch,dinner
    print(f'I ate {breakfast} for breakfast, {lunch} for lunch and {dinner} for dinner!') 