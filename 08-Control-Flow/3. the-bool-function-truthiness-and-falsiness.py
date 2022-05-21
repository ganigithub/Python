#3: Truthiness and Falsiness

if 3:             #if 3: doesnt make sense so python considers it has a Truthiness and body executes
    print('hello')

if 0:                          # 0 is considered to have a Falsiness and body doesnt execute
    print('will this print?')

if 'hi':                       # strings aslo have truthiness so body executes
    print('garry')

if '':                         # an empty string has Falsiness 
    print('will this print?')

#to check if some function have truthiness or falsiness, use built in function bool()

print(bool(3))     #any no other than 0 is considered to be Truthiness
print(bool(0))
print(bool('hi'))  
print(bool(''))
print(bool(7.123))
print(bool(-23))