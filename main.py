# coding: utf-8

try:
	#from fonctions import *
	from graph import *
	from carte import *
	from histo import *
	from app import *

	import tkinter as tk #interface graphique
	from tkinter import Label
	from tkinter import Button
	import tkinter.messagebox as tkMessageBox
	import requests
	import json

	from collections import namedtuple as NT
	import numpy as np #traitement mathématique
	import pandas as pd

	import folium #map
	import matplotlib.pyplot as plt #histogramme

	from urllib.request import urlopen as UR


# f.mainloop()

if __name__ == '__main__':
	# Lancer programme principal
	histogramme.app.run_server(debug=True)
	create_map()
	pass