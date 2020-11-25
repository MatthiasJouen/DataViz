# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Type": ["Nouveaux cas", "Décés", "Guéris", "Nouveaux cas", "Décés", "Guéris"],
    "Nombre": [5000, 450, 1000, 12000, 6501, 2354],
    "State": ["France", "France", "France", "USA", "USA", "USA"]
})

fig = px.bar(df, x="Type", y="Nombre", color="State", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='CAS COVID 19'),

    html.Div(children='''
        Histogramme du nombre de cas de covid en fonction du pays
    '''),

    dcc.Graph(
        id='covid-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)