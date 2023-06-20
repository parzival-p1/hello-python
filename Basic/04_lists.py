
###* L I S T A S *####
my_list = list()
my_snd_list = [] #~ esto tmbn es una lista

#& Declarar una lista
my_list = list("Hola Python")
my_list = ["Hola Python"]

print(len(my_list))
my_list = [30, 24, 62, 52, 30, 17] # lista de edades
print(type(my_list))           # <class 'list'>
print(len(my_list))            # 5

#&             -4,  -3,   -2,     -1
my_snd_list = [30, 1.60, "Paco", "Hdez"] # Lista con != type
print(type(my_snd_list))       # <class 'list'>
print(type(my_list))           # <class 'list'>

#^ Accediendo a los valores de la lista
print(my_snd_list[0])          # edad = 30-yo
print(my_snd_list[1])          # estatura = 1.60
print(my_snd_list[-1])         # apellido = Hdez
print(my_snd_list[-3])         # estatura = 1.60
print(my_list.count(30))       # 2, elvalue 30 se repita 2 veces
#print(my_snd_list[4])         #! IndexError
#print(my_snd_list[-5])        #! IndexError

age, height, name, surname = my_snd_list # la lista necesita todos los elm
print(name) # Paco

name, height, age, surname = my_snd_list[2], my_snd_list[1], my_snd_list[0], my_snd_list[3]
print(age)

print(my_list + my_snd_list) #? es posible concat 2 listas!
#! error print(my_list - my_snd_list) #? es posible concat 2 listas!

#& Anhadir elementos a la lista
my_snd_list.append("Hackool") # [30, 1.6, 'Paco', 'Hdez', 'Hackool']
print(my_snd_list)

#& Insertar elementos a la lista
my_snd_list.insert(1, "Rojo")
print(my_snd_list) # [30, 'Negro', 1.6, 'Paco', 'Hdez', 'Hackool']

my_snd_list[1] = "Negron"
print(my_snd_list)

#& Eliminar elementos de la lista
my_list.remove(30) #^ encuentra y elimina el elm
print(my_list) # [24, 62, 52, 30, 17]

#& Usando pop
my_list.pop()  # desapila el ultimo elm de la lista
print(my_list) # [24, 62, 52, 30]

#pop en especifico
print(my_list.pop(2)) # 2 = index of the list
print(my_list)        # 52

#& Usando del() (eliminando el nuevo elm)
del my_list[2] #^ elimina el index 2
print(my_list) # [24, 62]

#& Creando nueva lista
new_list = my_list.copy()

#& Usando clear()
my_list.clear() #^ borra la lista entera
print(my_list)  # []
print(new_list) # [24, 62]

#& Usando reverse()
new_list.reverse()
print(new_list) # [62, 24]

#& Usando sort()
new_list.sort() # 
print(new_list) # [24, 62]

#& como hacer sublistas
print(new_list[1:2]) # [62]

#& Tipos dinamicos
#my_list = "Hola Python" #^ esto ya no es una lista
#print(my_list) # Hola Python
#print(type(my_list)) # <class 'str'>
