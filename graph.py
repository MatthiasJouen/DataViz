# coding: utf-8

import matplotlib.pyplot as plt
#from fonctions import *

def histo(wheres, weeks, param):

	#################################
	# Choix Pays/Région/Département #
	#################################
	week = None # Dates
	where = None
	#################################

	extract_data = [[1,2,1,2,3,4]] # Data en fonction du Pays/Région/Département
	
	i = 0

	for data in extract_data:
		if data==-1:
			return
		i +=1



	if i==1:
		position = [[1, 1, 1]]
	elif i==2:
		position = [[2, 1, 1],[2, 1, 2]]
	elif i==3:
		position = [[2, 2, 1],[2, 2, 2],[2, 1, 2]]
	else:
		position = [[2, 2, j] for j in range(1,5)]



	for element in position:

		i = 0

		if param==2:

			data = extract_data[position.index(element)]
			x = [0]*52

			while i<len(data):

				for j in range(5):
					x[(i%53)-1] += data[i]
				i +=1



			plt.figure(1)
			plt.subplot(element[0], element[1], element[2])
			plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
			plt.hist(x, bins=25, rwidth=100, color='blue')
			plt.legend()
			plt.xlabel("NOMBRE DE MORTS")
			plt.ylabel("NOMBRE DE SEMAINES")



			if len(weeks)>1:
				plt.title('''HISTOGRAMME POUR L'ETAT DU(DE) '''+where+' AU ')
				#+weeks[position.index(element)]
			else:
				plt.title('''HISTOGRAMME POUR L'ETAT DU(DE) '''+wheres[position.index(element)]+' AU '+week)



			plt.grid(True)


		else:

			data = [extract_data[position.index(element)]]
			# .cat1, extract_data[position.index(element)].cat2, extract_data[position.index(element)].cat3, extract_data[position.index(element)].cat4, extract_data[position.index(element)].cat5
			x = [[0]*52, [0]*52, [0]*52, [0]*52, [0]*52]

			

			# while i<min(len(data[l]) for l in range(len(data))):
			# 	for j in range(5):
			# 		x[j][(i%53)-1] += data[j][i]
			# 	i +=1



			plt.subplot(element[0], element[1], element[2])
			plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
			plt.hist(x, bins=25, rwidth=100, color=['blue', 'orange', 'green', 'red', 'purple'], label=['<1 week', '1-24 week', '25-44 week', '45-64 week', '>65 week'], histtype = 'bar')
			plt.legend()
			plt.xlabel("NOMBRE DE MORTS")
			plt.ylabel("NOMBRE DE SEMAINES")

			plt.title('''HISTOGRAMME POUR L'ETAT DU(DE) '''+wheres[position.index(element)])
			



			plt.grid(True)
			

			
	plt.show()