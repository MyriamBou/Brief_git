#impotation de la librairie
from sqlalchemy import create_engine 
import pandas as pd
import pymysql

# création de la connection
engine = create_engine("mysql+pymysql://myriam:hey@localhost/BDcardata")

"""
Version simple:
    df( c'est la variable data frame)
df=pd.read_csv('/home/myriam/Desktop/Projects/achat_voiture/00_input_project/carData.csv')
df.to_sql(cardata, con = engine, if_exists='append', index = False)
    
       """

# fonction pour lier la table csv 
def chargement(link, table):

    # lie le fichier csv
    df = pd.read_csv(link)
# commande pour envoyer au csv
    df.to_sql(table, con = engine, if_exists='append', index = False)
    return print("done")

chargement('/home/myriam/Desktop/Projects/achat_voiture/00_input_project/carData.csv', 'carData')# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

