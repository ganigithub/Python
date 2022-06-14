# 2. in and not in operators:

print('break' in 'breakfast')
print('break' not in 'breakfast')
print('food' not in 'breakfast')

print()

food = ['breakfast', 'lunch', 'dinner']
print('lunch' in food)
print('Breakfast' in food)
print('dinner' in food)
print('fast' in food)

print()

marks = [100, 99.0, 35]
print(100 in marks)
print(99.0 in marks)
print(99 in marks)

print()

print('lunch' not in food)
print('Lunch' not in food)
print(35 not in marks)
print(50 not in marks)

print(7 not in [1,2,3])