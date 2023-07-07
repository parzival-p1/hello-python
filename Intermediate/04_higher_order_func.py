
###*** ***  HIGH  ORDER  FUNCTIONS *** ***###
from functools import reduce

"""_DEFINICION_
Funciones dentro de otra funcion
"""

def sum_one(value):
    '''func that returns a value plus one'''
    return value + 1

def sum_five(value):
    '''func that returns a value plus five'''
    return value + 5


def sum_two_values_and_add_value(fst_val, snd_val, f_sum):
    '''func that sum two values'''
    return f_sum(fst_val + snd_val)

print(sum_two_values_and_add_value(5, 2, sum_one))  # 8
print(sum_two_values_and_add_value(5, 2, sum_five)) # 12

###*** ***  C   L   O   S   U   R   E   S *** ***###
"""_DEFINICION_
Func que retornas funciones dentro de si mismas
(ojo, se mandan a llamar dentro de sí mismas)
"""

def sum_ten(og_value):
    '''Func that returns the sum of ten values'''
    def add(value):
        return value + 10 + og_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))   # 16
print((sum_ten(5))(1))  # 16

###*** *** Built-in  Higher Order Functions *** ***###

numbers = [2, 5, 10, 21, 3, 30]

#^ Map (necesita un conjunto iterable) arg1: func, arg2: conjunto iterable
''' Recorre todos los valores y ejecuta una
    determinada func sobre ellos
'''

def mult_by_two(num):
    return num * 2

print(list(map(mult_by_two, numbers))) # [4, 10, 20, 42]

#^ lambda con map()
print(list(map(lambda num: num * 2, numbers))) # [4, 10, 20, 42]

#^ filter() arg1: func, arg2: conjunto iterable
''' Recorre todos los valores y ejecuta una 
    determinada func sobre ellos y retorna True o False
'''
def filter_greater_than_ten(number):
    '''Return True si el number es mayor que 10'''
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))   # [21, 30]

#^ lambda con filter() este es el metodo más directo
print(list(filter(lambda number: number > 10, numbers))) # [21, 30]

#^ Reduce
''' Opera entre los valores que va recorriendo
y opera con los valores que tiene en cada caso
a medida que recorre un iterable
'''

def sum_two_values(fst_val, snd_val):
    ''' suma dos valores dados '''
    print(fst_val)
    print(snd_val)

    return fst_val + snd_val

print((reduce(sum_two_values, numbers)))  # 71
