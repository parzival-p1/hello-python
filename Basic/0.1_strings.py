
#* String format

first_name = 'Paco'
last_name = 'Hdez'
language = 'Python'
formated_string = 'I am {} {}. I learn {}'.format(first_name, last_name, language)
print(formated_string)

#? Strings and numbres
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, pi)
print(formated_string)

#* f-Strings | String Interpolation
"""_summary_
Another new string formatting is strin
interpolation, f-strings. Strings start with
f and we can inject the data in their
corresponding positions.
"""

a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
#* String format

first_name = 'Paco'
last_name = 'Hdez'
language = 'Python'
formated_string = 'I am {} {}. I learn {}'.format(first_name, last_name, language)
print(formated_string)

#? Strings and numbres
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, pi)

print(formated_string)
print('\n')

#*** f-Strings | String Interpolation ***#
"""_summary
Another new string formatting is string
interpolation, f-strings. Strings start with
f and we can inject the data in their
corresponding positions.
"""

a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')

#! formated_string(f'{a} ** {b} = {a ** b}')
print (formated_string) #! formated str is not callable

#*** Python Strings as Sequences of Characters ***#
language = 'Python'
a, b, c, d, e, f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
print('\n')
#^ Accessing Characters in Strings by Index
fst_letter = language[0]
print(fst_letter)

snd_letter = language[1]
print(snd_letter)

trd_letter = language[2]
print(trd_letter)

#? Want to start from the end? #
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

#*** Slicing Python Strings ***
language = 'Python'
fst_three = language[0:3]
print(fst_three) # Pyt

last_three = language[3:6]
print(last_three)

#? Another way
last_three = language[-3:]
print(last_three) # hon

last_three = language[3:]
print(last_three) # hon

#*** Reversing a String ***#
greeting = "Hello World"
print(greeting[::-1]) # !dlroW ,olleH

#^Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto