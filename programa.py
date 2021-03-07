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
        if len(batalla_atacantes(fich,batalla)[0]) == 1:
            print ("La casa atacantes es: ")
            print (batalla_atacantes(fich,batalla)[0][0])
        else:
            print ("Las casas atacantes son: ")
            for var in batalla_atacantes(fich,batalla)[0]:
                print (var)
        
        if len(batalla_atacantes(fich,batalla)[1]) == 1:
            print ("La casa defensora es: ")
            print (batalla_atacantes(fich,batalla)[1][0])
        else:
            print ("Las casas defensoras son: ")
            for var in batalla_atacantes(fich,batalla)[1]:
                print (var)
        print()
    elif opcion == 4:
        print ("Estas son las casas disponibles: ")
        for var in listar_casas(fich):
            print (var)
        print()
        casa = input("De que casa desea realizar la consulta: ")
        print ("la casa %s a participado como atacante en estas batallas: " % casa)
        if len(casa_batalla(fich,casa)[0]) == 0:
            print ("No ha participado en ninguna.")
        else:
            for var in casa_batalla(fich,casa)[0]:
                print (var)
        print()
        print ("la casa %s a participado como defensora en estas batallas: " % casa)
        if len(casa_batalla(fich,casa)[1]) == 0:
            print ("No ha participado en ninguna.")
        else:
            for var in casa_batalla(fich,casa)[1]:
                print (var)
        print()
    elif opcion == 5:
        
        
    opcion = menu()