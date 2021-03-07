from lxml import etree
import sys

def leer_xml(fichero):
    try:
        with open(fichero) as f:
            datos=etree.parse(fichero)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

def menu():
    print ("1. Mostrar nombre de todas las batallas de Juego De Tronos")
    print ("2. Contar las batallas donde a muerto un personaje importante")
    print ("3. Mostrar casa atacante y defensora de una batalla en concreto")
    print ("4. Mostrar las batallas donde ha participado una casa en concreto")
    print ("5. Mostrar las batallas de una región y quienes son los reyes atacantes y defensores")
    print ("6. Salir del programa")
    opcion = int(input("Que acción desea realizar: "))
    return opcion

def mostrar_batallas(fich):
    nombres = fich.xpath('//nombre/text()')
    return nombres

def contar_muertes(fich):
    lista = []
    for var in fich.xpath('//muerte_importante/text()'):
        if int(var) > 0:
            lista.append(int(var))
    return sum(lista)