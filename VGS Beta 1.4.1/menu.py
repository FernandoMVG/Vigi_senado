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
                vgs.BuscarP(nombreP.title())

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
                        print("Por implementar")
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
                print("Por implementar")
                #vgs.MostrarPartidos()
                break
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
                #nombreC = input("Ingrese Nombre del Senador: ")
                #vgs.BuscarC()
                print("Por implementar")
                break
            
            ###Sub-menú Sección Senadores: Mostrar todos los Senadores
            elif opP == 2:
                #vgs.MostrarPartidos()
                print("Por implementar")
                break
                
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
    
    else:
        print ("Introduce un numero entre 1 y 3")
        


