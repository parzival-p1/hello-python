
###*** E  X  C  E  P  T  I  O  N  S ***###
"""_DEFINICION_
Manejor de errores con excpetions
Mecanismo que puede suceder
"""

numOne, numTwo = 5, 1
numTwo = "1"

###* *** Diferencia con if / else *** *###

if type(numTwo) == int:
    print(numOne + numTwo)      # 6
else:
    print("No se cumple la condition")

###* *** try, except, else, finally *** *###
try:
    print(numOne + numTwo)
    print("No se ha producdio error alguno")
except TypeError:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

###^ try, except, else
else:
    # Se ejecuta si nno se produce una excepcion
    print("La ejeución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejeución continúa")

###* *** Exceptions por tipo *** *###

try:
    print(numOne + numTwo)
    print("No se ha producdio error alguno")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

###* *** Captura de la info de la exepcion *** *###

try:
    print(numOne + numTwo)
    print("No se ha producdio error alguno")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
