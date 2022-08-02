# extend method: .extend(arguments): add a new list to the end of existing list. unlike append, extend method can
#add more than one element in list

countries = ['India', 'Bhutan']
countries.extend(['SriLanka', 'Bangladesh'])
print(countries)

more_countries = ['China', 'Nepal', 'Russia']
countries.extend(more_countries)
print(countries)

#in above cases, extend method is mutating the original list
#we can do above thing by using + sign but that wouldn't change the original list infact 
#it creates a brand new string 

list1 = ['a', 'b']
list2 = ['c','d']
list3 = list1 + list2
print(list3) #this is comletely a new list
print(list1) #we can see here original list of list1 and list2 are not changed or mutated
print(list2) 

list1 += list2
print(list1)  #Here the original list1 is mutated to a new list