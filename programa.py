from funciones import *
fich = leer_xml("github/ejercicio_xml/Batallasjuegodetronos.xml")

opcion = menu()
while opcion != 6:
    if opcion == 1:
        for var in mostrar_batallas(fich):
            print (var)
        print()
    elif opcion == 2:
        print ("Han muerto personajes importantes en",contar_muertes(fich),"batallas.")
        print()
    elif opcion == 3:
        batalla = input("Introduzca el nombre de la batalla: ")
        print ("La casa",batalla_atacantes(fich,batalla)[0][0],"es la atacante y la casa",batalla_atacantes(fich,batalla)[1][0],"es la defensora.")
        print()
        
    opcion = menu()