from __future__ import unicode_literals
from base64 import encode
import csv
from encodings import utf_8


ListCongresistas = []
class Congresista():
    

    def __init__(self, Periodo, Nombre, Genero, AñoNacimiento, CiudadNacimiento, DepNacimiento, Partido, nVotos, correo):
        self.Nombre = Nombre
        self.Genero = Genero
        self.AñoNacimiento = AñoNacimiento
        self.CiudadNacimiento = CiudadNacimiento
        self.AñoNacimiento = DepNacimiento
        self.PartidoP = Partido
        self.Periodo = Periodo
        self.correo = correo 
        self.nVotos = nVotos     
    
    def mostrarInfo(self):
        ##print(self.Nombre)
        ##print(self.PartidoP)
        ##print(self.curul)
        ##print(self.correo)
        ##print(self.nVotos)
        ...
    
    def expandirInfo(self):
        #dt.imprimirCongresista() 
        ...

    def search():
        Senador = input("Ingrese el senador a buscar: ")
        with open("Sen_directorio.csv", "r") as archivo:
            lector = csv.reader(archivo, delimiter=";")
            #Omite el encabezado
            next(lector, None)
            for fila in lector:
                if(Senador in fila[1]):
                    Periodo = fila[0]
                    Nombre = fila[1]
                    Genero = fila[2]
                    AñoNacimiento = fila[3] 
                    CiudadNacimiento = fila[6]
                    DepNacimiento = fila[5]
                    Partido = fila[7]
                    nVotos = fila[8]
                    correo = fila[11]
                    Sen = Congresista(Periodo,Nombre,Genero,AñoNacimiento,CiudadNacimiento,DepNacimiento,Partido,nVotos,correo)
                    #print(Periodo,Nombre,Genero,AñoNacimiento,CiudadNacimiento,DepNacimiento,Partido,nVotos,correo)
                    print(Sen.Periodo, "/", Sen.Nombre, "/", Sen.PartidoP)
                
    #Congresista(Periodo,Nombre,Genero,AñoNacimiento,CiudadNacimiento,DepNacimiento,Partido,nVotos,correo)
    #ListCongresistas.append(Congresista)

Congresista.search()





