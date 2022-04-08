#5 assignment

# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
def easy_money():
    return 100
money = easy_money()
print(money)

# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    return 'sushi'
food = best_food_ever()
print(food)

# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign,
# and return the result. 
def convert_to_currency(amount):
    return '$'+ str(amount)

result = convert_to_currency(75)
print (result)