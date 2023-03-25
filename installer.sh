#!/bin/bash

# Vérifier si pip est installé
if ! command -v pip &> /dev/null
then
    echo "pip n'est pas installé. Veuillez l'installer avant de continuer."
    exit
fi

# Installer le module emailfinder
pip install emailfinder
pip install requests
pip install dnspython
pip install colorama
pip install bs4
pip install is_wordpress

# Vérifier si l'installation a réussi
if [ $? -eq 0 ]
then
    echo "Les module ont étés installés avec succès."
else
    echo "Une erreur est survenue lors de l'installation des modules."
fi


# Vérifier si Nmap est installé
if ! command -v nmap &> /dev/null
then
    echo "Nmap n'est pas installé. Installation en cours..."
    # Installation de Nmap
    apt-get update
    apt-get install nmap -y
    if [ $? -eq 0 ]
    then
        echo "Nmap a été installé avec succès."
    else
        echo "Une erreur est survenue lors de l'installation de Nmap."
        exit
    fi
fi
