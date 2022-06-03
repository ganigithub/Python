# Define a fizzbuzz function that accepts a single number as an argument. 
# The function should print every number from 1 to that argument. 

# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# If the number is not divisible by either 3 or 5, just print the number.

def fizzbuzz(last_number):
    start_number = 1
    while start_number <= last_number:
        if start_number % 15 == 0:
            print('fizzbuzz')
        elif start_number % 3 == 0:
            print('fizz')
        elif start_number % 5 == 0:
            print('buzz')
        else:
            print(start_number)
        start_number += 1

print(fizzbuzz(30))

#Make a program which will tell if your are selected or not
#100 = selected
# < 100 = Try next year
# > 100 = invalid marks (run intill user provides correct input)
# < 0 = marks cannot be negative (run intill user provides correct input)

print('This program will tell if you are selected or not')
marks = True
while marks:
    marks = int(input('Enter your marks: '))
    if marks == 100:
        print('Contrats! You are selected!')
        marks = False
    elif marks < 0:
        print('Marks cannot be negative. Try again!')
    elif marks < 100:
        print('Try next year. Best of Luck!')
        marks = False
    elif marks > 100:
        print('Marks cannot be more than 100. Try again!')