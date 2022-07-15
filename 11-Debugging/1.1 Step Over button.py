#Step over button: continues to next line in current scope.

# Scope: Current area of execution. A file is one scope and function body in 
#file is another scope.

print('Hi I am learning Python3')
def do_fun_stuff():
    a = 20
    print('Hello')
    print('Bye')
    a = 25
    return a
fianl = do_fun_stuff()
print(do_fun_stuff())