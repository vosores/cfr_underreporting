import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os

paises = {"Chile": ["CHL", "Chile"], "Argentina": ["ARG", "Argentina"],
"Australia": ["AUS", "Australia"],
"Denmark": ["DNK", "Denmark"],
"Austria": ["AUT", "Austria"],
"Switzerland": ["CHE", "Switzerland"],
"Belgium": ["BEL", "Belgium"],
"Korea del Sur": ["KOR", "Korea del Sur"],
"Usa": ["USA", "Usa"],
"United Kingdom": ["GBR", "United Kingdom"],
"Italy": ["ITA", "Italy"]
}

chile_regiones = {"Chile": ["CHL", "Chile"],
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

regiones = paises#chile_regiones

if (regiones == paises):
    out_folder = 'figures_paper'
    path = "./data/current_estimates_extracted_not_age_adjusted_countries/result_"
else:
    out_folder = 'figures_Chile_all_dates'
    path = "./data/current_estimates_extracted_not_age_adjusted_all_dates/result_"





for region in regiones.keys():
    df = pd.read_csv (path + regiones[region][0] +".csv")
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
    ax8.plot (FECHAS.values[:], (1.0 - df["estimate"].values[:])*100, label = "% Sintomáticos no reportados, "+regiones[region][1])
    ax8.legend (loc = "best")
    ax8.set_ylim(0, 100)
    ax8.set_ylabel("Porcentaje de casos sintomáticos no reportados (%)")
    fig.savefig(os.path.join(out_folder,"as_reportados_" + regiones[region][1] + ".png"), format='png', bbox_inches = 'tight')
    plt.close(fig)