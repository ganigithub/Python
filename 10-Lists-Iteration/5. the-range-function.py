# range function: used to generate collection of ordered numbers

for number in range(5):  #range function prints values from 0 to one number less than argument
    print(number)        # 5 is not inclusive in output

print()
for number in range(0,5): #here 0 is inclusive and 5 is excluded much like indexing
    print(number)

print()
for number in range(10, 101, 10): #this gives range from 10 t0 100 in increments of 10
    print(number)

print()
for number in range(10,0,-1): #this gives range from 0 to 10 in reverse order
    print(number)             #10 is inclusive and 0 is exclusive

print()
# give a function that gives product of every even number within range of your choice
product = 1
for number in range(1,11):
    if number % 2 == 0:
        product *= number
print(product)