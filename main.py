import os
import glob
from zipfile import ZipFile

print("descomprimir archivos con python")
ruta = r'C:\Users\USER2021\BROWNFIELD'

extencion = '*.zip'
print(extencion)
listaDeArchivos = glob.glob(ruta + os.sep + extencion)

print(listaDeArchivos)

for i in range(0,len(listaDeArchivos)):
     with ZipFile(file = listaDeArchivos[i], mode = "r", allowZip64=True) as file:
        listaDeArchivos[i] = file.open(name = file.namelist()[0], mode = "r")
        print(listaDeArchivos[i].read())
        listaDeArchivos[i].close()

        navegacion = "C:\\Users\\USER2021\\BROWNFIELD"
        print("Descomprimiendo")
        file.extractall(path = navegacion)
        print("archivo descomprimido")