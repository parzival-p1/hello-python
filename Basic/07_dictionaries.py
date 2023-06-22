
###* D I C T I O N A R I E S *###
"""_Definicion_
Lo que hay detrás son los hash tables
Almacena datos de tipo: clave - valor
"""

#& Inicializando dictionaries()
my_dict = dict()
my_snd_dict = {}

print(type(my_dict))     # <class 'dict'>
print(type(my_snd_dict)) # <class 'dict'>

#& Definiendo dictionaries()
my_snd_dict = {
    #* Key   #* Value
    "Nombre" : "Paco",
    "Apellidos" : "Hdez",
    "Edad" : 30,
    1 : "Python"
}

my_dict = {
    #* Key   #* Value
    "Nombre" : "Paco",
    "Apellidos" : "Hdez",
    "Edad" : 30,
    "Lang" : {"Python", "Swift", "Kotlin"}, # set
    1: 1.60
}
print(my_dict)
print(my_snd_dict)

#& Elementos de los dict()
print(len(my_snd_dict))    # 4 elementos
print(len(my_dict))        # 5 elementos

#& Accediendo al dict()
print(my_dict["Nombre"]) # Paco

#& Asignando valores al dict()
my_dict["Nombre"] = "Isco"
print(my_dict["Nombre"]) # Isco

print(my_dict[1]) # 1.6

#& Anhadiendo valores al dict()
my_dict["Calle"] = "Calle Escuela"
print(my_dict)

#& Removiendo elementos
del my_dict["Calle"]
print(my_dict) 

#& Comprobando si existe un elm en el dict()
print("Apellidos" in my_dict) # True 
print("Apellido" in my_dict)  # False : busca por key not value
print("Isco" in my_dict["Nombre"]) # True : comprobando el valor accediendo al key

#& Usando los built-inn methods
print(my_dict.items())       # return keys & values
print(my_dict.keys())       # return all the keys
print(my_dict.values)      # return all the values

#& Usando dict.fromkeys() Crea un nuevo dict
new_dict = dict.fromkeys(("Nombre", 1)) # Crea dict sin valores
print(new_dict) # {'Nombre': None, 1: None}

# Anhadiendo keys & values
new_dict["Nombre"] = "Pacool"
new_dict[1] = 1993
print(new_dict)

#& Creando una lista con dict.fromkeys()
my_list = ["Nombre", 1, "Piso"]

new_dict = dict.fromkeys((my_list))
print(new_dict) # {'Nombre': None, 1: None, 'Piso': None}
new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((new_dict)) # {'Nommbre': None, 1: None, 'Piso': None}

#& Crear nuevo dict() copiando otro
new_dict = dict.fromkeys((my_dict))
print((new_dict)) # Crea un nuevo dict sin eliminar las keys contenidas
# {'Nombre': None, 'Apellidos': None, 'Edad': None, 'Lang': None, 1: None}

new_dict = dict.fromkeys(new_dict, "HackoolDev")
print((new_dict)) # Added ("HackoolDev") a todos los values

#& Accediendo a los values
print(new_dict.values()) # dict_values data type
print(list(new_dict))   # get only keys ['Nombre', 'Apellidos', 'Edad', 'Lang', 1]
print(tuple(new_dict)) # get only keys ('Nombre', 'Apellidos', 'Edad', 'Lang', 1)
print(set(new_dict))  # get only keys {'Edad', 1, 'Apellidos', 'Lang', 'Nombre'}
