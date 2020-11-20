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

def getWeekLimit(currentDate):
    
    calendar = currentDate.isocalendar()
    weekDay = calendar[2]

    weekStart = currentDate - timedelta(days=(weekDay - 1))
    weekEnd = currentDate + timedelta(days=(7 - weekDay))

    dateStart = weekStart.isoformat()
    dateEnd = weekEnd.isoformat()

    return dateStart+" au "+dateEnd

def targetDataPerWeek(json_data, target):
    cases = list()
    deaths = list()
    heals = list()
    weeks = list()

    pos = -1

    for item in json_data:
        if(item["nom"].lower() == target.lower()):
            values = item["date"].split('-')
            
            currentDate = getWeekLimit(date(int(values[0]), int(values[1]), int(values[2])))

            if(item["cas"] == ""):
                case = 0
            else:
                case = int(item["cas"])

            if(item["deces"] == ""):
                death = 0
            else:
                death = int(item["deces"])
            
            if(item["guerisons"] == ""):
                heal = 0
            else:
                heal = int(item["guerisons"])

            

            if(currentDate not in weeks):
                weeks.append(currentDate)
                pos += 1
                
                cases.append(case)
                deaths.append(death)
                heals.append(heal)
            else:
                cases[pos] += case
                deaths[pos] += death
                heals[pos] += heal
    
    return cases, deaths, heals, weeks
            
##### Definition du chemin du projet et récupération des datas ####
#project_path = os.getcwd()                                       #
#all_data = readJson(project_path)                                #
################################################################### 