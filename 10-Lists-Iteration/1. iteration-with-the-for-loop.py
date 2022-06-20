# Iteration : repeating steps over and over like a loop
# Iterable objects: data structures from which "successive items can be obtained until supply is 
# exhausted"

food = 'Rice and Biryani'
for character in food:
    print(character)

print()
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

print()
numbers = [1,2,3,4,5]
for squares in numbers:
    print(squares ** 2)

print()
movies = ['Avengers', 'Thor', 'Loki', 'Captain America']
for good_movie in movies:
    print(len(good_movie))

print()
print(squares)     #at this point squares has value 5 coz its last number in list
print(good_movie) #similarly good_movie has value Captain America coz its last element of list
print(character) #here character has value i coz i is the last character in the string

print()
#if we want to all the numbers in list using for loop:
numbers = [23, 4, 5, 10]

total = 0
for number in numbers:
    total += number

print(total)