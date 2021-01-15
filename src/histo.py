# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


def createHisto(title, histoDatas, ordonnee, abscisse):
    df = pd.DataFrame(histoDatas)
    figures = []
    for ord,tit in zip(ordonnee, title):
        figures.append(px.bar(df, x=abscisse, y=ord, color=ord, barmode="group", title=tit, template="plotly_dark",
        labels={
            abscisse:"Départements",
            ord:ord
        },))
    return figures
    
def createMaps(app, df_France, figures):
    colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'subtitle': 'white'
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
    html.P(children="Cette page est répartie en trois morceaux et montre l'impact de la COVID-19 depuis le début de l'épidémie selon différents critères et selon les départements Français", style={
        'color':colors['subtitle']
    }),
    html.P(children="Les données sont mises à jour tous les jours !", style={
        'color':colors['subtitle']
    }),
    html.Hr(),
    #----------------------Données totales----------------------------------
    html.Div(style={
        'textAlign':'left',
        'color': colors['subtitle']
        },
        children=[
        html.H3(" Données totales en France depuis le début de la pandémie"),
        html.H4(" Nombre de guéris total : " + str(df_France[0][6])),
        html.H4(" Nombre d'hospitalisés total : " + str(df_France[0][3])),
        html.H4(" Nombre de décès total : " + str(df_France[0][5])),
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
    

