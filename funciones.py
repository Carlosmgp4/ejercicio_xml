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

def batalla_atacantes(fich,nom):
    lista = []
    atacante = fich.xpath('/raiz/batalla[nombre="%s"]//atacantes/atacante/text()'%nom)
    defensore = fich.xpath('/raiz/batalla[nombre="%s"]//defensores/defensor/text()'%nom)
    lista.append(atacante)
    lista.append(defensore)
    return lista

def listar_casas(fich):
    lista = []
    for var in fich.xpath('//atacantes/atacante/text()'):
        if var not in lista:
            lista.append(var)
    return lista

def casa_batalla(fich,ca):
    lista = []
    ata = fich.xpath('//contendientes/ejercito_atacante/atacantes[atacante="%s"]/../../../nombre/text()'%ca)
    defe = fich.xpath('//contendientes/ejercito_defensor/defensores[defensor="%s"]/../../../nombre/text()'%ca)
    lista.append(ata)
    lista.append(defe)
    return lista