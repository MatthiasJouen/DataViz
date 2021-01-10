# coding: utf-8

import folium
import os.path as path
import pandas as pd


def create_map(project_path, data, filter=None):
    Map = folium.Map(location=[47.1539,2.2508] ,zoom_start=6)#centre de la france
    choropleth = folium.Choropleth(
        geo_data='departements.geojson',
        name="departements",
        data=data,
        columns=['nom', 'deces'],
        key_on='feature.properties.nom',
        fill_color='OrRd',
        fill_opacity=0.7,
        line_opacity=0.2
    ).add_to(Map)

    folium.LayerControl().add_to(Map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nom'], labels=False)
    )
    Map.save(outfile=path.join(project_path, 'france.html'))