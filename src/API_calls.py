
"""
Modulo para hacer las llamadas al API y obtener la información
@autor Liahut Ley Celic Aislinn
"""

import requests 
from dotenv import load_dotenv
import os

load_dotenv()  

API_KEY = os.getenv("API_KEY")


def request(lat,lon):
    """ método que devuelve la respuesta del api 
  
    Parameters
        ----------
        lat: 
            Valor que tiene el valor de latitud de la ciudad que se quiere hacer un request a la API
        lon: 
            Valor que tiene el valor de longitud de la ciudad que se quiere hacer un request a la API
        Returns
        -------
        response
            respuesta del API , si es 200 , quiere decir que todo bien, de lo contrario ha ocurrido un error
    """
  
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={API_KEY}&lang=sp&units=metric")
    return response


def requestGetJsons(lat,lon):
    """ metodo que devuelve el json de la respuesta del request
    Parameters
        ----------
        lat: 
            Valor que tiene el valor de latitud de la ciudad que se quiere hacer un request a la API
        lon: 
            Valor que tiene el valor de longitud de la ciudad que se quiere hacer un request a la API     
        Returns
        -------
        response
            Json con los datos """
            
    response = request(lat,lon)
    return response.json()
        

