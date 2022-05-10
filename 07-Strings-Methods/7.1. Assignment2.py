# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).

def fancy_cleanup(text):
    return text.strip().replace('g', 'z').replace(' ', '!')
print(fancy_cleanup('   gan esh  '))
print(fancy_cleanup('     whitespace    '))
print(fancy_cleanup('grade'))