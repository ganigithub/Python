# def reverse(str):
#     first_index = 0
#     last_index = len(str) - 1
#     reversed_string = ''
#     while last_index >= 0:
#         reversed_string += str[last_index]
#         last_index -= 1    
#     return(reversed_string)
# print(reverse('mobile'))

def reverse(str):
    if len(str) <= 1:           #this is base case for recursion of reverse(str)
        return str
    
    return str[-1] + reverse(str[0:-1])

print(reverse('garry'))

# y + reverse[garr]
# y + r + reverse[gar]
# y + r + r + reverse[ga]
# y + r + r + a + reverse[g]
# y + r + r + a + g