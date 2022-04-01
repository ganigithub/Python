#parameters #keyword arguments (sep, end, file, flush)
#sep (separator)
print('abc', 'def', 'xyz')
print('abc', 'def', 'xyz', sep='+')
print('abc', 'def', 'xyz', sep='--&--')

#end 
print('1', '2','3', sep='$', end='#')
print('1', '2','3', sep='$')
# line no 8,9 are joined together by mark # which is feature of end parameter

print('1', '2','3', sep='$', end='@')
print('1', '2','3', end='@', sep='$')
print('hi')
print('bye')
#the default end parameter at line 14 is end='\n' thats why there is
#line break in output