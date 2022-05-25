# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero
# negative_energy(10)   => 10
# negative_energy(-5)   => 5

def negative_energy(a):
    if a > 0:
        return a
    elif a < 0:
        return -a
    else:
        return 0

print(negative_energy(10))
print(negative_energy(-10))
print(negative_energy(-5))
print(negative_energy(0))

#another way to redefine the code is;
def negative_energy(a):
    if a > 0: return a
    else: return -a

print(negative_energy(10))
print(negative_energy(-10))
print(negative_energy(-5))
print(negative_energy(0))