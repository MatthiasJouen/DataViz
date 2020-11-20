# coding: utf-8

try:
	#from fonctions import *
	from graph import *
	from carte import *
	from histo import *

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



except ImportError as E:

	print('''Il manque un ou plusieurs modules.\nEn effet le programme a rencontré l'erreur suivante : \n\n''' + str(E))
	exit()

where=['France', 'Espagne', 'USA']
when=[['2020-11-02', '2020-11-05', '2020-11-07', '2020-11-11', '2020-11-15', '2020-11-17', '2020-11-20','2020-11-22', '2020-11-24', '2020-11-26', '2020-11-28', '2020-11-30', '2020-12-01', '2020-12-05'],
 	['2020-11-02', '2020-11-05', '2020-11-07', '2020-11-11', '2020-11-15', '2020-11-17', '2020-11-20','2020-11-22', '2020-11-24', '2020-11-26', '2020-11-28', '2020-11-30', '2020-12-01', '2020-12-05'],
 	['2020-11-02', '2020-11-05', '2020-11-07', '2020-11-11', '2020-11-15', '2020-11-17', '2020-11-20','2020-11-22', '2020-11-24', '2020-11-26', '2020-11-28', '2020-11-30', '2020-12-01', '2020-12-05']]
number = [[22000, 21000, 18000, 25000, 32000, 12000, 17563,22000, 21000, 18000, 25000, 21000, 15200, 17563],#France
	[132, 520, 145, 245, 132, 95, 451,321, 145, 146, 178, 453, 231, 124],#Espagne
	[2200, 2100, 1800, 2500, 3200, 1200, 1753,2200, 2100, 1800, 2500, 2100, 1520, 1753]]#USA

print('Selectionnez un pays')#ici seront les boutons pour selectionner un lieu
choosenState = 'Espagne'#on stocke le pays qui a ete choisi
index = where.index(choosenState)#on recup l'index du tableau des pays

histoCas(where, when, number, index)#on envoi dans la fonction d'histo : (les pays, les valeurs des dates, les nb de cas, l'index du tab pays)


# f.mainloop()

if __name__ == '__main__':
	# Lancer programme principal
	pass