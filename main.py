# coding: utf-8
from histo import createHisto
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
    
    
    #------------------------------------------------------------------------------------------------------------#
    #----------------------------------------------DASHBOARD-----------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------#

    colors = {
    'background': 'white',
    'text': '#7FDBFF',
    'subtitle': 'black'
    }
    #-----------------------Haut de page---------------------------------
    app.layout = html.Div(style={
        'backgroundColor': colors['background'],
        'textAlign': 'center'
        }, 
        children=[
    html.H1(children='DASHBOARD Jouen Matthias/ Helie Damien', style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.P("Cette page est répartie en trois morceaux et montre l'impact de la COVID-19 depuis le début de l'épidémie selon différents critères et selon les départements Français"),
    html.P("Les données sont mises à jour tous les jours !"),
    html.Hr(),
    #----------------------Données totales----------------------------------
    html.Div(style={
        'textAlign':'left'
        },
        children=[
        html.H3("Données totales en France depuis le début de la pandémie"),
        html.H4("Nombre de guéris total :" + str(df_France[0][6])),
        html.H4("Nombre d'hospitalisés' total :" + str(df_France[0][3])),
        html.H4("Nombre de décès total :" + str(df_France[0][5])),
    ]),
    html.Hr(),
    #---------------------PARTIE 1------------------------------------------
    html.H3(children='Carte de France des hospitalisations de la COVID-19', style={
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_hospi', srcDoc=open('html/new_hospi.html', 'r').read(), width='80%', height='400'),
        dcc.Graph(
            id='covid-rea',
            figure=figures[0]
            ),
    html.Hr(),
    #---------------------PARTIE 2-----------------------------------------
    html.H3('Carte de France des guérisons de la COVID-19', style={
        'textAlign': 'center',
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_gueris', srcDoc=open('html/gueris.html', 'r').read(), width='80%', height='400'),
        dcc.Graph(
            id='covid-healed',
            figure=figures[2]
        ),
    html.Hr(),
    #---------------------PARTIE 3-----------------------------------------
    html.H3('Carte de France des décès de la COVID-19',style={
        'textAlign': 'center',
        'color': colors['subtitle']
    }),
    html.Iframe(id='map_deces', srcDoc=open('html/deces.html', 'r').read(), width='80%', height='400'),
        dcc.Graph(
            id='covid-dead',
            figure=figures[1]
        ),      
    ])
    
if __name__ == '__main__':
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title='Sujet COVID-19'
    main(app)
    app.run_server(debug=True)