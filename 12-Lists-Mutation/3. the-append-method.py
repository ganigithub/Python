#append method: .append(arg): adds element to end of list

countries = ['India', 'Bangladesh', 'SriLanka']
countries.append('Bhutan')
print(countries)

# countries.append('Afghan', 'Australia')  #append method takes only one argument thats to be added
# print(countries)

countries = countries.append('Japan') #here countries.append() has value None and we are assigning that to countries
print(countries) #None will be output