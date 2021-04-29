class Camion:
    __identificador = ''
    __nombre = ''
    __patente = ''
    __marca = ''
    __tara = ''
    def __init__(self,id='',nom='',pat='',mar='',tar=''):
        self.__identificador = id
        self.__nombre = nom
        self.__patente = pat
        self.__marca = mar
        self.__tara = tar
    def __str__(self):
        return 'Camion numero: {}, nombre: {}, patente: {}, marca: {}, tara: {}'.format(self.__identificador,self.__nombre,self.__patente,self.__marca,self.__tara)
    def getTara(self):
        return self.__tara
    def getPatente(self):
        return self.__patente
    def getNombre(self):
        return self.__nombre

