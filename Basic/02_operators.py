
###* O P E R A T O R S *####

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 // 4) # floor division
print(10 % 3)
print(2 ** 2)

#^Concatenar
print("Hola " + "Python")
print("Hola " + str(5)) # tipado dinamico
print("Hola " * 5)
print("Hola " * (2 ** 3))

###* OPERADORES COMPARATIVOS *###
''' print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4) '''

###* OPERADORES COMPARATIVOS & STRS *###
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # ordenacion alfabética
print(len("aaaa") >= len("abaa")) # count chars
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

###* OPERADORES LÓGICOS *###
print(3 > 4 and "Hola" > "Python") # &&
print(3 > 4 or "Hola" > "Python")  # ||
print(3 < 4 and "Hola" < "Python") # &&
print(3 < 4 or "Hola" < "Python")  # ||
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not (3 > 4))
#print(3 > 4 not "Hola" > "Python") # !=
