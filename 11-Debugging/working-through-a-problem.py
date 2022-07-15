#def function which accepts list of numbers
#function should return sum of each number multiplied by number one less than index
#number

#use debugging and debug colsole if any problems faced.

def iterator(numbers):
    total = 0
    for index,number in enumerate(numbers):
        total += number * (index - 1)
    return total

print(iterator([1,2,3,4,5]))