import random
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib import pyplot
import Data
from barycenter_list import Barycenter_List
from Operator import Operator
from Data import *

clusters_number = input("Saisissez le nombre de clusters que vous désirez : ")

# Initialisation de la data_sheet
data = Data.data

# Initialisation d'un compteur d'itérations
compteur = 0
stop = False

coord_abs = []
tab_abs = []
tab_ord = []

while stop == False and compteur < 1_000:
    # Test
    print("Iteration numéro :", compteur)

    # Création des premiers barycentres aléatoirement
    if compteur == 0:
        barycenters = Barycenter_List(int(clusters_number))
        size = len(barycenters.barycenter_list)
    # Calculs des nouveaux barycentres
    else:
        barycenters, barycenters_old = Operator.average(clusters, data, barycenters)
        size = len(barycenters.barycenter_list)

    # Test
    # print("Les coordonnées des", clusters_number, "clusters sont 😊
    # for i in range(size):
    #     print(barycenters.barycenter_list[i].getcoord())

    # Création de la liste des normes de chaque point par rapport aux "n" barycentres
    normes_list = []
    for i in range(data.shape[1]):
        normes_list.append(Operator.norme(barycenters, Data.data[0][i], Data.data[1][i]))

    # Test
    # print(normes_list)
    # On attribue les points à des clusters
    clusters = Operator.attribuer(normes_list)

    # Test
    # print("Le tableau contenant les", clusters_number, "clusters est le suivant 😊
    # print(clusters)

    if compteur > 0:
        stop = Operator.end(barycenters_old, barycenters)

    # print("clusters:", clusters)

    # print('-----------------------------')

    # print('-----------------------------')

    compteur += 1

for i in range(len(clusters)):
    tab_abs_memory = []
    tab_ord_memory = []
    for j in range(len(clusters[i])):
        point_abs = Data.abs[clusters[i][j]]
        point_ord = Data.ord[clusters[i][j]]
        tab_abs_memory.append(point_abs)
        tab_ord_memory.append(point_ord)
    tab_abs.append(tab_abs_memory)
    tab_ord.append(tab_ord_memory)

colors = []
for i in range(len(tab_abs)):
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    colors.append(color)
    pyplot.scatter(tab_abs[i], tab_ord[i], c=colors[i])

pyplot.show()
