# coding: utf-8

import mpl_toolkits as mplt
import numpy as np
import matplotlib.pyplot as plt
#from fonctions import *

def draw(states, years):

	extract_data = {year:[] for year in years}
	state = ' '.join([state for state in states])


	#######################################################################################
	# Construction des Itérables (listes, dico) contenant les données depuis fonctions.py #
	#######################################################################################
	for year in extract_data.keys():
		for state in states:
			pass
			

	

	for data in extract_data.values():
		for element in data:
			if element[1]==-1:
				return

	if len(years)==1:
		position = [[1, 1, 1]]
	elif len(years)==2:
		position = [[2, 1, 1],[2, 1, 2]]
	elif len(years)==3:
		position = [[2, 2, 1],[2, 2, 2],[2, 1, 2]]
	elif len(years)==4:
		position = [[2, 2, j] for j in range(1,5)]
	else:
		return



	fig = plt.figure()
	j = 0

	for year, data in extract_data.items():

		ax = fig.add_subplot(position[j][0], position[j][1], position[j][2])
		ax.set_title('''CARTE DU NOMBRE TOTAL DE MORT DES ETATS EN ''' + year)
		
		m = mplt.Basemap(width=12000000,height=9000000,projection='merc', resolution=None,llcrnrlat=25.,llcrnrlon=-126.,urcrnrlat=50,urcrnrlon=-65.)
		m.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)

		lat = []
		lon = []
		valeur = []

		for state2 in data:
			######### Lattitude et Longitude a partir de fonctions ########
			lat2 = None
			lon2 = None
			###############################################################

			lat.append(lat2)
			lon.append(lon2)
			valeur.append(int(state2[1]))

			x, y = m(lon2, lat2)
			x2, y2 = m(lon2 + 1.5, lat2 + 5)
			plt.annotate(state2[0], xy=(x, y),  xycoords='data', xytext=(x2, y2), textcoords='data', arrowprops=dict(arrowstyle="->"))

		sizes = [(x*200/max(valeur)) for x in valeur]
		xpt,ypt = m(lon, lat)
		m.scatter(xpt, ypt, s=sizes, c='b', zorder=2)
			
		j += 1



	plt.show()
	plt.close()