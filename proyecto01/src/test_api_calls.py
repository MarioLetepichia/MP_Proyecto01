"""Modulo que hace pruebas unitarias del archivo Api_calls.py"""
import unittest
from Api_calls import request
from Api_calls import requestGetJsons

class Api_calls(unittest.TestCase):
    """Clase que hereda de unittest.TestCase"""
    def test_requests(self):
        "test sobre si se ejecuta bien una petición"
        resultado = request("19.43","-99")
        assert resultado.status_code== 200

    def test_info_Jsons_Uno(self):
        """test que verifica que se accede a la información correcta en los jsons"""
        nombreCiudad = requestGetJsons("19.39","-99.09")['name'] 
        nombrePais = requestGetJsons("19.39","-99.09")['sys']['country'] 
        id = requestGetJsons("19.39","-99.09")['sys']['id'] 
        assert  nombreCiudad == 'Iztacalco' and id == 47729 and nombrePais == 'MX'

 