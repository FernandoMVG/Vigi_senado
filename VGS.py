from abc import ABC, abstractmethod
from ast import Str
import Data as dt

class Vigi_Senado(ABC):
    @abstractmethod
    def expandirInfo():
        ...
    
    @abstractmethod
    def Buscar():
        ...
    
    @abstractmethod
    def Comparar():
        ...

class Senado(Vigi_Senado):
    def __init__(self, curul: list(), Partido, Congresista):
        self.curul = curul
        
    def buscar(self, Data, Partido, Senador):
        ...

    def comparar(self, Data, Senador):
        ...
    
class Data():
    def __init__(self, titulo, experiencia, proyectos, votaciones):
       self.titulo = titulo
       self.experiencia = experiencia
       self.proyectos = proyectos
       self.votaciones = votaciones
    
    
class Congresista(Vigi_Senado, dt):
    def __init__(self, Nombre, PartidoP, 
    curul, correo, Data, nVotos):
        self.Nombre = Nombre
        self.PartidoP = PartidoP
        self.curul = curul
        self.correo = correo 
        self.Data = Data
        self.nVotos = nVotos

    def mostrarInfo(self):
        print(self.Nombre)
        print(self.PartidoP)
        print(self.curul)
        print(self.correo)
        print(self.nVotos)
    
    def expandirInfo(self):
        dt.imprimirCongresista()
        

class Partido(Vigi_Senado):
    def __init__(self, nSenadores, nombre, nVotos, Data, Congresista):
        self.nSenadores = nSenadores
        self.nombre = nombre
        self.nVotos = nVotos
        self.Data = Data
        self.Congresista = Congresista
    
    def mostrarInfo(self):
        print(self.nombre)
        print(self.nSenadores)
        print(self.nVotos)

    def expandirInfo(self):
        dt.imprimirPartido()
        
    def Buscar():
        ...
