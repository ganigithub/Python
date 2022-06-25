#4. enumerate function: gives the index position of the elements in list

work = ['python', 'quantum', 'outside', 'jogging']
print(enumerate(work))
      
for index, things in enumerate(work): #remember index should be first and then list element(things)
    print(f'{things} is at number {index} on my list to do!')

print()
#indexing starts from 0 obviously but we can do following thing to make output more sensible:
for index, things in enumerate(work):
    print(f'{things} is at number {index + 1} on my list to do')

print()
#other way to do this is to pass in optional argument in enumerate function to start indexig from 1

for index, things in enumerate(work, 1):
    print(f'{things} is at number {index} on my list to do')