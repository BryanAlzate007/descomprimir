import os
import glob

print("descomprimir archivos con python")
ruta = r'home/bryan-ubuntu/Documentos/usb'

extencion = '*.zip'
listaDeArchivos = glob.glob(ruta + os.sep + extencion)

print(listaDeArchivos)