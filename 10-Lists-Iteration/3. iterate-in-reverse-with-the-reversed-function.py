# iteration in reverse order using reversed function:

movies = ['Avengers', 'Age of ultron', 'InfinityWars', 'Endgame']
for movie in movies[::-1]:
    print(f'{movie} has total of {len(movie)} characters')

print()
#another way is using the reversed funciton:

print(reversed(movies)) 
print(type(reversed(movies))) #the output we get is a type of class called 'list_reverseiterator'
#the reversed finction is giving back an object called 'generator object'
#generator object do not store all elements in memory instead only the next one. ie one at a time
# generators prove more effective when list is massive or big text file.
# it goes one line at a time instead of processing every line at same time.

for movie in reversed(movies):
    print(f'{movie} has total of {len(movie)} characters')