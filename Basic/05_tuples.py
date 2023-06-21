
###* T U P L E S *####

"""_Definicion_
    Conjunto de valores inmutables
"""

###& Definiendo tuples
my_tuple = tuple()  # manera 1
my_snd_tuple = (35, 60, 30)   # manera 2

my_tuple = (30, 1.6, "Paco", "Hdez", "Paco")
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0])  # 30
print(my_tuple[-1]) # Paco
# print(my_tuple[4])  # IndexError
# print(my_tuple[-6]) # IndexError

###& Usando count()
print(my_tuple.count("Paco")) # 2
print(my_tuple.index("Hdez")) # 3
print(my_tuple.index("Paco")) # 2 se queda con el 1er index


###! Los valores en las tuples son inmutables
# my_tuple[1] = 1.8 #! 'tuple' object does not support item assignment
# print(my_tuple)

sum_tuple = my_tuple + my_snd_tuple
print(sum_tuple) # (30, 1.6, 'Paco', 'Hdez', 'Paco', 35, 60, 30)
print(sum_tuple[3:6]) # ('Hdez', 'Paco', 35)

my_tuple = list(my_tuple)
print(type(my_tuple))       # <class 'list'>

###& De tuple a list
my_tuple[4] = "Hackool"
my_tuple.insert(1, "Azul")
print(my_tuple) # [30, 'Azul', 1.6, 'Paco', 'Hdez', 'Hackool']

###& de list() a tuple()
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple)) # <class 'tuple'>

###& del ()
#! del my_tuple Error!
# print(my_tuple)
