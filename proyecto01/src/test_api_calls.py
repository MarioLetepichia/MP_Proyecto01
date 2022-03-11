import unittest
from Api_calls import request

class Api_calls(unittest.TestCase):

    def test_requests(self):
        resultado = request("19.43","-99")
        assert resultado.status_code== 200

#no las continue porque no me corrian :(.
