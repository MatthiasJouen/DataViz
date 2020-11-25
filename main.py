# coding: utf-8

try:
	#from fonctions import *
	from graph import *
	from carte import *
	from fonctions import readJson, histoFromJson

	import requests
	import json

	import numpy as np #traitement mathématique

	import dash
	import dash_core_components
	import dash_html_components

	import pandas as pd

	import folium #map
	import matplotlib.pyplot as plt #histogramme

	from urllib.request import urlopen as UR

	import os



except ImportError as E:

	print('''Il manque un ou plusieurs modules.\nEn effet le programme a rencontré l'erreur suivante : \n\n''' + str(E))
	exit()


def generate(project_path):

	all_data = readJson(project_path)
	histo = histoFromJson(all_data)

	app = dash.Dash(__name__)

if __name__ == '__main__':
	project_path = os.getcwd()      

	generate(project_path)