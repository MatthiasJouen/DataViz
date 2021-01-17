# coding: utf-8

import pandas as pd
import urllib
import json

def get_data_with_url():
    #On recupere les donnees de l'api et on les retournes sous DataFrame
    url = 'https://coronavirusapi-france.now.sh/AllLiveData'

    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            df = pd.json_normalize(data)
            dt = df.to_dict()
            return pd.DataFrame.from_dict(dt['allLiveFranceData'][0])
    except urllib.error.URLError:
        print("Cant access {0}".format(url))