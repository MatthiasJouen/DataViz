# coding: utf-8

try:
	#from fonctions import *
	from fonctions import readJson, histoFromJson
	from app import createDash

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
	import sys, getopt


except ImportError as E:

	print('''Il manque un ou plusieurs modules.\nEn effet le programme a rencontré l'erreur suivante : \n\n''' + str(E))
	exit()


def generate(project_path, target):

	all_data = readJson(project_path)
	histo = histoFromJson(all_data, target)
	
	
	createDash(histo, "X", "number", "Country")
	
"""
def main(argv):

if __name__ == '__main__':
	main(sys.argv[1:])
"""