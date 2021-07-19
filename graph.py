import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import datetime
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
import os

out_folder = 'figures_Chile'

# # # #########################################################################
# # # #       crea csv para calcular undereporting actualizado.               #
# # # #########################################################################

# # # df = pd.read_csv ("./data/COVID_Chile_Regiones_sin_provincias.csv", sep = ";")
# # # df = df.dropna(subset = ['Region'])
# # # df = df.groupby("Fecha", as_index=False).sum()
# # # df["Fecha_dt"] = pd.to_datetime (df["Fecha"])
# # # df = df.sort_values(by=["Fecha_dt"])
# # # df = df.reset_index(drop=True)
# # # df = df[(df["Contagiados"] > 100)]

# # # FECHA_INICIAL = '2020-03-18'
# # # FECHA_FINAL = '2021-05-13'

# # # FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# # # FECHAS = pd.to_datetime(FECHAS)
# # # # print(FECHAS)
# # # # print(df["Muertes_DEIS"])

# # # # print(FECHAS.day)
# # # # print(df["Contagiados"].values[1:]-df["Contagiados"].values[0:-1])
# # # # aa = [1,2,3,4,5,6]
# # # # print(aa[0:-1])


# # # # print(FECHA_INICIAL)

# # # # print((df["Muertes_DEIS"].values[1:]-df["Muertes_DEIS"].values[0:-1])[(df["Muertes_DEIS"].values[1:]-df["Muertes_DEIS"].values[0:-1])>=0])
# # # # print(df["Fecha_dt"])
# # # # # # muertes = df["Muertes_DEIS"].values[4:-20]-df["Muertes_DEIS"].values[3:-21]
# # # # # # contagiados = df["Contagiados"].values[4:-20]-df["Contagiados"].values[3:-21]
# # # # # # print(len(muertes))

# # # N_pop = 18952035

# # # new_table = pd.DataFrame(columns=["dateRep","day","month","year","cases","deaths","countriesAndTerritories","geoId",
# # # "countryterritoryCode","popData2019","continentExp"])

# # # for i in range(df.shape[0]):
# # #     new_table = new_table.append({"dateRep": FECHAS.strftime('%d/%m/%Y')[i], "day": FECHAS.day[i], "month": FECHAS.month[i], "year": FECHAS.year[i],"countriesAndTerritories": "Chile",
# # #     "geoId": "CL", "countryterritoryCode": "CHL", "popData2019": N_pop, "continentExp": "America"}, ignore_index=True)
# # # new_table["cases"][:] = 0.0
# # # new_table["cases"][1:] = df["Contagiados"].values[1:]-df["Contagiados"].values[0:-1]
# # # new_table["deaths"][:] = 0.0 
# # # deaths = df["Muertes_DEIS"].values[1:]-df["Muertes_DEIS"].values[0:-1]
# # # deaths[deaths<0]=0
# # # new_table["deaths"][1:] = deaths
# # # # new_table["countriesAndTerritories"]

# # # new_table_reversed = new_table.iloc[::-1]

# # # # print(new_table.deaths[420:437])
# # # # # # # print(df["Contagiados"])
# # # # # # # print(df["Contagiados"][3:-20])
# # # # # # # print(len(FECHAS))
# # # # # # # print(FECHAS,len(FECHAS))
# # # # # # # print(df["Muertes_DEIS"][3:-20])

# # # # # # plt.plot(FECHAS.values[1:],new_table["deaths"].values[1:],FECHAS.values[1:],new_table["cases"].values[1:]/70)
# # # # # # plt.show()

# # # # # # exit()


# # # fechas_dic = {}
# # # subreporte_dic = {}

# # # fig = plt.figure('Underreport',figsize = (10, 5))
# # # ax2 = fig.add_subplot(111)
# # # ax2.set_title('Estimación del subregistro')
# # # for country in ["Argentina","Bolivia","Brazil","Canada","Chile","Colombia","Australia"]:
# # #     df = pd.read_csv ("./data/"+country+".csv")
# # #     FECHA_INICIAL = df["date"][0]
# # #     FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# # #     FECHAS = pd.to_datetime(FECHAS)
# # #     fechas_dic[country] = FECHAS
# # #     subreporte_dic[country] = df["underreporting_estimate"].values
# # #     ax2.plot (FECHAS.values[:], df["underreporting_estimate"].values, label = "Subregistro "+country)
# # # ax2.legend (loc = "best")
# # # ax2.set_ylim(0, 1)
# # # fig.savefig(os.path.join(out_folder,'subreporte.png'), format='png', bbox_inches = 'tight')

# # # df = pd.read_csv ("./data/Brazil.csv")
# # # FECHA_INICIAL = df["date"][0]
# # # FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# # # FECHAS = pd.to_datetime(FECHAS)
# # # fig = plt.figure('Casos',figsize = (10, 5))
# # # ax3 = fig.add_subplot(111)
# # # ax3.set_title('Casos')
# # # ax3.plot (FECHAS.values[1:], df["total_cases"].values[1:]-df["total_cases"].values[0:-1], label = "Casos Totales")
# # # ax3.legend (loc = "best")
# # # fig.savefig(os.path.join(out_folder,'casos_totales.png'), format='png', bbox_inches = 'tight')



# # # df = pd.read_csv ("./data/Positividad_Diaria_Media_T.csv")
# # # FECHA_INICIAL = df["Fecha"][0]
# # # FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
# # # FECHAS = pd.to_datetime(FECHAS)
# # # fig = plt.figure('Comparación: subreporte, positividad, pcr',figsize = (10, 5))
# # # ax = fig.add_subplot(111)
# # # ax.set_title('Comparación: subreporte vs positividad')
# # # N = 7
# # # positividad_mov = np.convolve(df["positividad"].values, np.ones((N,))/N, mode='valid')
# # # pcr_mov = np.convolve(df["pcr"].values, np.ones((N,))/N, mode='valid')
# # # # ax.plot (FECHAS.values[:], df["positividad"].values, label = "Positividad")
# # # ax.plot (FECHAS.values[3:-3], positividad_mov, label = "Positividad (media movil 7 días)")
# # # ax.plot (fechas_dic["Chile"].values,subreporte_dic["Chile"], label = "Estimación subreporte")
# # # ax.plot (FECHAS.values[3:-3], pcr_mov/max(pcr_mov), label = "PCR (media movil 7 días)")
# # # ax.legend (loc = "best")
# # # # ax.set_ylim(0, 1)
# # # fig.savefig(os.path.join(out_folder,'underreport_positividad_pcr.png'), format='png', bbox_inches = 'tight')

regiones = {"Chile": ["CHL", "Chile"],
    "Arica y Parinacota": ["AYP", "Arica y Parinacota"], 
    "Tarapacá": ["TPA", "Tarapacá"], 
    "Antofagasta": ["ANT", "Antofagasta"], 
    "Atacama": ["ATM", "Atacama"], 
    "Coquimbo": ["CQB", "Coquimbo"], 
    "Valparaíso": ["VPO", "Valparaíso"], 
    "Santiago": ["STO", "Santiago"], 
    "O’Higgins": ["OHG", "O’Higgins"], 
    "Maule": ["MLE", "Maule"], 
    "Ñuble": ["NBL", "Ñuble"], 
    "Biobío": ["BIO", "Biobío"], 
    "Araucanía": ["ARC", "Araucanía"], 
    "Los Ríos": ["LRS", "Los Ríos"],
    "Los Lagos": ["LLS", "Los Lagos"], 
    "Aysén": ["AYN", "Aysén"], 
    "Magallanes": ["MGN", "Magallanes"]
    }

for region in ["Chile", "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Santiago", 
"O’Higgins", "Maule", "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos", "Aysén", "Magallanes"]:
    df = pd.read_csv ("./data/current_estimates_extracted_not_age_adjusted/result_" + regiones[region][0] +".csv")
    FECHA_INICIAL = df["date"][0]
    FECHAS = np.array([pd.to_datetime (FECHA_INICIAL) + datetime.timedelta(days=i) for i in range(df.shape[0])])
    FECHAS = pd.to_datetime(FECHAS)
    fig = plt.figure('Subreporte_'+regiones[region][1],figsize = (10, 5))
    ax7 = fig.add_subplot(111)
    ax7.set_title(regiones[region][1])
    ax7.fill_between(FECHAS.values[:], df["upper"].values[:]*100, df["lower"].values[:]*100, alpha=0.2)
    ax7.plot (FECHAS.values[:], df["estimate"].values[:]*100, label = "% Sintomáticos, "+regiones[region][1])
    ax7.legend (loc = "best")
    ax7.set_ylim(0, 100)
    ax7.set_ylabel("Porcentaje de casos sintomáticos reportados (%)")
    fig.savefig(os.path.join(out_folder,"s_reportados_" + regiones[region][1] + ".png"), format='png', bbox_inches = 'tight')
    plt.close(fig)


    fig = plt.figure('Reporte_'+regiones[region][1],figsize = (10, 5))
    ax8 = fig.add_subplot(111)
    ax8.set_title(regiones[region][1])
    ax8.fill_between(FECHAS.values[:], (1.0 - df["lower"].values[:])*100, (1.0 - df["upper"].values[:])*100, alpha=0.2)
    ax8.plot (FECHAS.values[:], (1.0 - df["estimate"].values[:])*100, label = "% Asintomáticos, "+regiones[region][1])
    ax8.legend (loc = "best")
    ax8.set_ylim(0, 100)
    ax8.set_ylabel("Porcentaje de casos asintomáticos (%)")
    fig.savefig(os.path.join(out_folder,"as_reportados_" + regiones[region][1] + ".png"), format='png', bbox_inches = 'tight')
    plt.close(fig)