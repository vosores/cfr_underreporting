import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import datetime
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
import os

out_folder = 'images'
regiones = ['Arica y Parinacota','Tarapacá','Antofagasta','Atacama','Coquimbo','Valparaíso','Santiago'
,'O’Higgins','Maule','Ñuble','Biobío','Araucanía','Los Ríos','Los Lagos','Aysén','Magallanes']
#########################################################################
#       crea csv para calcular undereporting actualizado.               #
#########################################################################

##Para Chile
df = pd.read_csv ("./data/COVID_Chile_Regiones_sin_provincias.csv", sep = ";")
df = df.dropna(subset = ['Region'])
df = df.groupby("Fecha", as_index=False).sum()
df["Fecha_dt"] = pd.to_datetime (df["Fecha"])
df =df[df["Fecha_dt"] >= '2020-03-18']
df = df.sort_values(by=["Fecha_dt"])
df = df.reset_index(drop=True)
df_c=df
##Otro
df = pd.read_csv ("./data/COVID_Chile_Regiones_sin_provincias.csv", sep = ";")
df = df.dropna(subset = ['Region'])
df["Fecha_dt"] = pd.to_datetime (df["Fecha"])
df =df[df["Fecha_dt"] >= '2020-03-18']
# df = df[df["Region"] == "Maule"]
# df = df_c["Fecha_dt"]
print(df[df["Region"] == "Maule"].Contagiados)

# FECHA_INICIAL = '2020-03-18'
# FECHA_FINAL = '2021-05-13'

# FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# FECHAS = pd.to_datetime(FECHAS)
# print(df)



columns = ["Province/State","Country/Region","Lat","Long"]
for fecha in df_c.Fecha_dt:
    columns.append(fecha.strftime("%m/%d/%Y"))


confirmed = pd.DataFrame(columns=columns)
deaths = pd.DataFrame(columns=columns)


info_conf = [" " ,"Chile",-35.6751,-71543]
info_deaths = [" " ,"Chile",-35.6751,-71543]
for i in df_c.Contagiados:
    info_conf.append(int(i))

for i in df_c.Muertes:
    info_deaths.append(int(i))


confirmed.loc[0] = info_conf
deaths.loc[0] = info_deaths

i=1
for region in regiones:
    info_confirmados = [" " ,region,-35.6751,-71543]
    info_muertes = [" " ,region,-35.6751,-71543]
    for j in df[df["Region"] == region].Contagiados:
        info_confirmados.append(int(j))
    for j in df[df["Region"] == region].Muertes:
        info_muertes.append(int(j))
    confirmed.loc[i] = info_confirmados
    deaths.loc[i] = info_muertes
    i = i+1

confirmed.to_csv("./data/covid19_confirmed_chile_fmt.csv",index = False)
deaths.to_csv("./data/covid19_deaths_chile_fmt.csv",index = False)