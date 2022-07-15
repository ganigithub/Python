#step into: stepinto will move into a nested execution context into a nested scope.
#step out: stepout will come out of a nested scope.

# simply setpinto will go one level deeper into the nested scope eg. moving
#into function from file
# step out will come one lever higher of scope. eg moving from a function to file.

print('Hi I am learning Python3')
def do_fun_stuff():
    a = 20
    print('Hello')
    print('Bye')
    a = 25
    return a
fianl = do_fun_stuff()
print(do_fun_stuff())