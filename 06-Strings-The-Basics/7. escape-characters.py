
print('Hello, \nmy name is Garry. \nI live in Mumbai.') #\n is used to break line.
print('\tI am learning Python3 \tfrom computer from last 3 months')#\t will add indentation(space)
print('I live on \tEarth, which is \n\t3rd planet') #or combination of both

#lets say i want to print a path of a file which is c:\news\trave. In this case python will 
# see \n and \t as special character and we will not get the print properly. So to avoid python
# to see these as special character is, we use letter r as in RAW
print('\n')
print('c:\news\travel') # to avoid this problem we use Raw
print(r'C:\news\travel')

#to avoid double and single inverted commas, we use Escape character \
print('Hi my name is \'Garry\'') #the \ before ' or " will allow python to ignore that
print("Hi my name is \"Garry\"")

print('lets print a backshlash: \\')

#we can break up line or expression if its too long eg;
some_random_number = 2
some_wrong_calculation = 3
additional_number_picked_from_somewhere = 4

# final = some_random_number + \ 
        # some_wrong_calculation + \ 
        # additional_number_picked_from_somewhere

print(some_random_number,
        some_wrong_calculation, 
        additional_number_picked_from_somewhere)