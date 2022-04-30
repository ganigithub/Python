#3. Count method: counts how many times a string or value is in the main string
sentence = 'queueing'

print(sentence.count('q'))
print(sentence.count('u'))
print(sentence.count('e'))
print(sentence.count('Q')) #this doesnt exist so output will be 0
print(sentence.count('ue')) #python will search exactly how many times ue is there in string
print(sentence.count('ing'))

print()

print(sentence.count('u') + sentence.count('e')) #this will add how many times u and e are in string