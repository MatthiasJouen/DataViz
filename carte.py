# coding: utf-8

import mpl_toolkits as mplt
import numpy as np
import matplotlib.pyplot as plt
import folium
#from fonctions import *

def create_map(data_by_region, filter):
    franceMap = folium.Map(location=[45.7833,3.0833] ,zoom_start=6)
    choropleth = folium.Choropleth(
        geo_data='regions.geojson',
        name="regions",
        data=data_by_region,
        columns=['region_num', filter],
        key_on='feature.properties.code',
        fill_color='OrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=filter
    ).add_to(franceMap)

    folium.LayerControl().add_to(franceMap)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nom'], labels=False)
    )