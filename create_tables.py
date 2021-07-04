import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import datetime
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
import os

out_folder = 'images'

#########################################################################
#       crea csv para calcular undereporting actualizado.               #
#########################################################################

df = pd.read_csv ("./data/COVID_Chile_Regiones_sin_provincias.csv", sep = ";")
df = df.dropna(subset = ['Region'])
df = df.groupby("Fecha", as_index=False).sum()
df["Fecha_dt"] = pd.to_datetime (df["Fecha"])
df = df.sort_values(by=["Fecha_dt"])
df = df.reset_index(drop=True)
# df = df[(df["Contagiados"] > 100)]

# FECHA_INICIAL = '2020-03-18'
# FECHA_FINAL = '2021-05-13'

# FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# FECHAS = pd.to_datetime(FECHAS)
# print(df)

columns = ["Province/State","Country/Region","Lat","Long"]
for fecha in df.Fecha_dt:
    columns.append(fecha.strftime("%m/%d/%Y"))


confirmed = pd.DataFrame(columns=columns)
deaths = pd.DataFrame(columns=columns)


info_conf = [" " ,"Chile",-35.6751,-71543]
info_deaths = [" " ,"Chile",-35.6751,-71543]
for i in df.Contagiados:
    info_conf.append(int(i))

for i in df.Muertes:
    info_deaths.append(int(i))


confirmed.loc[0] = info_conf
confirmed.to_csv("covid19_confirmed_chile.csv",index = False)
deaths.loc[0] = info_deaths
deaths.to_csv("covid19_deaths_chile.csv",index = False)