"""Modulo que hace pruebas unitarias del archivo Api_calls.py"""
import unittest
from Api_calls import request

class Api_calls(unittest.TestCase):
    """Clase que hereda de unittest.TestCase"""
    def test_requests(self):
        "test sobre si se ejecuta bien una petición"
        resultado = request("19.43","-99")
        assert resultado.status_code== 200
