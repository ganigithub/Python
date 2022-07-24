#declare a squares function which returns the squares of each number in list in form of list

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares
numbers = [1,2,3,4,5, 20, 40, -2, 3.3]
print(squares(numbers))

#declare a convert_to_float function which returns float value of each number in form of list

def convert_to_float(numbers):
    final = []
    for number in numbers:
        final.append(float(number))
    return final
print(convert_to_float([1,2,3,4,5]))

#declare a even_or_odd function which returs list of True, False if numbers are even its True and if odd its False.

def even_or_odd(numbers):
    final = []
    for number in numbers:
        final.append(number % 2 == 0)
    return final
print(even_or_odd([1,2,4,5,6]))

#in all of the above case notice that we built a complete new list from an existing list. 
#Hence building a list from another list
