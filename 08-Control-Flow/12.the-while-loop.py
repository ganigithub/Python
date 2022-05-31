#12 while loop :

count = 0   #value of count is set to be 0

while count <= 5:    #this line is repeated until count is <= 5
    print(count)     #this line prints count 
    count += 1       #this line adds 1 to the previous count until values is 6

print()
print(count)        #upto here value of count is 6 

print()
while count <=10:
    print(count)
    count += 1

print()
while count <= 10: #this will not be executed again coz count has value of 11 which is more than 10
    print(count)
    count += 1

# make a program that will tell user to input no more than 10. use while loop

invalid_number = True
while invalid_number:
    user_value = int(input('Enter number more than 10: '))
    if user_value > 10: 
        print(f'{user_value} is a great choice!')
        invalid_number = False
        if user_value == 100:
            print('congrats your score is perfect')
    else: 
        print(f'{user_value} is not more than 10! Try again!')