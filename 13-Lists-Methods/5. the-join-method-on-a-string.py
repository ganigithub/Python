# join method: combines elements of list into string

address = ['Marine Drive', 'Churchgate', '123456']
print(', '.join(address))
#       |
#    seperator: what will be the seperator between two elements in list.

print('-'.join(['123', '456', '7890']))

# print('-'.join([123, 456, 222])) #typeError will be raised coz join method only joins 
# string elements of list