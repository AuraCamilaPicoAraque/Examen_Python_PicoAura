import json
from ModuloCliente import *

### abrir

def abrirJSON():
    abrir={}
    with open ("./Usuarios.json", "r") as openfile :
        abrir=json.load (openfile)
    return abrir

def abrirJSON():
    abrir={}
    with open ("./reportes.json", "r") as openfile :
        abrir=json.load (openfile)
    return abrir

### guardar

def guardarJSON(abrir):
    with open("./Usuarios.json",'w') as outFile:
        json.dump(abrir,outFile)



def guardarJSON(abrir):
    with open("./reportes.json",'w') as outFile:
        json.dump(abrir,outFile)



###################################################################################

def AgregarUsuario ():

    abrir = abrirJSON()

    print("Ingrese el nombre del usuario")
    nom = input("~~~ : ")
    print("Ingrese la direccion del usuario")
    dire = input("~~~ : ")
    print("Ingrese el telefono del usuario")
    tel = input("~~~ : ")
    print("Se registro el dia de hoy como nuevo usuario")

    abrir["clientes"].append({  "nombre" : nom ,
                                "direccion" : dire ,
                                "telefono" : tel ,

                                "Categoria" :{

                                    "nuevo" : "0" ,
                                    "regular" : "" ,
                                    "leal" : ""
                                }
    })
    guardarJSON (abrir)






