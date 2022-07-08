#command line arguments with argv (use terminal)

import sys #module is a buldle of related code. #python doesnt store every function to save memory.
#We use import to import some functionality 
#sys on line 3 is a module means system. its related to functoinalities related to computer system

print(sys.argv) #this is dot based syntex. We get a piece of data of this module or box using dot.
#argv stands for argument variable consisting a list of all arguments we get from command line
#line 7 will give the string of current file name.

print(type(sys.argv)) #sys.argv has a class of list

#if we want to add arguments in command line, we simply add arguments with space bet them.
#add argument after the file name in command line

#if we want to make a program which adds lengths of arguments:

word_lengths = 0
for arg in sys.argv[1:]: #[1:] because first argument in command line is the name of file. We want to
    word_lengths += len(arg)  #skip that and add rest arguments in line.
print(f'total length of command line arguments is {word_lengths}') 

# insert arguments like garry and gani in command line after the file name in terminal and see output