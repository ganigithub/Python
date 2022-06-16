#4. List slicing

print('guitar'[1:5]) #index before colon is inclusive and after colon is exclusive

clothes = ['shirt', 'lungi', 'jeans', 'pant', 'cap']
print(clothes[0:3])
print(clothes[2:3])
print(clothes[:4])
print(clothes[2:])
print(clothes[0:100])
print(clothes[:])


print()
print(clothes[-3:4])
print(clothes[-5:-1])
print(clothes[-5:100])

print()
print(clothes[0:-1:2])
print(clothes[0:-1:1])
print(clothes[::1])
print(clothes[::-1])
print(clothes[::-4])