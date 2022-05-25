#LIMPIADOR DE VENTANAS
#Instrucciones
#Ubicación de la ventana en donde se encuentra el dispositivo: Ingrese A - B - C (En mayúsculas)
#Ingrese el estado en el que se encuentra la ventana: 0 = LIMPIO - 1 = SUCIO
def limpiador_ventanas():
    # Iniciacializa el estado final
    # indica 0 si esta limpio y 1 si esta sucio
    global objetivo
    global ubicacion_limpiador
    global letra_2
    global letra_3
    objetivo = {'A': '0', 'B': '0', 'C': '0'}
    costo = 0
    print("===========================================================")
    print("=                   LIMPIA VENTANAS                       =")
    print("===========================================================")
    ubicacion_limpiador = input("Introduzca la ubicación del limpiador de ventanas: ") #Ubicacion donde esta colocado el limpiador de ventanas
    #Restringe el numero de ventanas a las ventanas existentes
    if ubicacion_limpiador == "A" or ubicacion_limpiador == "B" or ubicacion_limpiador == "C":
        estado_ventana = input("Introduzca el estado de " + ubicacion_limpiador + ": ") #Especifica si la ventana esta sucia o limpia
        if estado_ventana == "0" or estado_ventana == "1":
            
            #Ingreso de estados de las demas ventanas
            if ubicacion_limpiador == "A":
                letra_2 = "B"
                letra_3 = "C"
                otras_ventanas()
            if ubicacion_limpiador == "B":
                letra_2 = "A"
                letra_3 = "C"
                otras_ventanas()
            if ubicacion_limpiador == "C":
                letra_2 = "A"
                letra_3 = "B"
                otras_ventanas()

            print("===========================================================")
            print("=    Objetivo deseado: " + str(objetivo) + "     =")
            print("===========================================================")

            if ubicacion_limpiador == 'A':
                print("El limpiador se encuentra en la ventana " + ubicacion_limpiador)
                # La ubicacion A se encuentra sucia
                if estado_ventana == '1':

                    print("La ventana "+ubicacion_limpiador+" esta sucia.")
                    # Quita la suciedad y marca como limpia
                    limpieza_objetivo()
                    costo += 1 #Aumenta el costo de la limpieza
                    print("Limpiando la ventana "+ubicacion_limpiador+"...")
                    print("Costo actual: " + str(costo))
                    print("===========================================================")

                    if siguiente_ventana == '1':
                        # Si B esta sucia
                        print("La ventana "+letra_2+" esta sucia.")
                        print("Pasandose a la ubicacion "+letra_2+".")
                        costo += 1 #Incrementa el costo por movimiento
                        print("Costo actual: " + str(costo))
                        # Quita la suciedad y la marca como limpia
                        objetivo['B'] = '0'
                        costo += 1   
                        print("Limpiando la ventana "+letra_2+"...") #Costo de limpiar
                        print("Costo actualizado: "+str(costo))
                        print("===========================================================")

                    else:
                        if siguiente_ventana == '0':
                            # Quita la suciedad y marca como limpia
                            print("La ventana B esta limpia.")
                            print("Ninguna acción. Costo actual: " + str(costo))
                            print("===========================================================")
                        
                        else:
                            # Mensaje de error de estado
                            print("                         VENTANA B                         ")
                            print("               No se pudo realizar la acción               ")
                            print("                     Estado no valido                      ")
                            print("===========================================================")

                    if ultima_ventana == '1':
                        # Si C esta sucia
                        print("La ventana C esta sucia.")
                        print("Pasandose a la ubicacion C.")
                        costo += 1 #Incrementa el costo de movimiento
                        print("Costo actual: " + str(costo))
                        # Quita la suciedad y marca como limpia
                        objetivo['C'] = '0'
                        costo += 1 #Incrementa el costo por limpieza
                        print("Limpiando ventana C...")
                        print("Costo actual: " + str(costo))
                        print("===========================================================")

                    else:
                        if ultima_ventana == '0':
                            # Quita la suciedad y marca como limpia
                            print("La ventana C esta limpia.")
                            print("Ninguna acción. Costo actual: " + str(costo))
                            print("===========================================================")
                        
                        else:
                            # Mensaje de error de estado
                            print("                         VENTANA C                         ")
                            print("               No se pudo realizar la acción               ")
                            print("                     Estado no valido                      ")
                            print("===========================================================")

                if estado_ventana == '0':
                    print("La ventana A se encuentra limpia.")

                    if siguiente_ventana == '1': # si la ventana B esta sucia
                        print("La ventana B esta sucia.")
                        print("Pasandose a la ubicacion B.")
                        costo += 1 #Incrementa el costo por movimiento
                        print("Costo actual: " + str(costo))
                        # Quita la suciedad y la marca como limpia
                        objetivo['B'] = '0'
                        costo += 1   
                        print("Limpiando la ventana B...") #Costo de limpiar
                        print("Costo actualizado: "+str(costo))
                        print("===========================================================")
                        
                    else:
                        if siguiente_ventana == '0':
                            print("Ninguna acción " + str(costo))
                            print(costo)
                            # Quita la suciedad y marca como limpia
                            print("La ventana B se encuentra limpia.")
                            print("===========================================================")
                        
                        else:
                            # Mensaje de error de estado
                            print("                         VENTANA B                         ")
                            print("               No se pudo realizar la acción               ")
                            print("                     Estado no valido                      ")
                            print("===========================================================")
                
                    if ultima_ventana == '1': # si la ventana C esta sucia
                        print("La ventana C esta sucia.")
                        print("Pasandose a la ubicacion C.")
                        costo += 1 #Incrementa el costo por movimiento
                        print("Costo actual: " + str(costo))
                        # Quita la suciedad y la marca como limpia
                        objetivo['C'] = '0'
                        costo += 1   
                        print("Limpiando la ventana C...") #Costo de limpiar
                        print("Costo actualizado: " + str(costo))
                        print("===========================================================")
                        
                    else:
                        if ultima_ventana == '0':
                            print("Ninguna acción " + str(costo))
                            print(costo)
                            # Quita la suciedad y marca como limpia
                            print("La ventana C se encuentra limpia.")
                            print("===========================================================")

                        else:
                            # Mensaje de error de estado
                            print("                         VENTANA C                         ")
                            print("               No se pudo realizar la acción               ")
                            print("                     Estado no valido                      ")
                            print("===========================================================")

            else:
                if ubicacion_limpiador == 'B':
                    print("El limpiador se encuentra en la ventana B")
                    # La ubicacion B se encuentra sucia
                    if estado_ventana == '1':
                        print("La ventana "+ubicacion_limpiador+" esta sucia.")
                        # Quita la suciedad y marca como limpia
                        objetivo['B'] = '0'
                        costo += 1 #Aumenta el costo de la limpieza
                        print("Limpiando la ventana "+ubicacion_limpiador+"...")
                        print("Costo actual: " + str(costo))
                        print("===========================================================")

                        if siguiente_ventana == '1':
                            # Si A esta sucia
                            print("La ventana A esta sucia.")
                            print("Pasandose a la ubicacion A. ")
                            costo += 1 #Incrementa el costo de movimiento
                            print("Costo actual: " + str(costo))
                            # Quita la suciedad y marca como limpia
                            objetivo['A'] = '0'
                            costo += 1 #Incrementa el costo por limpieza
                            print("Limpiando ventana A...")
                            print("Costo actual: " + str(costo))
                            print("===========================================================")

                        else:
                            if siguiente_ventana == '0':
                                # Quita la suciedad y marca como limpia
                                print("La ventana A esta limpia.")
                                print("Ninguna acción. Costo actual: " + str(costo))
                                print("===========================================================")
                            
                            else:
                                # Mensaje de error de estado
                                print("                         VENTANA A                         ")
                                print("               No se pudo realizar la acción               ")
                                print("                     Estado no valido                      ")
                                print("===========================================================")

                        if ultima_ventana == '1':
                            # Si C esta sucia
                            print("La ventana C esta sucia.")
                            print("Pasandose a la ubicacion C.")
                            costo += 1 #Incrementa el costo de movimiento
                            print("Costo actual: " + str(costo))
                            # Quita la suciedad y marca como limpia
                            objetivo['C'] = '0'
                            costo += 1 #Incrementa el costo por limpieza
                            print("Limpiando ventana C...")
                            print("Costo actual: " + str(costo))
                            print("===========================================================")

                        else:
                            if ultima_ventana == '0':
                                # Quita la suciedad y marca como limpia
                                print("La ventana C esta limpia.")
                                print("Ninguna acción. Costo actual: " + str(costo))
                                print("===========================================================")
                            
                            else:
                                # Mensaje de error de estado
                                print("                         VENTANA C                         ")
                                print("               No se pudo realizar la acción               ")
                                print("                     Estado no valido                      ")
                                print("===========================================================")

                    if estado_ventana == '0':
                        print("La ventana B se encuentra limpia.")
                        print("===========================================================")

                        if siguiente_ventana == '1': # si la ventana A esta sucia
                            print("La ventana A esta sucia.")
                            print("Pasandose a la ubicacion A.")
                            costo += 1 #Incrementa el costo por movimiento
                            print("Costo actual: " + str(costo))
                            # Quita la suciedad y la marca como limpia
                            objetivo['A'] = '0'
                            costo += 1   
                            print("Limpiando la ventana A...") #Costo de limpiar
                            print("Costo actualizado: "+str(costo))
                            print("===========================================================")
                        
                        else:
                            if siguiente_ventana == '0':
                                print("Ninguna acción " + str(costo))
                                print(costo)
                                # Quita la suciedad y marca como limpia
                                print("La ventana A se encuentra limpia.")
                                print("===========================================================")

                            else:
                                # Mensaje de error de estado
                                print("                         VENTANA A                         ")
                                print("               No se pudo realizar la acción               ")
                                print("                     Estado no valido                      ")
                                print("===========================================================")
                
                        if ultima_ventana == '1': # si la ventana C esta sucia
                            print("La ventana C esta sucia.")
                            print("Pasandose a la ubicacion C.")
                            costo += 1 #Incrementa el costo por movimiento
                            print("Costo actual: " + str(costo))
                            # Quita la suciedad y la marca como limpia
                            objetivo['C'] = '0'
                            costo += 1   
                            print("Limpiando la ventana C...") #Costo de limpiar
                            print("Costo actualizado: " + str(costo))
                            print("===========================================================")
                        
                        else:
                            if ultima_ventana == '0':
                                print("Ninguna acción " + str(costo))
                                print(costo)
                                # Quita la suciedad y marca como limpia
                                print("La ventana C se encuentra limpia.")
                                print("===========================================================")

                            else:
                                # Mensaje de error de estado
                                print("                         VENTANA C                         ")
                                print("               No se pudo realizar la acción               ")
                                print("                     Estado no valido                      ")
                                print("===========================================================")

                else:
                    if ubicacion_limpiador == 'C':
                        print("El limpiador se encuentra en la ventana C")
                        # La ubicacion C se encuentra sucia
                        if estado_ventana == '1':
                            print("La ventana "+ubicacion_limpiador+" esta sucia.")
                            # Quita la suciedad y marca como limpia
                            objetivo['A'] = '0'
                            costo += 1 #Aumenta el costo de la limpieza
                            print("Limpiando la ventana "+ubicacion_limpiador+"...")
                            print("Costo actual: " + str(costo))
                            print("===========================================================")

                            if siguiente_ventana == '1':
                                # Si A esta sucia
                                print("La ventana A esta sucia.")
                                print("Pasandose a la ubicacion A. ")
                                costo += 1 #Incrementa el costo de movimiento
                                print("Costo actual: " + str(costo))
                                # Quita la suciedad y marca como limpia
                                objetivo['A'] = '0'
                                costo += 1 #Incrementa el costo por limpieza
                                print("Limpiando ventana A...")
                                print("Costo actual: " + str(costo))
                                print("===========================================================")
                                
                            else:
                                if siguiente_ventana == '0':
                                    # Quita la suciedad y marca como limpia
                                    print("La ventana A esta limpia.")
                                    print("Ninguna acción. Costo actual: " + str(costo))
                                    print("===========================================================")
                                
                                else:
                                    # Mensaje de error de estado
                                    print("                         VENTANA A                         ")
                                    print("               No se pudo realizar la acción               ")
                                    print("                     Estado no valido                      ")
                                    print("===========================================================")

                            if ultima_ventana == '1':
                                # Si B esta sucia
                                print("La ventana B esta sucia.")
                                print("Pasandose a la ubicacion B.")
                                costo += 1 #Incrementa el costo de movimiento
                                print("Costo actual: " + str(costo))
                                # Quita la suciedad y marca como limpia
                                objetivo['B'] = '0'
                                costo += 1 #Incrementa el costo por limpieza
                                print("Limpiando ventana B...")
                                print("Costo actual: " + str(costo))
                                print("===========================================================")

                            else:
                                if ultima_ventana == '0':
                                    # Quita la suciedad y marca como limpia
                                    print("La ventana B esta limpia.")
                                    print("Ninguna acción. Costo actual: " + str(costo))
                                    print("===========================================================")

                                else:
                                    # Mensaje de error de estado
                                    print("                         VENTANA B                         ")
                                    print("               No se pudo realizar la acción               ")
                                    print("                     Estado no valido                      ")
                                    print("===========================================================")

                        if estado_ventana == '0':
                            print("La ventana C se encuentra limpia.")

                            if siguiente_ventana == '1': # si la ventana A esta sucia
                                print("La ventana A esta sucia.")
                                print("Pasandose a la ubicacion A.")
                                costo += 1 #Incrementa el costo por movimiento
                                print("Costo actual: " + str(costo))
                                # Quita la suciedad y la marca como limpia
                                objetivo['A'] = '0'
                                costo += 1   
                                print("Limpiando la ventana A...") #Costo de limpiar
                                print("Costo actualizado: "+str(costo))
                                print("===========================================================")
                        
                            else:
                                if siguiente_ventana == '0':
                                    print("Ninguna acción " + str(costo))
                                    print(costo)
                                    # Quita la suciedad y marca como limpia
                                    print("La ventana A se encuentra limpia.")
                                    print("===========================================================")

                                else:
                                    # Mensaje de error de estado
                                    print("                         VENTANA A                         ")
                                    print("               No se pudo realizar la acción               ")
                                    print("                     Estado no valido                      ")
                                    print("===========================================================")
                
                            if ultima_ventana == '1': # si la ventana B esta sucia
                                print("La ventana B esta sucia.")
                                print("Pasandose a la ubicacion B.")
                                costo += 1 #Incrementa el costo por movimiento
                                print("Costo actual: " + str(costo))
                                # Quita la suciedad y la marca como limpia
                                objetivo['B'] = '0'
                                costo += 1   
                                print("Limpiando la ventana B...") #Costo de limpiar
                                print("Costo actualizado: " + str(costo))
                                print("===========================================================")
                        
                            else:
                                if ultima_ventana == '0':
                                    print("Ninguna acción " + str(costo))
                                    print(costo)
                                    # Quita la suciedad y marca como limpia
                                    print("La ventana B se encuentra limpia.")
                                    print("===========================================================")

                                else:
                                    # Mensaje de error de estado
                                    print("                         VENTANA B                         ")
                                    print("               No se pudo realizar la acción               ")
                                    print("                     Estado no valido                      ")
                                    print("===========================================================")



            # Limpieza finalizada
            print("=                      ESTADO FINAL                       =")
            print("===========================================================")
            print(objetivo)
            print("Medida de rendimiento: " + str(costo))
            print("===========================================================")

        else:
            print("===========================================================")
            print("=                       ERROR!!                           =")
            print("=             Este no es un estado valido                 =")
            print("===========================================================")
            print("      \n")
            limpiador_ventanas()

    #Mensaje de ventanas no existentes o no disponibles
    else:
        print("===========================================================")
        print("=                       ERROR!!                           =")
        print("=   Esta ventana no se encuentra disponible o no existe   =")
        print("===========================================================")
        print("      \n")
        limpiador_ventanas()

def otras_ventanas():
    global siguiente_ventana
    global ultima_ventana
    siguiente_ventana = input("Introduzca el estado de "+ letra_2 + ": ")
    ultima_ventana = input("Introduzca el estado de "+ letra_3 + ": ")

def limpieza_objetivo():
    if ubicacion_limpiador == "A":
        objetivo['A'] = '0'
    if ubicacion_limpiador == "B":
        objetivo['B'] = '0'
    if ubicacion_limpiador == "C":
        objetivo['C'] = '0'
        
limpiador_ventanas()