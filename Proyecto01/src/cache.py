
class Cache:
    def __init__(self):
        self.ca = {}

    def addCache(self, iata, info):
        #Revisamos si ambos argumentos cumplen con las condiciones
        if type(iata) != str or type(info) != dict:
            raise TypeError
        #Ahora resivamos que el codigo IATA tenga exactamente 3 caracteres
        if len(iata) != 3 :
            raise ValueError
        #Si todo salio bien agregamos el nuevo dato al diccionario
        self.ca.update({iata, info})

'''
Falta...
Buscar un elemento en el cache (regresa -1 si no se encuentra)
Actualizar cache (actualizar el value para cada key, recibe un dict completo)
Entegar una lista con todos los keys dentro del cache
Limpiar el cache
'''

