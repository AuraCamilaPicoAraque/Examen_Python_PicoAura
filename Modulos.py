
### abrir

def abrirJSON():
    abrir = {}
    with open ("./nn", "r") as openfile :
        abrir = json.load (openfile)


def guardarJSON(abrir):
    with open("./nn", "w") as outfile :
        json.dump (abrir , outfile , index=4 , ensure_ascii = False) 