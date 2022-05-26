import csv

class Vigi_Senado():
    def __init__(self):
        self.SENADO = Lista()
    

    def BuscarP(self, nombre):
        P = self.SENADO.head
        cont = True
        while(P != None and cont):
            if (nombre in P.nombreP):
                cont = False
            else:
                P = P.next
        print(f"Nombre: '{P.nombreP}' Numero de Senadores: {P.nSenadores} Fecha de Fundación: {P.fechaFundacion} Presidente: {P.presidente} Posición: {P.posicion} Eslogan: {P.eslogan}, Porcentaje: {P.porcentaje}")
   
    
    def Comparar():
        ...
    
    def CrearLista(self):
        
        with open("Partidos_Politicos.csv", "r") as archivoPar:
            lector = csv.reader(archivoPar, delimiter=";")
            #Omite el encabezado
            next(lector, None)
            for fila in lector:
                NOMBRE = fila[0]
                FECHAFUNDACION = fila[1]
                PRESIDENTE = fila[2]
                POSICION = fila[3] 
                ESLOGAN = fila[4]
                #Se agregan los partidos
                self.SENADO.insertP(NOMBRE, FECHAFUNDACION,
                PRESIDENTE, POSICION, ESLOGAN, 0, 0)
        archivoPar.close()
        #AgregarSenadores
        with open("Sen_directorio.csv", "r") as archivoCon:
            lector = csv.reader(archivoCon, delimiter=";")
            #Omite el encabezado
            next(lector, None)
            for fila in lector:
                PERIODO = fila[0]
                NOMBRE = fila[1]
                GENERO = fila[2]
                AÑONACIMIENTO = fila[3]
                DEPNACIMIENTO = fila[6]
                CIUDADNACIMIENTO = fila[7] 
                PARTIDOP = fila[8]
                NVOTOS = fila[9]
                CORREO = fila[12]
                REDES = fila[13]
                #Se agrega el senador
                self.SENADO.insertC(NOMBRE, GENERO, AÑONACIMIENTO, CIUDADNACIMIENTO,
                DEPNACIMIENTO, PARTIDOP, PERIODO, NVOTOS, CORREO, REDES)
        archivoCon.close        


class Congresista():
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

        self.next = self
        self.prev = self
        self.child = self


class Partido():
    def __init__(self, nombre, fechaFundacion, presidente,
    posicion, eslogan, nSenadores, porcentaje):
        self.nombreP = nombre
        self.fechaFundacion = fechaFundacion
        self.presidente = presidente
        self.posicion = posicion
        self.eslogan = eslogan
        self.nSenadores = nSenadores
        self.porcentaje = porcentaje

        self.next = self
        self.prev = self
        self.child = self


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        string = ""

        if (self.head == None):
            string += "Lista vacía"
            return string
    
        string += f"CLL list: \n{self.head.nombreP}" # PTR
        P = self.head.next # Segundo nodo despues de PTR
        while(P != None):
            string += f" -> {P.nombreP}"
            P = P.next
        return string

    def insertP(self, nombre, fechaFundacion, presidente,
    posicion, eslogan, nSenadores, porcentaje):

        if(self.head == None):
            self.head = Partido(nombre, fechaFundacion, presidente,
            posicion, eslogan, nSenadores, porcentaje)
            self.tail = self.head
            self.tail.next = None
            self.tail.prev = None
            self.tail.child = None
        else:
            self.tail.next = Partido(nombre, fechaFundacion, presidente,
            posicion, eslogan, nSenadores, porcentaje)
            temp = self.tail
            self.tail = self.tail.next
            self.tail.next = None
            self.tail.prev = temp
            self.tail.child = None

    def insertC(self, nombre, genero, añoNacimiento, ciudadNacimiento,
    depNacimiento, partidoP, periodo, nVotos, correo, redes):

        if(self.head == None):
            print("List is empty")
        else:
            P = self.head
            cont = True
            while ((P.next != None) and (cont)):
                if(P.nombreP == nombre):
                    if(P.child == None):
                        P.child = Congresista(nombre, genero, añoNacimiento,
                        ciudadNacimiento, depNacimiento, partidoP, periodo,
                        nVotos, correo, redes)
                        Q = Q.child
                        Q.child = None
                    else:
                        Q = P.child
                        while (Q.child !=  None):
                            Q = Q.child
                        Q.child = Congresista(nombre, genero, añoNacimiento,
                        ciudadNacimiento, depNacimiento, partidoP, periodo,
                        nVotos, correo, redes)
                        Q = Q.child
                        Q.child = None
                    P.nSenadores = int(int(P.nSenadores) + 1)
                    P.porcentaje = str((int(P.nSenadores) / 106) * 100) + "%"
                    cont = False
                else:
                    P = P.next

vgs = Vigi_Senado()
vgs.CrearLista()
print(vgs.SENADO.__repr__())
vgs.BuscarP("Cambio")
