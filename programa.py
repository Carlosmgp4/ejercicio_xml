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
    opcion = menu()