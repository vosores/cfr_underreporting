import os
import pandas as pd

columns = ["iso"]
iso = pd.DataFrame(columns=columns)
countries = ["KOR", "USA", "GBR", "ITA"]#"AUS", "DNK", "AUT", "CHE", "BEL"]
chile_region = ["CHL", "AYP", "TPA", "ANT", "ATM", "CQB", "VPO", "STO", "OHG", "MLE", "NBL", "BIO", "ARC", "LRS", "LLS", 
"AYN", "MGN"]

for i in countries: #chile_region:
    iso.loc[0] = i
    iso.to_csv("iso.csv",index = False)
    os.system("R CMD BATCH /home/shared/victorosores/cfr_underreporting/scripts/Chile_GP.R")