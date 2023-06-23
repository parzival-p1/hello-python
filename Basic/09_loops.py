
###* L  O  O  P  S *###

"""_DEFINICION_
"""

###&  W H I L E &###
condition = 0

while condition < 10:
    print(condition) # o infinito
    condition += 2  # condition++

else: # else es opcional
    print("Mi condición es mmayor o igual que 10")

print("La ejecución continiúa")

while condition < 20:
    condition += 1
    if condition == 15:
        print("Mi condición es 15, se detiene la ejecución")
        break
    print(condition)

print("La ejecucion continua")

###&  F  O  R   &###
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = [35, 1.60, "Paco", "Hdez", "Paco"]
for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}
for element in my_set:
    print(element)

my_dict = {
    "Nombre" : "Paco",
    "Apellido" : "Hdez",
    "Edad" : 30,
    1: "Python"
}
for element in my_dict:
    print(element) # Imprime solo keys no  values
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El loop for para mi diccionario ha finalizado")
