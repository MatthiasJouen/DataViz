# coding: utf-8

try:
	#from fonctions import *
	from graph import *
	from carte import *

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


appel = i = conditions = 0
year_list = [2, 1,5]
state_list = ['France', 'USA', 'Allemagne']

# f = tk.Tk()
# f.title('PROJET PYTHON E3')
# f.resizable(width=False, height=False)

histo(state_list, year_list, 1)

# class Bouton:
	# """
	# 	Bouton permettant de garder en mémoire le choix de l'utilisateur
	# """

	# def __init__(self, pValeur=''):
	# 	if type(pValeur)==str:
	# 		self.valeur = pValeur
	# 		self.chose = False
	# 		self.bouton = None
	# 		self.width = 5


	# def getchose(self):
	# 	return self.chose


	# def getstate(self):
	# 	return self.valeur


	# def selection(self):
	# 	conditions = 0
	# 	#suppress()

	# 	if self.chose:
	# 		self.chose = False
	# 	else:
	# 		self.chose = True

	# 	if self.valeur=='TESTER':
	# 		generate()
	# 	elif self.valeur=='QUITTER':
	# 		f.destroy()

	# 	self.change_button()
			
	# 	try:
	# 		int(self.valeur)
	# 	except Exception:
	# 		# mettre à jour
	# 		pass

				
	# def config_width(self, pWidth):
	# 	self.bouton.config(width=pWidth)


	# def change_button(self):
	# 	if self.chose:
	# 		self.bouton.config(bg='green', relief='flat')
	# 	else:
	# 		self.bouton.config(bg='grey', relief='raised')


	# def create(self):
	# 	self.bouton = tk.Button(f, width=self.width, bg='grey', relief='raised' ,text=self.valeur, command=self.selection)


	# def place(self, pI, pJ, par1, par2, par3):
	# 	if self.bouton != None:
	# 		if self.valeur in ('TESTER', 'QUITTER'):
	# 			self.bouton.grid(row=pI, columnspan=pJ, padx=par1, pady=par2, sticky=par3)
	# 		else:
	# 			self.bouton.grid(row=pI, column=pJ, padx=par1, pady=par2, sticky=par3)


	# def delete(self):

	# 	if self.bouton != None:
	# 		self.bouton.destroy()

# def data():

# 	string = ''
# 	f3 = tk.Toplevel(f)



# 	for state in state_list:

# 		for year in year_list:

# 			string += '\n\nETAT : ' + state
# 			string += ''' pour l'année ''' + year + ' :\n\n'

# 			stat = [[]] # Stats a partir de fonctions.py

# 			string += ' -> MOYENNE : ' + str(stat[0][0]) + '\n'
# 			string += ' -> MEDIANE : ' + str(stat[0][1]) + '\n'
# 			string += ' -> ECART TYPE : ' + str(stat[0][2]) + '\n'
# 			string += ' -> VARIANCE : ' + str(stat[0][3]) + '\n'


# 	#chaine1 = Label(f3, text=string).grid(row=1, column=1, columnspan=3)

# def charger(param):
# 	"""
# 		Charge l'histogramme ou la map en fonction du choix de l'utilisateur
# 	"""
# 	if param==3:
# 		data()

# 	elif conditions==1 or param==0:
# 		draw(state_list, year_list)

# 	elif conditions==2:
# 		histo(state_list, year_list, param)	

# def suppress(window):
# 	"""
# 		Ferme la fenetre passée en parametre
# 	"""
# 	try:
# 		window.destroy()
# 	except Exception:
# 		pass


# def generate():

# 	try:
# 		##########################################################
# 		# Création des itérables selon le choix de l'utilisateur #
# 		##########################################################

# 		state_list = []
# 		year_list = []

# 	except Exception:
# 		tkMessageBox.showinfo('ERREUR : Interne', 'Un problème est survenu veuillez réessayer')
# 		conditions = 0

# 	else:
# 		if len(state_list)==0 or len(year_list)==0:
# 			tkMessageBox.showinfo('ERREUR : Données', 'Il manque une ou plusieurs données')
# 			return



# 	if len(year_list)==1:

# 		if len(state_list)>4:
# 			conditions = 1
# 		else:
# 			conditions = 2

# 	elif len(year_list)>1 and len(year_list)<=4:

# 		if len(state_list)>1:
# 			conditions = 1
# 		else:
# 			conditions = 2

# 	elif len(year_list)>4:

# 		tkMessageBox.showinfo('ERREUR : Années', '''Vous avez entré un trop grand nombre d'années''')
		
# 	else:

# 		tkMessageBox.showinfo('ERREUR : Années', '''Vous avez entré un trop grand nombre d'années''')



# 	year = ' '.join(year_list)
# 	state = ' '.join(state_list)

# 	f2 = tk.Toplevel(f)
# 	f2.title('CHOIX')

# 	str1 = '''\n\nTracer le(les) histogramme(s) de(s) état(s) : ''' + state + ''' pour l'année ''' + year + ' OPTION : TOTAL\n\n'
# 	str3 = '''\n\nTracer la carte de(s) état(s) : de(s) état(s) : ''' + state + ''' pour l'année ''' + year + '\n\n'
# 	str2 = '''\n\nTracer le(les) histogramme(s) de(s) état(s) : ''' + state + ''' pour l'année ''' + year + ' OPTION : MULTI-ÂGE\n\n'
# 	str4 = '''\n\nAfficher les statistiques des données : ''' + state + ''' pour l'années ''' + year + '\n\n'

# 	#############################################################################
# 	# Création des boutons de choix de sélection d'interfaces (histo, map, stat)#
# 	#############################################################################

# 	while True:
		
# 		########################################################
# 		# Création Itérable selon le nombre de lieux différents#
# 		########################################################
# 		liste_button = {}
		
# 		i = 2
# 		j = 1

# 		for state, button in liste_button.items():
# 			if j%8==0:
# 				i+=1
# 				j=1
# 			button.create()
# 			button.place(i, j, 0, 0, None)
# 			j +=1



# f.mainloop()

if __name__ == '__main__':
	# Lancer programme principal
	pass