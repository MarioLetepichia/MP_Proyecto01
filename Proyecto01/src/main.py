#Clases de Ivette
import read_csv_pandas
import create_html.py

import cache as c
import API_call as api

input = read_file('dataset1.csv')
cache = c.Cache()
tickets_procesados = []

for i in range(0,len(input)):
    #Guardamos la salida y la entrada del ticket #i
    ticket_entry = input[i]
    salida_ciudad = (ticket_entry[0], ticket_entry[1], ticket_entry[2])
    llegada_ciudad = (ticket_entry[3], ticket_entry[4], ticket_entry[5])
    #Comprobamos si estan en el cache
    clima_salida = cache.getValue(salida_ciudad[0])
    clima_llegada = cache.getValue('llegada_ciudad[0]')
    if clima_salida == None:
        clima_salida = api.requestGetJsons(salida_ciudad[1], salida_ciudad[2])
        cache.addValue(salida_ciudad[0], clima_salida)
    if clima_llegada == None:
        clima_llegada = api.requestGetJsons(llegada_ciudad[1], llegada_ciudad[2])
        cache.addValue(llegada_ciudad[0], clima_llegada)
    #Definimos un ticket tupla (salida, clima, llegada, clima)
    ticket = (salida_ciudad[0], clima_salida['main']['temp'], clima_salida['weather'][0]['description'], llegada_ciudad[0], clima_llegada['main']['temp'], clima_llegada['weather'][0]['description'])
    tickets_procesados.append(ticket)
    print(i)

create_html(tickets_procesados)