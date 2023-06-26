
###*** M  O  D  U  L  E  S ***###

"""_MODULOS_
Concepto similar a librerías
Serie de operaciones y utilidades que resuelvan
problemas con alguna relacion
"""

###& *** Accediendo a la func del modulo *** &###
import my_module

my_module.sum_value(5, 3, 1)         # 9
my_module.print_value("Hola Python!")

from my_module import sum_value, print_value

sum_value(5, 6, 1)               # 12
print_value("Hola Python 🐍")   # Hola Python 🐍

###& *** Importando modulos de Python *** &###
import math
# import random

print(math.pi)          # 3.141592653589793
print(math.pow(2, 8))   # 256.0

###& *** Dando valores especificos a las func() *** &###
from math import pi as PI_VALUE
print(PI_VALUE)         # 3.141592653589793
