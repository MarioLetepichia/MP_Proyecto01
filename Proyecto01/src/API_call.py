
 # """Llamadas al Api"""
from unicodedata import name
# #from urllib import response

import requests 
# #import bcrypt
# #importa la libreria de dotenv ,libreria que ayuda a ocultar la llave
from dotenv import load_dotenv
import os
# #carga el .env file
load_dotenv()  # take environment variables from .env.
#Para ocultar la llave
API_KEY = os.getenv("API_KEY")
#API_KEY = "690105502b81dfb642de8266590f7300"



    
    
    
    #print(API_KEY)

    #response = ""

def request(lat,lon):
    """ request """
    #falta mandar excepcion en caso que se salga de cordenadas no eistentes
    #Se hace la primera peticion de origen 
    #Se hace la primera peticion de origen 
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={API_KEY}&lang=sp&units=metric")
    return response
    #responseOne = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat1}&lon={lon1}&APPID={API_KEY}&lang=sp&units=metric")
    #responseTwo = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat2}&lon={lon2}&APPID={API_KEY}&lang=sp&units=metric")



def make2RequestsAndGetWeather(lat1,lon1,lat2,lon2):
    """ Realiza las dos llamadas al Api y obtiene e imprime la información que se necesita"""

    responseOne = request(lat1,lon1)
    print(responseOne)
    responseTwo = request(lat2,lon2)
        
        

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



def make1RequestAndGetWeather(lat1,lon1):
    #   """ Realiza una llamadas al Api y obtiene e imprime la información que se necesita"""

    #Se hace la primera petición de origen 
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat1}&lon={lon1}&APPID={API_KEY}&lang=sp&units=metric")


    #imprime 200 si todo ha ido bien en la petición
    print(response)
    #imprime un json del resultado (ahi viene toda la info)
    print(response.json())

    data = response.json()
    #accesemos a los valores e imprimimos
    temperature = data['main']['temp'] 
    description = data['weather'][0]['description']
    print("Datos climatologicos de",data['name'],
    "\ntemperatura:",temperature,
    "\ndescripción:",description )
        


def makeNRequestsAndGetWeather():
    #""" método que ejecuta n veces el metodo makeRequestsAndGetWeather"""
    lat1 = "19.43"
    lon1= "-99"
    lat2= "25.6714"
    lon2 = "-100.309"
    #for x in :
    for x in range(1):
            
        make2RequestsAndGetWeather(lat1,lon1,lat2,lon2)
            

def requestGetJsons(lat,lon):
    """ metodo que devuelve el json de la respuesta del request """

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID=690105502b81dfb642de8266590f7300&lang=sp&units=metric")
    return response.json()