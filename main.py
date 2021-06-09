import numpy as np
import pandas as pd
from pathlib import Path
from barycenter_list import Barycenter_List
from Operator import Operator

# Initialisation de la data_sheet
ds = pd.read_csv(Path().joinpath('data', 'Data_test.csv'))
data = np.array([ds['x'], ds['y']])

# Création des barycentres
barycenter_list = Barycenter_List(2)

# Création de la liste des normes de chaque point par rapport aux "n" barycentres
normes_list = []
for i in range(data.shape[1]):
    normes_list.append(Operator.norme(barycenter_list, data[0][i], data[1][i]))
# print(normes_list)

# On attribue les points à des clusters
Operator.attribuer(normes_list)