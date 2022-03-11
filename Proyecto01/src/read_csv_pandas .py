#!/usr/bin/env python
# coding: utf-8

# In[4]:



"""
Lectura de base de datos con pandas
@autor Ivette612
"""
import pandas as pd

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
#df_tickets = df['origin','destination'].value_counts()
df_destinos.to_csv("aita.csv")


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

