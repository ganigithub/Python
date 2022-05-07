#7. replace method: replaces the character with new one

mobile_number = '123 345 999'
print(mobile_number.replace(' ', '-')) #replaces empty space with -
print(mobile_number.replace(' ', '---'))
print(mobile_number.replace('9', '1'))
print(mobile_number.replace('9', '10'))

mobile_number = mobile_number.replace(' ', '-')
print(mobile_number)