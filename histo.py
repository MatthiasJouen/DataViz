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
        figures.append(px.bar(df, x=abscisse, y=ord, color=ord, barmode="group", title=tit))
    return figures
    

