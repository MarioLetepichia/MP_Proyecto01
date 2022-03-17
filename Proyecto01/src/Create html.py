#!/usr/bin/env python
# coding: utf-8

# In[2]:



"""
Lectura de base de datos con pandas
@autor Ivette612
"""
import pandas as pd


def create_html(list): 
    
    """Create a html

    Parameters
    ----------
    list : tickets_procesados
    Returns
    -------
    html with the output final information 
        
    """

    
    df_output = pd.DataFrame(list)     
    df_columns_names = df_output.set_axis(['|ORIGIN|','|TEMPERATURE ORIGIN|', '|CLOUD COVER ORIGIN|', '|DESTINATION|', '|TEMPERATURE DESTINATION|', '|CLOUD COVER DESTINATION|'], axis='columns') 
    df_final = df_columns_names.style.set_caption("TICKETS PROCESADOS")
    df_out = df_final.to_html("output.html")
    
    return df_out



# In[ ]:





# In[ ]:




