#debugging: to check if everything in code is working properly
#breakpoint: line of the function where python will pause. Python executes upto only breakpoint

print('Hi I am learning Python3') #when run this line, in terminal, we get the o/p of this line.
#we will go all the way to upto next breakpoint ie. line 13. but line 12 - 15
#will not execute coz there is no invocation of do_fun_stuff() upto line 13.
#so python skips whole body and jumps to line 18 where function is invoked
# Now that function is invoked, body runs upto line 13. then 16.
#after that line 19 will be executed and finally we will get return value of a

def do_fun_stuff():
    a = 20
    print('Hello')
    print('Bye')
    a = 25
    return a
 
fianl = do_fun_stuff()
print(do_fun_stuff())

#VARIABLE section on left side in debugging section gives current values of variables.
#eg here a = 20 before line 13. then a = 25 before line 16. 

#CALL STACK section tells why we are at a particular line. or whether we are inside a function.
#eg here when line 18 is executed, call stack section tells we at line 13 becasue of line 18

#BREAKPOINTS section tell where are the breakpoints in code.