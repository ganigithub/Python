# 1. Length : counts no. of characters in a string
print(len('hello'))
print(len('12334'))
print(len('(^&#&*@@*!'))
print(len(' '))
print(len(''))

# length function doesnt work for integers, bools or floats
# print(len(312))
# print(len(3.133))
# print(len(True))

#concatenation. The strings here are immutable ie. unchangable. garry and getto are 
#two diff strings and we get output of third new string. fundamentally strings garry
#and getto are immutable ie unchangable
print('garry' + 'getto')
print('garry '+'getto')
print('garry'+' '+'getto') 
print('s' 's' 's')
print('hi' * 10)