# coding: utf-8

from histo import createHisto, createMaps
from fonctions import get_data_with_url
from carte import create_map_deces, create_map_gueris, create_map_hospi

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import os


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


def main(app):
    #on recupere les datas
    df = get_data_with_url()
     #On supprime les colonnes qu'on a pas besoin
    del df['source']
    del df['sourceType']
    del df['decesEhpad']
    del df['casConfirmesEhpad']
    del df['casConfirmes']
    del df['nouvellesHospitalisations']
    del df['nouvellesReanimations']
    
    #On supprime les lignes de regions qui ne nous sont pas utiles
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

    #creations des cartes
    create_map_hospi(project_path, df)
    create_map_deces(project_path, df)
    create_map_gueris(project_path, df)
    #creation des histogrammes
    figures = createHisto(["Nombre de personnes ayant été hospitalisées selon le département", "Nombre de personnes décédés selon le département", "Nombre de guérisons selon le département"], df, ["hospitalises","deces","gueris"], "nom")
    createMaps(app, df_France, figures)

if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title='Sujet COVID-19'
    main(app)
    app.run_server(debug=True)