# 4 input function

first_name = input('whats you name? ')
print( 'welcome', first_name, '!')

age = input('what is your age? ')
print('so you are', age, 'years old. Thats nice.')

a = input('choose a number ')
a = int(a)
print('so u have chosen your first no as ',a )
b = input('choose another nubmer ')
b = int(b)
print('so u have chosen ur sec no as ',b)
print('so the sum of ur nos is', a+b)

#line 9 & 10 and line 12 &13 can be written shortly as;
a = int(input('choose a number '))
b = int(input('choose another number '))
print('so sum of your numbers is', a + b)