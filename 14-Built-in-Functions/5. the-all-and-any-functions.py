#all function: all(iterable): returns True if all elements are True
#any function: any(iterable): returns True if any element of list is True

print(all([True]))
print(all([True, True]))
print(all([True, True, False])) #false coz one element is falsy
print(all(['a', 'b']))
print(all(['a', 'b', '']))
print(all([1,2]))
print(all([1,2, 0])) #false coz 0 is falsy
print(all([]))  #empty list in all will return True

print()

print(any([True, False]))
print(any([False, False]))
print(any([1,2,0]))
print(any([0]))
print(any(['a', 'b', '']))
print(any(['', '', '']))
print(any([])) #empty list in any will return False

# print(any(True, False)) #doesnt accept sequential arguments