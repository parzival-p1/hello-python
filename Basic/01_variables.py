
#*** Variables ***

my_str_variable = "My string variable" #camelCase
print(my_str_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_var = str(my_int_variable)
print(my_int_to_str_var)
print(type(my_int_to_str_var)) # <class 'str'>

my_bool_variable = True
print(my_bool_variable)

print(my_str_variable, my_int_variable, my_bool_variable)

#^Concatenacion de var en un print
print(type(print("Mi cadena de texto"))) # Tipo 'NoneType'
print("Este es el valor de: ", my_bool_variable)

#^len() function
print(len(my_str_variable))

#^Variables en una sola linea
name, surname, alias, age = "Paco", "Hdez", "Pacool", "30" # es posible mezclar tipos de datos
print("Me llamo: ", name, surname, "Mi edad es: ", age, "Y  mi alias es:", alias)


