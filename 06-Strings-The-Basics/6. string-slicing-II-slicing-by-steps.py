# 7. string slicing in steps II
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0:26])
print(alphabet[0:26:2]) #the number after second colon will give output in steps
# i.e output will jump by 2 letters (see output)
print(alphabet[0:26:5]) #here output will jump by 5 letters
print(alphabet[:26:5])
print(alphabet[0::5])
print(alphabet[::5])

print()
print(alphabet[-20:-1:3])

print()
print(alphabet[26:1:-3]) #negative value after second colon will give output in reverse steps
#while going reverse, consider value before first colon as second_index and after colon as first
#although the inclusive and exclusive property reamains same.
#above consideration is done by me not BORIS
print(alphabet[::-2])
print(alphabet[::-1])