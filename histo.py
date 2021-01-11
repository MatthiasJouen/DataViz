# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


def createHisto(histoDatas, ordonnee, abscisse, color="", app=""):
    
    df = pd.DataFrame(histoDatas)
    figures = []
    for ord in ordonnee:
        figures.append(px.bar(df, x=abscisse, y=ord, color=color, barmode="group"))
    return figures
    

