library(reticulate)
use_condaenv('r-reticulate', required = TRUE)
library(greta)
library(greta.gp)
greta::install_tensorflow(method = "conda",
                          version = "1.14.0",
                          extra_packages = "tensorflow-probability==0.7")
install.packages("httr")
install.packages("dplyr")
