#insert method: .insert(index, arg): add an element in between the list

countries = ['Bhutan', 'SriLanka', 'Nepal']

countries.insert(1, 'Bharat') #first object is the index position and second object is the insert value
print(countries)

countries.insert(0, 'Bangladesh')
print(countries)

countries.insert(10, 'Australia') #python detects index is out of range so its adds to end of list
print(countries)

countries.insert(-10, 'England')
print(countries)

# countries.insert(1, 'South Africa', 'Nepal') #insert takes only two arguments. one index and 
# print(countries)                             # one value