from barycenter import Barycenter
from pathlib import Path
import numpy as np
import pandas as pd

class Operator:
    def __init__(self):
        self.barycenter = Barycenter()
        ds = pd.read_csv(Path().joinpath('data', 'Data_test.csv'))
        self.data = np.array([ds['x'], ds['y']]).T
        self.normes = []
        # fin du constructeur

    # Return a list of N lists. (N = number of barycenters)
    # Each List contains the distance between each point and the corresponding barycentre :
    # return [ [dist(point1,bary1),...,dist(pointN,bary1)], ..., [dist(point1,baryN),...,dist(pointN,baryN)] ]
    def norme(self, p_barycenter_number):
        n_rows= self.data.shape[0]
        matrice1 = np.ones((n_rows,1))
        # Generate random barycenters
        barycenter_list = self.barycenter.random_barycenter(p_barycenter_number)
        # Generate a list of index
        indices = [i for i in range(self.data.shape[0])]


        for i in range(p_barycenter_number):
            # Calculate the norm for each point
            column_norme = np.sum(matrice1*((self.data-barycenter_list[i])**2),1)
            # Add to the list : all the norms indexed
            self.normes.append(np.c_[indices, column_norme])

    # Sort each array of self.normes in ascending order
    def sortNorms(self):
        for i in range(len(self.normes)):
            self.normes[i] = self.normes[i][self.normes[i][:,1].argsort()]