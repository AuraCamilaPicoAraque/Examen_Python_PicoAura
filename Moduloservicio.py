import json
from ModuloCliente import *

### abrir

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

### guardar

def guardarJSON(abrir):
    with open("./Usuarios.json",'w') as outFile:
        json.dump(abrir,outFile)



def guardarREPORTJSON(abrir):
    with open("./reportes.json",'w') as outFile:
        json.dump(abrir,outFile)




def AgregarProducto():

    abrir = abrirREPORTJSON()

    print("Ingrese el producto")
    pro = input("~~~ : ")
    print("Ingrese el precio del producto de cada mes")
    mes = input("~~~ : ")

    print("Se registro el dia de hoy un nuevo producto")

    abrir["informe"]["PRODUCTOS"].append({  "Producto" : pro ,
                                "precio cada mes" : mes ,
                                "descuento" : "" ,
    })
    guardarREPORTJSON (abrir)