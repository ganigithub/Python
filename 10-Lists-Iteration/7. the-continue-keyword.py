#continue keyword: forces for loop to continue to next iteration ie. skip particular element.
#Doesnt terminate whole loop like break keyword but skips an element

#if i want to add all positive no's from list, one way to do it is:

def addition(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

print(addition([1, -4, 1, -5]))

#in above case, for loop checks for every number whether its positive or not and then adds to total
#the continue keyword will simply skip the negative no's and add positive no's

def addition(numbers):
    total = 0
    for number in numbers:
        if number < 0:
            continue
        total += number
    return total

print(addition([1, 2, -1, 5, -10, 3]))