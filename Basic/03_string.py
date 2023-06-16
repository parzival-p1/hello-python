
###* S T R I N G S *####

my_string = "My string"
my_second_string = 'My second string'

print(len(my_string))           # 9
print(len(my_second_string))    # 16

#& Concatenar
print(my_string + " " + my_second_string)

#& Con salto de linea
my_new_line_str = "Este es un String\ncon salto de linea"
print(my_new_line_str)

#& Con tabulaciones
my_tab_str = "\tEste es un String con tabulacion"
print(my_tab_str)

#& Como escapar Strings
my_scape_str = "\\tEste es un String \\n escapado"
print(my_scape_str)

#& Como formatear Strings
name, surname, age = "Paco", "Hdez", 30

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #* format
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))      #* template strings
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #* inferencia de datos

#& Como usar f-Strings
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#& Desempaquetado de chars
language = "python3"
a, b, c, d, e, f, g = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#& Division
lang_slice = language[1:3]
print(lang_slice) # yt

lang_slice = language[1:]
print(lang_slice)

lang_slice = language[-2]
print(lang_slice)

lang_slice = language[0:6:2] # Pto
print(lang_slice)

#& Reverse a string
reversed_lang = language[::-1]
print(reversed_lang) # 3nohtyP

#& Funciones
print(language.capitalize())      # P 1ª letra en MAYUS
print(language.upper())           # todas las letras en MAYUS
print(language.count('t'))        # 1 solo hay una 't'
print(language.isnumeric())       # False python3 no es un num
print("1".isnumeric())            # True
print(language.lower())           # todas en minus
print(language.upper().isupper()) # True PYTHON3 esta en MAYUS
print(language.lower().isupper()) # False pyhton3 NO esta en MAYUS
print(language.startswith("py"))  # True
