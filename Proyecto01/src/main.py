from collections import Iterable

#Recibe una lista de tuplas (IATA, latitud, longitud)
input = [("ABC", 123, 123), ("YXZ", 345,345)] #ejemplo

import cache as c
import API_call as api

cache = c.Cache
tickets_procesados = []

for i in range(0,3000):
    #Guardamos la salida y la entrada del ticket #i
    salida_ciudad = input[i*2]
    llegada_ciudad = input[i*2 + 1]
    #Comprobamos si estan en el cache
    clima_salida = cache.getValue(salida_ciudad[0])
    clima_llegada = cache.getValue(llegada_ciudad[0])
    if clima_salida == None:
        clima_salida = api.request(salida_ciudad[1], salida_ciudad[2])
    if clima_llegada == None:
        clima_llegada = api.request(llegada_ciudad[1], llegada_ciudad[2])
    #Definimos un ticket tupla (salida, clima, llegada, clima)
    ticket = (salida_ciudad[0], clima_salida, llegada_ciudad[0], clima_llegada)
    tickets_procesados.append(ticket)

##################################################

try:
    df = pd.read_csv('dataset1.csv')

except FileNotFoundError:
    print("File not found.")
except pd.errors.EmptyDataError:
    print("No data")
except pd.errors.ParserError:
    print("Parse error")
except Exception:
    print("Some other exception")

#ANALISIS:

df_destinos = df['destination'].value_counts()
df_origin = df['origin'].value_counts()
df_tickets = df['origin','destination'].value_counts()
#df_destinos.to_csv("aita.csv")


#Datos separados

df_destinosdf_filtrado = df.drop_duplicates()
df_iata= df[['origin','destination']]
df_origin= df[['origin']]
df_destination= df[['destination']]
df_coodenadas = df[['origin_latitude','origin_longitude','destination_latitude','destination_longitude']]



#Creacion html
#df_iata.to_html("'D:\\weather_data\\my_html.html")


#Concatenar archivos dataframe

frames = [df_iata, df_coodenadas]
df_result = pd.concat(frames)

#Creacion listas

list_origin = [];
list_destination = [];
list_origin = df_origin.to_csv('dataset.csv', index=False)
list_destination = df_destination.to_csv('dataset.csv', index=False)
list_iata = df_coodenadas.to_csv('dataset.csv', index = False)