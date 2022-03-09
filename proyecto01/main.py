from unicodedata import name

import requests 
#import bcrypt
#importa la libreria de dotenv l

from dotenv import load_dotenv
import os
#carga el .env file
load_dotenv()  # take environment variables from .env.


#Para ocultar la llave
API_KEY = os.getenv("API_KEY")

def getWeather():
    """ Realiza las dos llamadas al Api y obtiene e imprime la información que se necesita"""

    #Se hace la primera petición de origen 
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat=19.43&lon=-99&APPID={API_KEY}&lang=sp&units=metric")


    #imprime 200 si todo ha ido bien en la petición
    #print(response)

    #imprime un json del resultado (ahi viene toda la info)
    print(response.json())

    data = response.json()
    #accesemos a los valores e imprimimos
    temperature = data['main']['temp'] 
    description = data['weather'][0]['description']
    print("Datos climatologicos de",data['name'],
    "\ntemperatura:",temperature,
    "\ndescripción:",description )

getWeather()
