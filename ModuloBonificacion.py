import json
from ModuloCliente import *
from Moduloservicio import *


### abrir -----------------------------------------------------------------------------------

def abrirJSON():
    abrir={}
    with open ("./Usuarios.json", "r") as openfile :
        abrir=json.load (openfile)
    return abrir

def abrirREPORTJSON():
    abrir={}
    with open ("./reportes.json", "r") as openfile :
        abrir=json.load (openfile)
    return abrir


def abrirclienteJSON():
    abrir={}
    with open ("./clientes.json", "r") as openfile :
        abrir=json.load (openfile)
    return abrir


### guardar--------------------------------------------------------------------------------------

def guardarJSON(abrir):
    with open("./Usuarios.json",'w') as outFile:
        json.dump(abrir,outFile)



def guardarREPORTJSON(abrir):
    with open("./reportes.json",'w') as outFile:
        json.dump(abrir,outFile)


def guardarclienteJSON(abrir):
    with open("./clientes.json",'w') as outFile:
        json.dump(abrir,outFile)


############################################################################################################################


def bonificacion():
    abrir = abrirJSON ()
    for i in range (len(abrir["clientes"])):
        print ("Usted") , abrir["clientes"]["nombre"] , abrir["clientes"]["Categoria"]


def lealtad ():
    abrir =abrirJSON ()
    abrir2 = abrirclienteJSON ()
    for i in range (len(abrir("clientes"))):
        if abrir ["clientes"][i]["Categoria"]["leal"] == 0 :

            abrir2["leales"].append (abrir["nombre"][i])