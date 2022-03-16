#!/usr/bin/env python
# coding: utf-8

# In[1]:



"""
Lectura de base de datos con pandas
@autor Ivette612
"""
import pandas as pd


def read_file(data): 
    """Read a csv file

    Parameters
    ----------
    file_csv : data
      
    Returns
    -------
    list
        a list of strings used that are a csv file
    """
   
   
    try:
        df = pd.read_csv(data)

        df_coodenadas = df[['origin','origin_latitude','origin_longitude', 'destination', 'destination_latitude','destination_longitude']]

        input = df_coodenadas.values.tolist()

    except FileNotFoundError:
        print("File not found.")
    except pd.errors.EmptyDataError:
        print("No data")
    except pd.errors.ParserError:
        print("Parse error")
    except Exception:
        print("Some other exception")
    return input




# In[ ]:




