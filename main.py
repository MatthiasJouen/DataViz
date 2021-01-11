# coding: utf-8
from histo import createHisto
from fonctions import get_data_with_url, readJson, histoFromJson
from carte import create_map_deces, create_map_gueris, create_map_hospi

import pandas as pd
import urllib.request, json
import json
import folium
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
    print(df)
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
    figures = createHisto(df, ["reanimation","deces","gueris"], "nom", "date", app)
    #affichage des cartes
    

    #DASHBOARD
    colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'subtitle': 'white'
    }
    #Titre de la page
    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='DASHBOARD Jouen Matthias/ Helie Damien', style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    #CARTE 1
    html.H3(children='Carte de France des nouvelles hospitalisations', style={
        'textAlign': 'left',
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_hospi', srcDoc=open('new_hospi.html', 'r').read(), width='80%', height='400'),
    #CARTE 2
    html.H3('Carte de France des nouvelles guérisons', style={
        'textAlign': 'left',
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_gueris', srcDoc=open('gueris.html', 'r').read(), width='80%', height='400'),
    #CARTE 3
    html.H3('Carte de France des nouveaux deces',style={
        'textAlign': 'left',
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_deces', srcDoc=open('deces.html', 'r').read(), width='80%', height='400'),

    #HISTO
    html.Div(children=[
        html.H1(children='NOMBRE DE CAS COVID 19 EN FONCTION DES DEPARTEMENTS FRANCAIS'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='covid-rea',
                    figure=figures[0]
                )
            ]),
            html.Div([
                dcc.Graph(
                    id='covid-dead',
                    figure=figures[1]
                )
            ]),
            html.Div([
                dcc.Graph(
                    id='covid-healed',
                    figure=figures[2]
                )
            ]),
        ])         
    ])
    ])
    
if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    main(app)
    app.run_server(debug=True)