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
    df_output.to_html("output.html")



# In[ ]:





# In[ ]:



