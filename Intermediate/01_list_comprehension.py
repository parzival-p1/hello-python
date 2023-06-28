
###***  L I S T  C O M P R E H E N S I O N ***###
"""_Definicion_
Crea listas en base a listas que ya se tienen
Son listas comprimidas
"""

###^ *** D e f i n i c i o n *** ^###
my_og_list = [1, 2, 3, 4, 5, 6, 7]
print(my_og_list) # [0, 1, 2, 3, 4, 5, 6, 7]

#*** list comprehension ***#
my_range = range(8)
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7]

# Guardando un valor extra
my_list = [i + 1 for i in range(8)]
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# Guardando el doble de cada valor
my_list = [i * 2 for i in range(8)]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

# Guardando el valor mult por si mismo
my_list = [i * i for i in range(8)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49]

# Funciones y list comprohension
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)  # [5, 6, 7, 8, 9, 10, 11, 12]
