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




def eliminar ():
    abrir = abrirJSON ()
    for i in range (len(abrir["clientes"])):
        print("Usuarios #" , i + 1 , abrir["clientes"][i]["nombre"])

        eliminar = input("¿A quien deseas eliminar?")
        for i in range (len(abrir["clientes"])):
            if abrir["clientes"][i]["nombre"] == eliminar :
                del (abrir["clientes"][i])
                guardarJSON






