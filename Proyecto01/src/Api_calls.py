
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
    """ método que devuelve la respuesta del api """
  
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={API_KEY}&lang=sp&units=metric")
    return response


def requestGetJsons(lat,lon):
    """ metodo que devuelve el json de la respuesta del request """
    response = request(lat,lon)
    return response.json()


def make2RequestsAndGetWeather(lat1,lon1,lat2,lon2):
    """ Realiza las dos llamadas al Api y obtiene e imprime la información que se necesita"""

    responseOne = request(lat1,lon1)
    responseTwo = request(lat2,lon2)

    response = responseOne

    for x in range(2):
        data = response.json()
        temperature = data['main']['temp'] 
        description = data['weather'][0]['description']
        print("Datos climatologicos de",data['name'],
        "\ntemperatura:",temperature,
        "\ndescripción:",description )
        response = responseTwo


def make1RequestAndGetWeather(lat1,lon1):
    """ Realiza una llamadas al Api y obtiene e imprime la información que se necesita"""

    response = request(lat1,lon1)
    data = response.json()
    temperature = data['main']['temp'] 
    description = data['weather'][0]['description']
    print("Datos climatologicos de",data['name'],
    "\ntemperatura:",temperature,
    "\ndescripción:",description )
        

