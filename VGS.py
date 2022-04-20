from abc import ABC, abstractmethod
from ast import Str

class Vigi_Senado(ABC):
    @abstractmethod
    def expandirInfo():
        pass
    def Buscar():
        pass
    def Comparar():
        pass

class Data():

    pass 

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
        pass
    def Buscar():
        pass    

class Partido(Vigi_Senado, Data):
    def _init_(self, nSenadores, nombre, nVotos, Data, Congresista):
        self.nSenadores = nSenadores
        self.nombre = nombre
        self.nVotos = nVotos
        self.Data = Data
        self.Congresista = Congresista

    def expandirInfo():
        pass
    def Buscar():
        pass
