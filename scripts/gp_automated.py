import os
import pandas as pd

columns = ["iso"]
iso = pd.DataFrame(columns=columns)

for i in ["CHL", "AYP", "TPA", "ANT", "ATM", "CQB", "VPO", "STO", "OHG", "MLE", "NBL", "BIO", "ARC", "LRS", "LLS", 
"AYN", "MGN"]:
    iso.loc[0] = i
    iso.to_csv("iso.csv",index = False)
    os.system("R CMD BATCH /home/shared/victorosores/cfr_underreporting/scripts/Chile_GP.R")    


# os.system("R")
# a <- 2.0
# a