from abc import ABC, abstractmethod
from ast import Str
import Data as dt
import Node

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
    


class Congresista(Vigi_Senado, dt, Node):
    def __init__(self, nombre, genero, añoNacimiento, ciudadNacimiento,
    depNacimiento, partidoP, periodo, nVotos, correo, redes):
        self.Nombre = nombre
        self.Genero = genero
        self.AñoNacimiento = añoNacimiento
        self.CiudadNacimiento = ciudadNacimiento
        self.DepNacimiento = depNacimiento
        self.PartidoP = partidoP
        self.Periodo = periodo
        self.nVotos = nVotos
        self.correo = correo 
        self.redes = redes

class Partido(Vigi_Senado, Node):
    def __init__(self, nombre, fechaFundacion, presidente, nSenadores,
    porcentaje, posicion, eslogan):
        self.nombre = nombre
        self.fechaFundacion = fechaFundacion
        self.presidente = presidente
        self.nSenadores = nSenadores
        self.porcentaje = porcentaje
        self.posicion = posicion
        self.eslogan = eslogan

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        string = ""

        if (self.head == None):
            string += "Lista vacía"
            return string
    
        string += f"CLL list: \n{self.head.data}" # PTR
        P = self.head.next # Segundo nodo despues de PTR
        while(P != self.head):
            string += f" -> {P.data}"
            P = P.next
        return string
    def insertP(self, value):

        if(self.head == None):
            self.head = Partido(value)
            self.tail = self.head
            self.tail.next = None
            self.tail.child = None
        else:
            self.tail.next = Partido(value)
            self.tail = self.tail.next
            self.tail.next = None
            self.tail.child = None

    def insertC(self, value):

        if(self.head == None):
            print("List is empty")
        else:
            P = self.head
            cont = True
            while (P.next != None & cont):
                if(P.data == value):
                    if(P.child == None):
                        P.child = Congresista(value)
                        P = P.child
                        P.child = None
                    else:
                        while (P.child !=  None):
                            P = P.child
                        P.child = Congresista(value)
                        P = P.child
                        P.child = None
                    cont = False
                else:
                    P = P.next
