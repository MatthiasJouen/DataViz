# coding: utf-8
from histo import createDash
from fonctions import get_data_with_url, readJson, histoFromJson
from carte import create_map

import pandas as pd
import urllib.request, json
import json
import folium
import datetime
import requests
import math

import os

def main():
    df = get_data_with_url()
	
    #On supprime les colonnes qu'on a pas besoin
    del df['source']
    del df['sourceType']
    del df['decesEhpad']
    del df['casConfirmesEhpad']
    del df['casConfirmes']
    del df['nouvellesHospitalisations']
    del df['nouvellesReanimations']
    
    #On supprime les lignes de regions
    number_regions = ["01", "02", "03", "04", "06", "05", "11", "24", "27", "28", "32", "44", "52", "53", "75", "76", "84", "93", "94"]
    for region in number_regions:
        index = df.index
        condition = df["code"] == "REG-"+region
        indices = index[condition]
        df.drop(indices, inplace=True)

    #On mets de cote les valeurs pour la France entiere
    indexNames = df[df['nom'] == 'France'].index
    df_France = df[df['nom'] == 'France'].values

    #on les enleve du DataFrame
    df.drop(indexNames, inplace=True)

    project_path = os.getcwd()
    create_map(project_path, df)

    createDash(df, ["reanimation","deces","gueris"], "nom", "date")
    
if __name__ == '__main__':
    main()