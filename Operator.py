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

    # Sort each array of self.normes in ascending order
    def sortNorms(ls : list):
        for i in range(len(ls)):
            ls[i] = ls[i][ls[i][:,1].argsort()]