import json
from ModuloCliente import *
from ModuloAd import *
from Moduloservicio import *
from ModuloBonificacion import *
from menu import *
## Abrir

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

##########################################################################################33

usuario = {}

def MenuPrincipio ():

    print("----------------------------------------")
    print("----- BIENVENIDOS AL SERVICIO DE--------")
    print("--------------MOVISTAR------------------")
    print("----------------------------------------")
    print("¿Quien eres ?")
    print(" 1- Cliente ")
    print(" 2 - Administrador ")
    print(" 3- Salir ")

    opc = int(input("~~~ :"))

    if opc == 1 :
        menuU ()
        opcu = int(input("~~~ :"))

        if opcu == 1 :
            print("")
        elif opcu == 2 :
            print("")
        elif opcu == 3 :
            print("")







    elif opc == 2 :

        menuadministrador()

        opci = int(input("~~~ :"))

        if opci == 1 :
            AgregarUsuario ()
        elif opci == 2 :
            AgregarProducto()
        elif opci == 3 :
            eliminar ()



    elif opc == 3 :
        bonificacion()




usuario=abrirJSON()


bo = True
while (bo == True) :
    bo = MenuPrincipio()