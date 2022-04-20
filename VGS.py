from abc import ABC, abstractmethod
from ast import Str

class Vigi_Senado(ABC):
    @abstractmethod
    def expandirInfo():
        ...
    
    def Buscar():
        ...
    
    def Comparar():
        ...

class Senado():
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
    
    
class Congresista(Vigi_Senado, Data):
    def _init_(self, Nombre, PartidoP, 
    curul, correo, Data, nVotos):
        self.Nombre = Nombre
        self.PartidoP = PartidoP
        self.curul = curul
        self.correo = correo 
        self.Data = Data
        self.nVotos = nVotos
    
    def expandirInfo():
        ...
        
    def Buscar():
        ...
        

class Partido(Vigi_Senado, Data):
    def _init_(self, nSenadores, nombre, nVotos, Data, Congresista):
        self.nSenadores = nSenadores
        self.nombre = nombre
        self.nVotos = nVotos
        self.Data = Data
        self.Congresista = Congresista

    def expandirInfo():
        ...
        
    def Buscar():
        ...
