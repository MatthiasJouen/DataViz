# coding: utf-8

from collections import namedtuple as NT
import numpy as np

from os import path
import os

from datetime import datetime, timedelta
from datetime import date
import requests

import json
import csv

#################################################################################
# Fonction pour associer Région/pays/département à ses coordonnées géographique #
#################################################################################

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
            f.write(datetime(now.year, now.month, now.day, now.hour-1, now.minute, now.second).isoformat())
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
                case += int(item["cas"])

            if(item["deces"] != ""):
                death += int(item["deces"])
            
            if(item["guerisons"] != ""):
                heal += int(item["guerisons"])
    
    return cases, deaths, heals

def histoFromJson(all_data):
	histoDatas = { "Name":[], "Cases":[], "Healed":[], "Deads":[] }

	countryDict = countriesList(all_data)

	for country in countryDict.values():
		cases, deaths, heals = targetDataPerWeek(all_data, country)

		histoDatas["Country"].append(country)
		histoDatas["Cases"].append(cases)
		histoDatas["Healed"].append(heals)
		histoDatas["Deads"].append(deaths)
	
	return histoDatas