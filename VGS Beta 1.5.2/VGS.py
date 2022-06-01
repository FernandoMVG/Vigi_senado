##Beta 1.5.2

import csv
import os

class Vigi_Senado():
    def __init__(self):
        self.SENADO = Lista()

    def BuscarP(self, nombre):
        P = self.SENADO.head
        cont = True
        while(P != None and cont):
            if (nombre.lower() in P.nombreP.lower()):
                cont = False
            else:
                P = P.next
        if(P == None):
            print("No existe este partido")
        else:
            print(f"Nombre: {P.nombreP} \nNumero de Senadores: {P.nSenadores} \nFecha de Fundación: ", 
            f"{P.fechaFundacion}  \nPresidente:  {P.presidente}  \nPosición:  {P.posicion}",
            f" \nEslogan:  {P.eslogan}  \nPorcentaje:  {P.porcentaje}")
            return P.nombreP
    
    def BuscarC(self, nombre, partido):
        P = self.SENADO.head
        cont = True
        encontrado = False
        i = 0
        if (partido == None):
            while(P.next != None and (not encontrado)):
                Q = P.child
                while (Q != None and cont):
                    if(nombre.lower() in Q.Nombre.lower()):
                        print(f"Nombre: {Q.Nombre} \nGénero: {Q.Genero} \nAño de nacimiento: ", 
                            f"{Q.AñoNacimiento}  \nCiudad de Nacimiento:  {Q.CiudadNacimiento}",
                            f"\nDepartamento de nacimiento:  {Q.DepNacimiento} \nPartido:  {Q.PartidoP}",
                            f"\nPeriodo:  {Q.Periodo}  \nNúmero de votos: {Q.nVotos}",
                            f"  \nCorreo: {Q.correo}  \nRedes: {Q.redes}") 
                        Q = Q.child
                        i = 1
                        encontrado = True
                    else:
                        Q = Q.child
                if(Q == None):
                    P = P.next
            if (i == 0):
                print("No se encontraron senadores con este nombre")
        else:
            while((P.next != None) and (cont)):
                if(P.nombreP.lower() == partido.lower()):
                    cont = False
                    Q = P.child
                    while (Q != None):
                        
                        if(nombre.lower() in Q.Nombre.lower()):
                            print(f"Nombre: {Q.Nombre} \nGénero: {Q.Genero} \nAño de nacimiento: ", 
                            f"{Q.AñoNacimiento}  \nCiudad de Nacimiento:  {Q.CiudadNacimiento}",
                            f"\nDepartamento de nacimiento:  {Q.DepNacimiento} \nPartido:  {Q.PartidoP}",
                            f"\nPeriodo:  {Q.Periodo}  \nNúmero de votos: {Q.nVotos}",
                            f"  \nCorreo: {Q.correo}  \nRedes: {Q.redes}")
                            Q = Q.child
                            i = 1
                        else:
                            Q = Q.child
                else:
                    P = P.next
            if (i == 0):
                print("No se encontraron senadores con este nombre dentro de este partido",
                "pruebe buscando todos los senadores (Opción 2 luego Opción 1")
        x = input("Ingrese cualquier tecla para volver: ")
        
    def MostrarPartidos(self):
        P = self.SENADO.head
        i = 1
        while (P != None):
            print(f"{i}: {P.nombreP}")
            P = P.next
            i += 1
        x = input("Ingrese cualquier tecla para volver: ")
    
    def MostrarSenadores(self, Partido):
        P = self.SENADO.head
        i = 1
        encontrado = False
        if (Partido == None):
            while (P != None):
                Q = P.child
                while (Q != None):
                    print(f"{i}: {Q.Nombre}\n\tPartido: {Q.PartidoP}\n")
                    Q = Q.child
                    i += 1
                P = P.next
        else:
            while (P != None and (not encontrado)):
                if (P.nombreP == Partido):
                    Q = P.child
                    while (Q != None):
                        print(f"{i}: {Q.Nombre}")
                        Q = Q.child
                        i += 1
                    encontrado = True
                else:
                    P = P.next
        x = input("Ingrese cualquier tecla para volver: ")

    def Comparar():
        ...
    
    def CrearLista(self):
        with open("PP_directorio.csv", "r") as archivoPar:
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
                DEPNACIMIENTO = fila[5]
                CIUDADNACIMIENTO = fila[6] 
                PARTIDOP = fila[7]
                NVOTOS = fila[8]
                CORREO = fila[11]
                REDES = fila[12]
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
            while ((P != None) and (cont)):
                if(P.nombreP == partidoP):
                    Q = P
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
                    P.nSenadores += 1
                    P.porcentaje = str((float(P.nSenadores) / 106) * 100) + "%"
                    cont = False
                else:
                    P = P.next


vgs = Vigi_Senado()
vgs.CrearLista()
os.system('cls')

def pedirOP():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Selecciona una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opción válida')
     
    return num

salir = False
op = 0

#Menú
while not salir:
    print("""Bienvenido a Vigi-Senado.
    
    Selecciona una de las siguientes apartados: 
    1: Partidos
    2: Senadores
    3: Salir 
    """)
    op = pedirOP()

    ##Apartado de Partidos
    os.system('cls')
    if op == 1:
        print("""Estas en la sección de Partidos Políticos. Estas son las acciones""",
        """que puedes hacer:
        1: Buscar Partido especifico
        2: Mostrar Todos los Partidos Politicos
        3: Volver al menu Pricnipal 
        """)
        opP = pedirOP()
        volver = False
        while not volver:
            ###Sub-menú Sección Partidos: Buscar PP especifico
            if opP == 1:
                nombreP = input("Ingrese Nombre del Partido: ")
                nombreP = vgs.BuscarP(nombreP)

                #### Más acciones:
                print("------------------------------------------------")
                print("""\nPuedes realizar estas acciones:""", 
                """
                1: Mostrar Lista de Senadores
                2: Volver al menú principal
                 """)
                oppi = pedirOP()
                regresar = False
                while not regresar:
                    #Más acciones: Op 1
                    if oppi == 1:
                        ## Metodo que imprima Lista de senadores
                        vgs.MostrarSenadores(nombreP)
                        break
                        
                    elif oppi == 2:
                        os.system('cls')
                        opP = 3
                        regresar = True
                    else:
                        print ("Introduce un numero entre 1 y 2")
                        regresar = True

            ###Sub-menú Sección Partidos: Mostrar todos los PP
            elif opP == 2:
                vgs.MostrarPartidos()
                volver = True  
            ###Sub-menú Sección Partidos: Volver al menú principal
            elif opP == 3:
                os.system('cls')
                volver = True           
            else:
                print ("Introduce un numero entre 1 y 3")
                

    ##Apartado de Senadores
    os.system('cls')
    if op == 2:
        print("""Estas en la sección de Senadores. Estas son las acciones""",
        """que puedes hacer:
        1: Buscar Senador especifico
        2: Mostrar Todos los Senadores Politicos
        3: Volver al menu principal
        """)

        opP = pedirOP()
        volver = False

        while not volver:
            ###Sub-menú Sección Senadores: Buscar Senador especifico
            if opP == 1:
                nombreC = input("Ingrese Nombre del Senador: ")
                os.system('cls')
                vgs.BuscarC(nombreC, None)
                os.system('cls')
                volver = True  
            
            ###Sub-menú Sección Senadores: Mostrar todos los Senadores
            elif opP == 2:
                vgs.MostrarSenadores(None)
                os.system('cls')
                volver = True  
                
                
            ###Sub-menú Sección Senadores: Volver al menú principal
            elif opP == 3:
                os.system('cls')
                volver = True
            
            else: 
                print ("Introduce un numero entre 1 y 3")
                

    ##Salir
    os.system('cls')
    if op == 3:
        print("""
        Gracias por usar nuestro programa :D
        Programadores: \n """,
        """
        Jaymed Linero (@Jaymed_DLC)
        Fernando Valencia (@Valenc_28g)
        """)
        salir = True
