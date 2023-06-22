
###* C O N D I T I O N A L S *###

#& Inicializando if()
my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")
else:
    print("La condición no se cumple")

# 2º if()
my_condition = 5 * 5

if my_condition == 10: # True
    print("Se ejecuta la condición del 2º if")

elif my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 mayor o igual que 20")

print("La ejecución continúa")

my_str = ""

if not my_str:
    print("Mi cadena de texto es vacía")

if my_str == "Mi cadena de texto":
    print("Estás cadenas de texto coinciden")
