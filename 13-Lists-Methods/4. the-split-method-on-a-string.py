# split method: .split(seperator/delimiter, maxsplit): convers the words in a string in form of list.

cars = 'Mercs, Benze, Ferrari, Ford'
print(cars.split(', ')) #the argument we provide is a seperator that tells python where to end the word in list
#in this case a seperator is a comma followed by a space. 
#common occurrence between two characters is called a delimiter. comma followed by space is delimiter in this case

print(cars.split(', ', 2)) #second argument is the maxsplit number. ie maximum split we want. here we gave 2 as maxsplit
#means python cuts only two times and rest words are not split. see output

sentence = 'I am learning Python'
word = sentence.split(' ')
print(word)