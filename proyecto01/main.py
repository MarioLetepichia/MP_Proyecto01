"""Llamadas al Api"""
from unicodedata import name
#from urllib import response

import requests 
#import bcrypt
#importa la libreria de dotenv ,libreria que ayuda a ocultar la llave
from dotenv import load_dotenv
import os
#carga el .env file
load_dotenv()  # take environment variables from .env.


#Para ocultar la llave
API_KEY = os.getenv("API_KEY")
response = ""



def makeRequestsAndGetWeather(lat1,lon1,lat2,lon2):
    """ Realiza las dos llamadas al Api y obtiene e imprime la información que se necesita"""

    #Se hace la primera petición de origen 
    responseOne = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat1}&lon={lon1}&APPID={API_KEY}&lang=sp&units=metric")
    responseTwo = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat2}&lon={lon2}&APPID={API_KEY}&lang=sp&units=metric")

    #imprime 200 si todo ha ido bien en la petición
    #print(response)

    response = responseOne

    for x in range(2):
        #imprime un json del resultado (ahi viene toda la info)
        print(response.json())

        data = response.json()
        #accesemos a los valores e imprimimos
        temperature = data['main']['temp'] 
        description = data['weather'][0]['description']
        print("Datos climatologicos de",data['name'],
        "\ntemperatura:",temperature,
        "\ndescripción:",description )
        response = responseTwo



def makeNRequetsAndGetWeather():
    """ método que ejecuta n veces el metodo makeRequestsAndGetWeather"""
    lat1 = "19.43"
    lon1= "-99"
    lat2= "25.6714"
    lon2 = "-100.309"
    #for x in :
    for x in range(1):
        
        makeRequestsAndGetWeather(lat1,lon1,lat2,lon2)
        

makeNRequetsAndGetWeather()


#makeRequestAndGetWeather("19.43","-99","25.6714","-100.309")