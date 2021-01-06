# coding: utf-8
from histo import createDash
from map import create_map
import pandas as pd
import urllib.request, json
import json
import folium
import datetime
import requests
import math

def get_data_with_url():
    #On recupere les donnees de l'api et on les retournes sous DataFrame
    url = 'https://coronavirusapi-france.now.sh/AllLiveData'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        df = pd.json_normalize(data)
        dt = df.to_dict()
        return pd.DataFrame.from_dict(dt['allLiveFranceData'][0])

def get_data_by_regions(filter):
    """Request the API for the data of yesterday and store them into a list
    for each region

    Parameters
    ----------
    filter : String
        The information we want in our dataframe

    Returns
    -------
    list
        a list of the death or positive case or intensive care or recovered for the last 7 days
    """

    all_data = []

    global_data = get_data_with_url()
    if global_data.empty:
        print("Empty data for date " + datetime.today().strftime('%Y-%m-%d'))
    else:
        REGIONS = ["11", "24", "27", "28", "32", "44", "52", "53", "75", "76", "84", "93", "94"]
        for region in REGIONS:
            name = data_utils.get_from_global_data(global_data, "REG-"+region, "nom")
            data = data_utils.get_from_global_data(global_data, "REG-"+region, filter)
            data_for_day = {}
            data_for_day["region_nom"] = name
            data_for_day["region_num"] = region
            data_for_day[filter] = data
            all_data.append(data_for_day)
    return all_data

def main():
    df = get_data_with_url()
    #On supprime les colonnes qu'on a pas besoin
    del df['source']
    del df['sourceType']
    del df['decesEhpad']
    del df['casConfirmesEhpad']
    del df['casConfirmes']
    del df['nouvellesHospitalisations']
    del df['nouvellesReanimations']
    
    #On supprime les lignes de regions
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
    print(df_France)
    print(df)


    Map = folium.Map(location=[47.1539,2.2508] ,zoom_start=6)#centre de la france
    choropleth = folium.Choropleth(
        geo_data='departements.geojson',
        name="departements",
        data=df,
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
    Map.save(outfile='france.html')
    

if __name__ == '__main__':
    main()