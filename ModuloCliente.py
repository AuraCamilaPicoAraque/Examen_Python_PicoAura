import json
from ModuloBonificacion import *

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







