# coding: utf-8

import matplotlib.pyplot as plt
from numpy.lib.function_base import angle
import pandas as pd
#from fonctions import *

def histoCas(where, when, number, index):
       
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(7, 9))

    # Add x-axis and y-axis
    ax.bar(when[index],number[index],color='blue', joinstyle='round')

    # Set title and labels for axes
    ax.set(xlabel="Date",
        ylabel="Nombre",
        title="Nombre de cas en fonction du temps : "+ where[index])

    # Rotate tick marks on x-axis
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.show()