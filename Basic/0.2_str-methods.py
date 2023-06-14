
#*** S T R   M E T H O D S ***

#^ C A P I T A L I Z E
# capitalize(): Converts the first character of the string to capital letter
challange = 'thirty days of python'
print(challange.capitalize()) # 'Thirty days of python'

#^ count() 
# returns occurrences of substring in string
challange = 'thirty days of python'
print(challange.count('y')) # 3
print(challange.count('y', 7, 14)) # 1
print(challange.count('th')) # 2

#^endswith(): Checks if a string ends with a specified ending
challange = 'thirty days of python'
print(challange.endswith('on')) # True
print(challange.endswith('tion')) # False

#^expandtabs(): Replaces tab character with spaces, 
# default tab size is 8. It takes tab size argument
challange = 'thirty\tdays\tof\tpython'
print(challange.expandtabs()) # 8tabs
print(challange.expandtabs(15))  # 'thirty    days      of        python'

#^ find() Returns the index of the first occurrence of a substring, if not found returns -1
challange = 'thirty days of python'
print(challange.find('y')) # 16
print(challange.find('th')) # 17

#^format(): formats string into a nicer output
fst_name = 'Paco'
last_name = 'Hdez'
age = 30
job = "Developer"
country = 'Mexico'

sentence = 'I am {} {}. I am {} years old. I am a {}. I live in {}'.format(fst_name, last_name, age, job, country)
print(sentence)

#^isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False