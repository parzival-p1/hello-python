import os
###*** ***  F I L E  H A N D L I N G *** ***###

#^ open()   .txt file
txt_file = open("Intermediate/files/my_file.txt", "w+") # read & write

#^ .txt file
#txt_file.write("Mi nombre es Paco\nMi apellido es Hdez\nTengo 30 años\nY mi lengauge favorito es C\n")

#^ .txt file readlines()
#print(txt_file.read())
print(txt_file.read(23))
print(txt_file.readline()) # Mi Nombre es Francisco
print(txt_file.readline()) # Mi Nombre es Francisco

#^ print() una sola línea
for line in txt_file.readlines():
    print(line) # imprime todo el txt del file

txt_file.write("\nTambién me gusta python 🐍") # Escribir en una nueva linea
print(txt_file.readline())

#^ close() the file
txt_file.close()

#^ Agregar nueva línea
with open("Intermediate/files/my_file.txt", "a") as my_snd_file:
    my_snd_file.write("\nY C++")

#! remove() el archivo
# os.remove("Intermediate/files/my_file.txt")

###*** ***  .json file handling *** ***###
import json

#^ open() .json
json_file = open("Intermediate/files/my_file.json", "w+")

json_test = {
    "name" : "Paco",
    "surname" : "Hdez",
    "age" : 30,
    "langs": ["Python", "C", "C++", "Java", "JavaScript"],
    "website" : "https://pacool.com"
}

json.dump(json_test, json_file, indent = 4)

#^ close file()
json_file.close()

with open("Intermediate/files/my_file.json") as my_snd_file:
    for line in my_snd_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/files/my_file.json"))
print(json_dict)
print(type(json_dict))  # <class 'dict'>
print(json_dict["name"]) # Paco
print(json_dict)

###*** *** .csv file handling *** ***###
import csv

#^ Step 1.  open() .csv
csv_file = open("Intermediate/files/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "lang", "website"])
csv_writer.writerow(["Paco", "Hdez", 30, "Python, C", "https://pacool.com" ])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

#^ Step 2.  close() .csv
csv_file.close()

#^ Step 3.  with open() .csv
with open("Intermediate/files/my_file.my_file.csv") as my_snd_file:
    for line in my_snd_file.readlines():
        print(line)

###*** *** .xlsx file handling *** ***###
# import xlrd #^ debe instalarse el modulo

###*** ***  .xml file handling *** ***###
import xml
