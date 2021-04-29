import csv
class Cosecha:
    __listaCosecha = [[],[]]
    def __init__(self):
        self.__listaCosecha =[[0 for i in range(45)] for y in range(20)]
    def cargarCosechas(self,indice1,indice2,kilos):
        self.__listaCosecha[indice1][indice2] += kilos
    def mostrar(self):
        for i in range(len(self.__listaCosecha)):
            for j in range(len(self.__listaCosecha[i])):
                print(self.__listaCosecha[i][j])
    def totalKilos(self,indice1):
        todo = 0
        for j in range(len(self.__listaCosecha[indice1])):
            todo += self.__listaCosecha[indice1][j]
        return todo
    def getKilos(self,numDia,i):
        return self.__listaCosecha[i][numDia]




