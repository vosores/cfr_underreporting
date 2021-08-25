library(reticulate)
use_condaenv('r-reticulate', required = TRUE)
library(greta)
library(greta.gp)
library(magrittr)
library(dplyr)
library(lubridate, warn.conflicts = FALSE)

# if tensorflow is not installed to a virtual
# environment/conda environment, run this command
# to get the right versions of tensorflow installed

#greta::install_tensorflow(method = "conda",
                          #version = "1.14.0",
                          #extra_packages = "tensorflow-probability==0.7")

# Temporal variation in reporting - bayesian model framework
# Fit gaussian process model using greta.gp to under-reporting estimates over time

# Set paths
setwd("/home/shared/victorosores/cfr_underreporting/")

#source data processing and plotting scripts
source('R/jhu_data_import.R')
source('R/scale_cfr_temporal.R')
source('R/cases_known_convolution.R')
source('R/run_bayesian_model.R')

# Fechas
fecha_ini <- "2020-02-01"
fecha_end <- "2020-06-01"
countries = "yes"

# setting baseline level CFR
cfr_baseline <- 1.4
cfr_range <- c(1.2, 1.7)

# Set parameters
mean <- 13
median <- 9.1

mu_cfr <- log(median)
sigma_cfr <- sqrt(2*(log(mean) - mu_cfr))

# Hospitalisation to death distribution
hospitalisation_to_death_truncated <- function(x) {
  plnorm(x + 1, mu_cfr, sigma_cfr) - plnorm(x, mu_cfr, sigma_cfr)
}

#--- Load and clean data using separate function
jhu_data <- jhu_data_import()

#--- inference is compute and memory heavy
#--- a HPC is used to run the inference for many countries/regions
#--- therefore we pick a single country here to run 
#--- we also only run it for the timeseries from September 2020
#--- as there are memory allocation issues when running it with a longer
#--- timeseries on standard computers

#--- choosing which country to run the full inference for

#--- Codigos por region inventados.
#--- "Chile" = "CHL",
#--- "Arica y Parinacota" = "AYP", 
#--- "Tarapacá" = "TPA", 
#--- "Antofagasta" = "ANT", 
#--- "Atacama" = "ATM", 
#--- "Coquimbo" = "CQB", 
#--- "Valparaíso" = "VPO", 
#--- "Santiago" = "STO", 
#--- "O’Higgins" = "OHG", 
#--- "Maule" = "MLE", 
#--- "Ñuble" = "NBL", 
#--- "Biobío" = "BIO", 
#--- "Araucanía" = "ARC", 
#--- "Los Ríos" = "LRS",
#--- "Los Lagos" = "LLS", 
#--- "Aysén" = "AYN", 
#--- "Magallanes" = "MGN"

# # # for (iso in c("CHL", "AYP", "TPA", "ANT", "ATM", "CQB", "VPO", "STO", "OHG", "MLE", "NBL", "BIO", "ARC", "LRS", "LLS", 
# # # "AYN", "MGN")) {
iso_arg <- read.csv(file = 'scripts/iso.csv')$iso
inference_data <- cases_known_convolution(iso_arg, jhu_data, cfr_baseline) %>%
    dplyr::filter(date > fecha_ini & date < fecha_end)
    # dplyr::filter(date > fecha_ini)

prediction <- run_bayesian_model(inference_data,
                                n_inducing = 5,
                                cfr_baseline = cfr_baseline,
                                cfr_range = cfr_range,
                                cfr_trend = NULL,
                                verbose = TRUE)

if (countries == "no"){
  write.csv(prediction, file = paste(paste("data/current_estimates_extracted_not_age_adjusted_all_dates/result_",iso_arg,sep=""),".csv",sep=""), row.names = FALSE)
# saveRDS(prediction, file = paste(paste("data/current_estimates_extracted_not_age_adjusted/result_",iso_arg,sep=""),".rds",sep=""))
} else {
  write.csv(prediction, file = paste(paste("data/current_estimates_extracted_not_age_adjusted_countries/result_",iso_arg,sep=""),".csv",sep=""), row.names = FALSE)
}
q(save = 'no')
# # # } 




# # ci_poly <- tibble::tibble(x = c(plot_data$date, rev(plot_data$date)),
# #                           y = c(prediction$upper, rev(prediction$lower)))
