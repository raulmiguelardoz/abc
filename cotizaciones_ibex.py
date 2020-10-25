# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:36:16 2020

@author: rmendozj
"""
import pandas as pd
def cotizaciones_IBEX_35(fichero):
    df=pd.read_csv(fichero,sep=";",decimal=",",thousands=".",index_col=0)
    new_datos=pd.DataFrame([df.min(),df.max(),df.mean()],index=['Minimo','Maximo','Media'])
    new_datos.to_excel("C:\\Users\\rmendozj\\Desktop\\Python\\Pandas\\nuevos_datos_ibex.xlsx")
    
cotizaciones_IBEX_35("C:\\Users\\rmendozj\\Desktop\\Python\\Pandas\\cotizacion_ibex.csv")
    