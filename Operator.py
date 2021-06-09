from barycenter import Barycenter
from pathlib import Path
import numpy as np
import pandas as pd
from barycenter_list import Barycenter_List

class Operator:
    pass

    # Return a list of N lists. (N = number of barycenters)
    # Each List contains the distance between each point and the corresponding barycentre :
    # return [ [dist(point1,bary1),...,dist(pointN,bary1)], ..., [dist(point1,baryN),...,dist(pointN,baryN)] ]
    def norme(blist : Barycenter_List):
        normes = []
        data = blist.data

        n_rows= data.shape[0]
        matrice1 = np.ones((n_rows,1))
        # Generate a list of index
        indices = [i for i in range(data.shape[0])]

        print(blist.barycenter_list[0].getCoord().shape)
        print(data.shape)
        for i in range(len(blist.barycenter_list)):
            # Calculate the norm for each point
            column_norme = np.sum(matrice1*((data-blist.barycenter_list[i].getCoord())**2),1)
            # Add to the list : all the norms indexed
            normes.append(np.c_[indices, column_norme])
        return normes

    def attribuer(normes_list):
        # Tableau contenant "n" clusters
        clusters = [[] for i in range(len(normes_list[0]))]
        # Déterminer la plus petite norme de chaque point et les attribuer au cluster correspondant
        # Nombre de lignes
        for i in range(len(normes_list)):
            # Valeur minimale parmi les "n" normes
            minimum = min(normes_list[i])
            # Index de la valeur minimale
            index_min = normes_list[i].index(minimum)
            # Ajout du point dans le cluster correspondant
            clusters[index_min].append(i)
        print(clusters)