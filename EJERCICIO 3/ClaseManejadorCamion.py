import csv
from ClaseCamion import Camion
class ManejadorCamion:
    __listaCamion = []
    def __init__(self):
        self.__listaCamion = []
    def test(self):
        testIdentificador = 5
        testNombre = 'Marcos'
        testPatente = 'ARUP498'
        testMarca = 'Iveco'
        testTara = 7890
        testCamion = Camion(testIdentificador,testNombre,testPatente,testMarca,testTara)
        print("TEST REALIZADO EXITOSAMENTE")
    def mostrarLista(self):
        for Camion in self.__listaCamion:
            print(Camion)
    def leerArchivo(self):
        archivo1 = open('Camioness.csv')
        reader = csv.reader(archivo1,delimiter=',')
        for fila in reader:
            id = fila[0]
            nom = fila[1]
            pat = fila[2]
            mar = fila[3]
            tar = int(fila[4])
            camion1 = Camion(id,nom,pat,mar,tar)
            self.__listaCamion.append(camion1)
        archivo1.close()
    def obtenerTara(self,indice1):
        return self.__listaCamion[indice1].getTara()
    def obtenerPatente(self,i):
        return self.__listaCamion[i].getPatente()
    def obtenerNombre(self,i):
        return self.__listaCamion[i].getNombre()
