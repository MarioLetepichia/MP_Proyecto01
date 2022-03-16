class Cache:
    def __init__(self):
        self.ca = {}

    def getValue(self, iata):
        if type(iata) != str and len(iata) != 3:
            raise ValueError
        return self.ca.get(iata)

    def getKeys(self):
        return self.ca.keys()

    def getLength(self):
        return len(self.ca)

    def getValue(self, iata):
        if type(iata) != str:
            raise TypeError
        return self.ca.get(iata)

    def addValue(self, iata, info):
        #Revisamos si ambos argumentos cumplen con las condiciones
        if type(iata) != str or type(info) != dict:
            raise TypeError
        #Ahora resivamos que el codigo IATA tenga exactamente 3 caracteres
        if len(iata) != 3 :
            raise ValueError
        #Si todo salio bien agregamos el nuevo dato al diccionario
        self.ca.update({iata: info})

    #La construccion del cache actualizado debera ser en otro modulo
    def updateCache(self, dicc):
        if type(dicc) != dict:
            raise TypeError
        #Pudes agregar unas lineas que comprueben que toda key en 'dicc' este en 'ca' y que no haya extras
        self.ca.update(dicc)

    def clearCache(self):
        self.ca.clear()