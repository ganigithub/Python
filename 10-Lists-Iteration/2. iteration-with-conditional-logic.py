#only add odd number in list:

values = [1,2,3,4,5,6,7,8,9,10]
other_values = [3, 45, 23, 87, 1, 87, 445]

def odd_sum(numbers):
    total = 0
    for odd_numbers in numbers:
        if odd_numbers % 2 != 0:
            total += odd_numbers
    return total

print(odd_sum(values))
print(odd_sum(other_values))

print()
#Give the greatest number in the list:

def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(greatest_number([1, 50, 2, 4, 1, 4, 35]))
print(greatest_number([23, -23, 11, 99, 99.99]))
print(greatest_number([-23, -1, -5]))
print(greatest_number([1,5,3]))
