# break keyword terminates for loop before it reaches its conclusion

# print(3 in [1,2,3,4,5]) #here 3 is at position 2 but python goes on for searching till end of list
#if we want code to stop once we found what we need, be can use break keyword to terminate loop

def contains(values, target):
    found = False
    for value in values:
        if value == target:
            found = True
            break           #here once target is found, for loop breaks. this saves time insted of
    return found            #searching the whole list

print(contains([1,2,3,4,5], 5))
print(contains([1,2,3,4,5], 6))