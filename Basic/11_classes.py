
###*** C  L  A  S  S  E  S ***###

"""_DEFINICION_
Las clases son objetos que sirven para
definir una entidad
"""

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

###& *** Recibiendo params en las classes *** &###

class Person:
    def __init__ (self, name, surname, aka="Sin alias"): # limitacion del lang self es un constructor
        self.name = name
        self.surname = surname
        self.fullname = f"{name} {surname} ({aka})" # Propiedad pública

        #* Private Classes
        self.__name = name          # private property
        self.__surname = surname

    #* Getter
    def get_name (self):
        return self.__name    

    def walk (self):
        print(f"{self.fullname} está caminando")

my_person = Person("Paco", "Hdez")
# my_person  = Person()
print(my_person.name)       # Paco
print(my_person.surname)    # Hdez
print(my_person.fullname)   # Paco Hdez
my_person.walk()            # Paco Hdez Está caminando

#& *** Creando una 2ª persona
my_snd_person = Person("Brais", "Moure")
print(my_snd_person.fullname)  # Brais Moure Sin alias
print(my_person.get_name())   # Brais
my_snd_person.walk()         # Brais Moure Sin alias está caminando

my_snd_person.fullname = "Paco Hdez (Pacool)"
print(my_snd_person.fullname)   # Paco Hdez (Pacool)

my_snd_person.fullname = 333
print(my_snd_person.fullname)   # 333
