# coding: utf-8

from collections import namedtuple as NT
import numpy as np
import pandas as pd

from os import path
import os

import urllib

import json
import csv

def get_data_with_url():
    #On recupere les donnees de l'api et on les retournes sous DataFrame
    url = 'https://coronavirusapi-france.now.sh/AllLiveData'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        df = pd.json_normalize(data)
        dt = df.to_dict()
        return pd.DataFrame.from_dict(dt['allLiveFranceData'][0])

