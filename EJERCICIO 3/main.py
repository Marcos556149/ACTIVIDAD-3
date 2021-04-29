import csv
from ClaseManejadorCamion import ManejadorCamion
from ClaseCosecha import Cosecha
if __name__=='__main__':
    Camiones = ManejadorCamion()
    Camiones.leerArchivo()
    Camiones.test()
    Cosechas = Cosecha()
    archivo2 = open('Cosechass.csv')
    reader = csv.reader(archivo2,delimiter=',')
    for fila in reader:
        indice1 = int(fila[0]) - 1
        indice2 = int(fila[1]) - 1
        kilos = int(fila[2]) - Camiones.obtenerTara(indice1)
        Cosechas.cargarCosechas(indice1,indice2,kilos)
    archivo2.close()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Ingresar descarga de camion")
        print("[2]...Mostrar la cantidad de kilos descargados de un camion")
        print("[3]...Mostrar conductor, patente, y cantidad de kilos descargados en un dia")
        print("[0]...Salir")
        try:
            op=int(input('Selecciona una opcion: '))
            if op in range(4):
                if op == 1:
                    indice1=int(input('Ingrese el identificador del camion: '))
                    while (indice1 < 1)or(indice1 > 20):
                        indice1=int(input('Numero incorrecto, ingrese un identificador de camion del 1 al 20: '))
                    indice1=indice1 - 1
                    indice2=int(input('Ingrese el dia: '))
                    while (indice2 < 1)or(indice2 > 45):
                        indice2=int(input('Numero de dia incorrecto, ingrese un numero de dia del 1 al 45: '))
                    indice2=indice2 - 1
                    kilos=int(input('Ingrese la cantidad de kilogramos descargados por el camion: '))
                    while (kilos < 0):
                        kilos=int(input('Numero incorrecto, la cantidad de kilogramos debe ser un numero positivo, ingrese nuevamente la cantidad de kilogramos: '))
                    kilos= kilos - Camiones.obtenerTara(indice1)
                    Cosechas.cargarCosechas(indice1,indice2,kilos)
                if op == 2:
                    indice1=int(input('Ingresar el identificador del camion: '))
                    while (indice1 < 1)or(indice1 > 20):
                        indice1=int(input('Numero incorrecto, ingrese un identificador de camion del 1 al 20: '))
                    indice1=indice1 - 1
                    print("El total de kilogramos de uva descargados por el camion con identificador {} es: {} ".format(indice1+1,Cosechas.totalKilos(indice1)))
                if op == 3:
                    numDia=int(input('Ingresa un numero de dia: '))
                    while (numDia < 1)or(numDia > 45):
                        numDia=int(input('Numero de dia incorrecto, ingrese un numero de dia del 1 al 45: '))
                    print("PATENTE          CONDUCTOR          CANTIDAD DE KILOS")
                    for i in range(20):
                        print((Camiones.obtenerPatente(i)).ljust(16) , (Camiones.obtenerNombre(i)).ljust(18) , str(Cosechas.getKilos(numDia - 1,i)))
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    print()
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 3")
        except ValueError:
            print("ERROR, ingrese solamente numeros")

