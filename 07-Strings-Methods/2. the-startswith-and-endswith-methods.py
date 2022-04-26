#2. Startswith method: returns true if string starts with the value
sentence = 'Bob the Builder'
print(sentence.startswith('B'))
print(sentence.startswith('b'))
print(sentence.startswith('Bob'))
print(sentence.startswith('bob'))

print()

# endswith method: returns true if string ends with the value
print(sentence.endswith('r'))
print(sentence.endswith('Builder'))
print(sentence.endswith('builder'))