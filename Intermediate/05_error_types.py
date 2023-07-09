
###*** ***  T I P O S  E R R O R E S *** ***###

###***! *** SyntaxError *** !***###

# print "Hola comunity!" #! Error
print("Hola comunidad!")

###***! *** NameError *** !***###
language = "Spanish" # Comentar para error
print(language)

###***! *** IndexError *** !***###
my_list = ["Python", "Swift", "Java", "JavaScript", "Java"]
print(my_list[0]) # Python
print(my_list[4]) # Java
print(my_list[-1]) # Java
# print(my_list[5]) # Desc para el Error #! IndexError

###***! *** ModuleNotFoundError *** !***###
# import maths #! No module named 'maths'

###***! *** AttributeError *** !***###
import math
# print(math.PI) #! module 'math' has no attribute 'PI'
print(math.pi)

###***! *** KeyError *** !***###
my_dict = {
    "Nombre" : "Paco",
    "Apellido" : "Hdez",
    "Edad"  : 30,
    1   : "Python"
}

# print(my_dict["Apelido"]) #! KeyError: 'Apelido'
print(my_dict["Apellido"])

###***! *** TypeError *** !***###
# print(my_list["Nombre"]) #! TypeError: list indices must be integers or slices, not str
print(my_list[1]) # Swift

###***! *** ImportError *** !***###
# from math import PI #! ImportError: cannot import name 'PI'
from math import pi
print(pi)

###***! *** ValueError *** !***###
# my_int = int("10 anhos")
my_int = int("10")
# print(type(my_int)) #! ValueError: invalid literal for int() with base 10: '10 anhos' 

###***! *** ZeroDivisionError *** !***###
print(4 / 2) # 2
# print(4 / 0) #! ZeroDivisionError: division by zero 
