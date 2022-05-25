#6 conditional expression:

pin_code = '123456'

# if len(pin_code) == 6:
#     print('valid')
# else:
#     print('invalid')

#another way of doing above code in simpler way is:

validity = 'valid' if len(pin_code) == 6 else 'invalid'
print(validity)