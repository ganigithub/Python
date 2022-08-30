#sort method: .sort(): sorts elements of list in ascending order if list has numbers
# and sorts alphabatically if elements are words

nubmers = [1,10,6,50, 45]
nubmers.sort()
print(nubmers) #gives list in ascending order

nubmers.reverse()
print(nubmers) #be applying reverse, we reverse the already mutated list which gives list in 
#descending order

#sort method is case sensetive ie. case of first letter of words matter.

fruits = ['Mango', 'Apple', 'Banana', 'Guava']
fruits.sort()
print(fruits)

fruits = ['Mango', 'apple', 'banana', 'Guava']
fruits.sort()
print(fruits)
#in above case, python first sorts words with capital letters first. and then sorts words with lower case
#hence, python first sorts Mango and Guava then apple and banana

letters = ['a', 'A', 'B', 'b']
letters.sort()
print(letters)

a = ['Abd', 'Abc']
a.sort()
print(a)

print()
#if we dont want to mutate the original list, we can use built in sorted function.

fruits = ['Mango', 'apple', 'banana', 'Guava']
print(sorted(fruits)) #we get sorted list using built in sorted function
print(fruits) #we can see original list is unchanged