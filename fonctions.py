# coding: utf-8

from collections import namedtuple as NT
import numpy as np
import pandas as pd

from os import path
import os

from datetime import datetime, timedelta
from datetime import date
import requests
import urllib

import json
import csv

#################################################################################
# Fonction pour associer Région/pays/département à ses coordonnées géographique #
#################################################################################

def country_code_association(project_path, countryName):
    with open(path.join(project_path, "pays2020.csv"), "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if(row[5].lower() == countryName.lower):
                return row[-2]


def countriesList(json_data):
    contries = dict()

    for item in json_data:
        if ("code" in item.keys()):
            if (len(item["code"].split("-")) == 1):
                contries[item["code"]] = item["nom"]

    return contries


def getCountryCoordinateByName(countryName, project_path):
    with open(path.join(project_path, "coordinates.csv"), "r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if(row[-1].lower() == countryName.lower):
                return (row[1], row[2])

    return None
    

#############################################
# Fonctions pour extraire récuperer le Json #
#############################################


def get_json_data(project_path):
    last = time_since_last_call(project_path)
    now = datetime.now()

    diff = now - last
    hoursSinceLastCall = diff.total_seconds()/60/3600

    if (hoursSinceLastCall < 1):
        raise PermissionError("You have to wait 1 hour before calling again")

    url = "https://www.coronavirus-statistiques.com/corostats/openstats/open_stats_coronavirus.json"
    response = requests.get(url)
    save_time_call(project_path)

    json_data = response.json()

    with open(path.join(project_path, "coronavirus.json"), "w") as f:
        json.dump(json_data, f)


def time_since_last_call(project_path):
    old_path = path.join(project_path, "old.txt")
    if (path.exists(old_path)):
        with open(old_path, "r") as f:
            date = f.readline()
            try:
                return datetime.fromisoformat(date)
            except Exception:
                return datetime.now()
    else:
        save_time_call(project_path, True)

    return datetime.now()


def save_time_call(project_path, new=False):
    if(new):
        now = datetime.now()
        with open(path.join(project_path, "old.txt"), "w") as f:
            f.write(datetime(now.year, now.month, now.day,
                    now.hour-1, now.minute, now.second).isoformat())
    else:
        with open(path.join(project_path, "old.txt"), "w") as f:
            f.write(datetime.now().isoformat())


def readJson(project_path):
    try:
        get_json_data(project_path)
        print("Json updated")
    except PermissionError:
        print("Json unchanged")

    with open(path.join(project_path, "coronavirus.json"), "r") as f:
        content = json.load(f)

    return content

#########################################################################################
# Fonctions pour extraire les datas du Json (Date, lieu, nb cas, nb mort, nb guérisons) #
#########################################################################################

def targetDataPerWeek(json_data, target):

    cases = 0
    deaths = 0
    heals = 0

    for item in json_data:
        if(item["nom"].lower() == target.lower()):

            if(item["cas"] != ""):
                cases += int(item["cas"])

            if(item["deces"] != ""):
                deaths += int(item["deces"])

            if(item["guerisons"] != ""):
                heals += int(item["guerisons"])

    return cases, deaths, heals

def histoFromJson(all_data, target=""):
    histo = { "X": [], "Country": [], "number": [] }
    
    countryDict = countriesList(all_data)
    if(target != ""):
        cases, deaths, heals = targetDataPerWeek(all_data, target)
        return { "X": ["Cas", "Décès", "Guérison(s)"], "Country": [target, target, target], "number": [cases, heals, deaths] }

    for country in countryDict.values():
        cases, deaths, heals = targetDataPerWeek(all_data, country)
        
        histo["X"].append("Cas")
        histo["X"].append("Décès")
        histo["X"].append("Guérison(s)")

        histo["Country"].append(country)
        histo["Country"].append(country)
        histo["Country"].append(country)
        
        histo["number"].append(cases)
        histo["number"].append(heals)
        histo["number"].append(deaths)
        
    return histo


def data_for_map(all_data, target=""):
    if(target == ""):
        return None
    
    cases, deaths, heals = targetDataPerWeek(all_data, target)

    return {target:{"deaths": deaths, "cases": cases, "healed":heals}}


def data_by_dept(all_data):
    data = list()
    lst = [dico for dico in all_data if "DEP" in dico["code"]]
    for elem in lst:
        if("DEP" in elem["code"]):        
            cases, deaths, heals = targetDataPerWeek(lst, elem["name"])
            dep = dict()
            dep["code"] = elem["code"].replace("DEP-", "")
            dep["nom"] = elem["nom"]
            dep["cases"] = cases
            dep["deaths"] = deaths
            dep["heals"] = heals

            data.append(dep)
    return data


def get_data_with_url():
    #On recupere les donnees de l'api et on les retournes sous DataFrame
    url = 'https://coronavirusapi-france.now.sh/AllLiveData'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        df = pd.json_normalize(data)
        dt = df.to_dict()
        return pd.DataFrame.from_dict(dt['allLiveFranceData'][0])

"""
def get_data_by_regions(filter):
    all_data = []

    global_data = get_data_with_url()
    if global_data.empty():
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
"""