# cfr_underreporting

1.- Instalar R: sudo apt install r-base
2.- Instalar los siguientes paquetes en R
    2.1 install.packages("reticulate")
    2.2 install.packages("greta")
    Al acceder a la librería pide instalar conda:
    No non-system installation of Python could be found.
    Would you like to download and install Miniconda?
    Miniconda is an open source environment management system for Python.
    See https://docs.conda.io/en/latest/miniconda.html for more details.
    Would you like to install Miniconda? [Y/n]: Y

    Queda en: environment location: /home/Usuario/.local/share/r-miniconda 

    2.3 install.packages("greta.gp") 
        Si no se instala usar:
        install.packages("remotes")
        remotes::install_github("greta-dev/greta.gp")
3.- Instalar las siguientes librerías en R
    3.1 install.packages("dplyr")
    3.2 install.packages("lubridate")
    3.3 install.packages("data.table")
    Se necesita instalar paquete curl y openssl
        sudo apt install -y libssl-dev
        sudo apt install lubcurl4-openssl-devurl 
        ó
        sudo apt install libcurl4-openssl-dev
    3.4 Instalar xml2 en R
        sudo apt install libxml2-dev
        install.packages("xml2")
    3.5 install.packages("tidyverse")
    3.6 install.packages("countrycode")

4.- Installar Anaconda en mi usuario y luego correr el script
    inicio.R que está en mi escritorio.


    
conda config --set auto_activate_base false
5.- install.packages("here")
    install.packages("patchwork")
    remotes::install_github("epiforecasts/NCoVUtils")
    install.packages("zoo")
