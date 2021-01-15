# coding: utf-8

import folium
import os.path as path
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html


def create_map_hospi(project_path, data, filter=None):
    Map = folium.Map(location=[47.1539,2.2508] ,zoom_start=5)#centre de la france
    choropleth = folium.Choropleth(
        geo_data=path.join(project_path, "src", 'departements.geojson'),
        name="departements",
        data=data,
        columns=['nom', 'hospitalises'],
        key_on='feature.properties.nom',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.2
    ).add_to(Map)

    folium.LayerControl().add_to(Map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nom'], labels=False)
    )
    Map.save(outfile=path.join(project_path, 'html/new_hospi.html'))

def create_map_gueris(project_path, data, filter=None):
    Map = folium.Map(location=[47.1539,2.2508] ,zoom_start=5)#centre de la france
    choropleth = folium.Choropleth(
        geo_data=path.join(project_path, "src", 'departements.geojson'),
        name="departements",
        data=data,
        columns=['nom', 'gueris'],
        key_on='feature.properties.nom',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.2
    ).add_to(Map)

    folium.LayerControl().add_to(Map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nom'], labels=False)
    )
    Map.save(outfile=path.join(project_path, 'html/gueris.html'))

def create_map_deces(project_path, data, filter=None):
    Map = folium.Map(location=[47.1539,2.2508] ,zoom_start=5)#centre de la france
    choropleth = folium.Choropleth(
        geo_data=path.join(project_path, "src", 'departements.geojson'),
        name="departements",
        data=data,
        columns=['nom', 'deces'],
        key_on='feature.properties.nom',
        fill_color='PuRd',
        fill_opacity=0.7,
        line_opacity=0.2
    ).add_to(Map)

    folium.LayerControl().add_to(Map)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['nom'], labels=False)
    )
    Map.save(outfile=path.join(project_path, 'html/deces.html'))
    