
###*** ***  C H A L L A N G E S *** ***###
"""_00-FIZZ-BUZZ_
Escribe un programa que muestre por consola (con un print) 
los números de 1 a 100 (ambos incluidos y con un salto de línea entre 
cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz():
    for idx in range (1, 101):
        if idx % 3 == 0 and idx % 5 == 0:
            print("fizzbuzz")
        elif idx % 3 == 0:
            print("fizz")
        elif idx % 5 == 0:
            print("buzz")
        else:
            print(idx)
fizz_buzz()

"""_01-ES_UN_ANAGRAMA?_
Escribe una función que reciba dos palabras (String) y 
retorne verdadero o falso (Boolean) según sean 
o no anagramas.
 * Un Anagrama consiste en formar una palabra 
    reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Nacionalista", "Altisonancia"))

"""_03_FIBONACCI_
Escribe un programa que imprima los 50 primeros 
números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión 
    de números en la que el siguiente siempre es 
    la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13 ...
"""
def succ_fibonacci():

    prev = 0
    next = 1

    for idx in range (0, 50):
        print(prev)
        fib = prev + next # formula clave
        prev = next
        next = fib

succ_fibonacci()

"""_04_Es primo?_
* Escribe un programa que se encargue de comprobar 
si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():

    for num in range(1, 101):

        if num >= 2:

            is_div = False

            for idx in range(2, num):
                if num % idx == 0:
                    is_div = True
                    break

            if not is_div:
                print(num)

is_prime()
