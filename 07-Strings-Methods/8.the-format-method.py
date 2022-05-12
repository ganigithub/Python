#8. format method: 

sentence = '{} slipped on a {} {}'              #{} is used to inject inputs

print(sentence.format('garry', 'funny', 'slide')) # the strings are injected in order
print(sentence.format('garry', 'slide', 'funny'))
# print(sentence.format('garry', 'slide')) #IndexError is raised as there are only two inputs
print(sentence.format('garry', 'large', 'potato', 'slide')) #python ignores the extra input given

print()

### injecting by indexing

sentence ='{0} slipped on a {1} {2}' #numbers in {} represent order of indexing in which the values
# will be injected
print(sentence.format('garry', 'huge', 'cactus'))#here 'garry', 'huge', 'cactus' have indexing 0,1,2
          #indexing ->  '0'  ,  '1'  ,    '2'

print(sentence.format('garry', 'cactus', 'huge')) 
          #indexing ->  '0'  ,    '1'     '2'
print()

sentence = '{2} slipped on a {0} {1}'
print(sentence.format('garry', 'slippery', 'surface'))

print()
### injecting by name:

sentence = '{name} saw a {adjective} {noun}'
print(sentence.format(name = 'garry', adjective = 'green', noun = 'alien'))
print(sentence.format(adjective = 'green', noun = 'alien', name = 'garry')) #order doesnt matter

print()

###using input method
sentence = '{name} shouted at a {adjective} {noun}'

name = input('enter a name: ')
adjective = input('enter an adjective: ')
noun = input('enter a noun: ')

print(sentence.format(name = name, adjective = adjective, noun = noun))