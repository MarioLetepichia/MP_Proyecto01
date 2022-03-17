"""
Cache para guardar datos ya consultados en el API
@author MarioLetepichia
"""
class Cache:
    """
    Clase para representar dicha estructura

    ***
    Attributes
    ----------
    ca : dict
        Estructura que guardara toda la informacion

    Methods
    -------
    getValue(iata)
        Regresa el valor asociado a 'iata'
    getKeys()
        Regresa una lista con todos los codigos IATA
    getLength()
        Regresa el tamano del cache
    addValue(iata, info)
        Agrega una nueva entrada al cache
    updateCache(dicc)
        Actualiza los valores del cache
    clearCache()
        Limpia el cache
    """

    def __init__(self):
        """Inicializa un nuevo Cache
        """
        self.ca = {}

    def getValue(self, iata):
        """Regresa el valor asociado a 'iata'

        Parameters
        ----------
        iata: 
            Valor que sera buscado dentro del cache

        Raises
        ------
        ValueError
            Si el valor 'iata' no es de tipo 'str' o no tiene exactamente 3 caracteres

        Returns
        -------
        data
            Asociado al valor 'iata' o None si no se encontro nada
        """
        if type(iata) != str and len(iata) != 3:
            raise ValueError
        return self.ca.get(iata)

    def getKeys(self):
        """Genera una lista de valores 'iata' dentro existentes en el cache
        
        Returns
        -------
        list
            Con los 'iata' dentro del cache
        """
        return self.ca.keys()

    def getLength(self):
        """

        Returns
        -------
        int 
            Longitud del cache (# elementos)
        """
        return len(self.ca)

    def addValue(self, iata, info):
        """Agrega una nueva entrada al cache

        Parameters
        ----------
        iata: 
            Key que sera asignada a la nueva entrada
        info:
            Informacion asociada a la nueva entrada

        Raises
        ------
        TypeError
            Si 'iata' no es de tipo 'str' o 'info' no es de tipo 'dict'
        ValueError
            Si 'iata' no tiene exactamente 3 caracteres
        """
        if type(iata) != str or type(info) != dict:
            raise TypeError
        if len(iata) != 3 :
            raise ValueError
        self.ca.update({iata: info})

    def updateCache(self, dicc):
        """Actualiza el cache

        Parameters
        ----------
        dicc:
            Cache del que se tomaran los nuevos datos

        Raises
        ------
        TypeError
            Si 'dicc' no es de tipo 'dict'
        """
        if type(dicc) != dict:
            raise TypeError
        self.ca.update(dicc)

    def clearCache(self):
        """Borra el contenido de todo el cache
        """
        self.ca.clear()