
###* S E T S *####

"""_Definicion_
    No son una estructura ordenada, 
    es un hash table que no admite elms
    repetidos.
"""

###& Definiendo set()
my_set = set()
my_snd_set = {}
print(type(my_set))     # <class 'set'>
print(type(my_snd_set)) # <class 'dict'>

my_snd_set = {"Paco", "Hdez", 30}
print(type(my_snd_set)) # <class 'set'>

###& Usando len()
print(len(my_snd_set)) # 3

# print(my_snd_set[0]) #! TypeError: 'set' object is not subscriptable

###& usando set.add()
my_snd_set.add("Hackool")
print(my_snd_set)   # {'Hdez', 'Paco', 'Hackool', 30}

#^ set() no admite repetidos
my_snd_set.add("Hackool")
print(my_snd_set)

###& Comprobando que un elm exite en un set
print("Hdez" in my_snd_set) # True
print("Hdz" in my_snd_set)  # False

###& Eliminando datos set.remove()
my_snd_set.remove("Hdez")
print(my_snd_set) # {'Hackool', 30, 'Paco'}

###& Vacia el set, el set.clear()
my_snd_set.clear()
print(len(my_snd_set))  # 0

###& Borrando el set
del my_snd_set


my_set = {"Paco", "Hdez", 30}
my_list = list(my_set)
print(my_list)  # ['Hdez', 'Paco', 30]

my_snd_set = {"C", "JavaScript", "Python"}

###& Uniendo 2 sets set.union()
new_set = my_set.union(my_snd_set)
print(new_set.union(new_set).union(my_set).union({"JavaScript", "#C"})) # {'Paco', 'Python', 'Hdez', 'JavaScript', '#C', 'C', 30}

###& Usando set.difference()
print(new_set.difference(my_set)) # {'C', 'Python', 'JavaScript'}
