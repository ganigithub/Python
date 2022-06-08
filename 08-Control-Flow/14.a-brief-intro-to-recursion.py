#14. Recusrion: when function calls itself

def count_down_from(number):
    start = number
    while start > 0:
        print(start)
        start -= 1
print(count_down_from(5))

print()
#another way to do above code using Recursion method is:

def count_down_from(number):
    if number <= 0:             # when finally number is 0, this line is True and function stops
        return                  # called Base line
    else: 
        print(number)
    count_down_from(number - 1)  #here the function count_down_from is invoked within itself called
                                 # Recursion which will repeat itself untill we introduce Base Case
                                 # Base Case: condition that tell function to stop running. line 14
print(count_down_from(5))