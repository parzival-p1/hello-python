
###* F  U  N  C  T  I  O  N  S *###

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (fst_value, snd_value):
    print(fst_value + snd_value)    # 12

sum_two_values(5, 7)            # 12
sum_two_values(5473, 71231)     # 76704
sum_two_values("5", "7")        # 57 concat !suma
sum_two_values(1.4, 5.2)        # 6.6

###& *** Retornado parametros *** &###
def sum_values_with_return(fst_value, snd_value):
    my_sum = fst_value + snd_value
    return my_sum

# my_result = sum_two_values(1.4, 5.2)
# print(my_result)

my_result = sum_values_with_return(10, 5)
print(my_result) # 15

###& *** Parametros  *** &###
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(name = "Paco", surname = "Hdez")  # Paco Hdez

###& *** Parametros por defecto  *** &###
def print_name_w_default(name, surname, aka="el sin alias"): # valor por default: el sin alias
    print(f"{name} {surname} {aka}")

print_name_w_default("Paco", "Hdez")
print_name_w_default("Paco", "Hdez", "Pacool")

###& *** Parametros por separado *** &###
def print_upper_txts(*texts): # esto es un ptr?
    print(type(texts))         # <class 'tuple'>
    for text in texts:
        print(text.upper())

print_upper_txts("Hola", "Python", "Hackool") # ('Hola', 'Python', 'Hackool')
print_upper_txts("Hola") # ('Hola')
