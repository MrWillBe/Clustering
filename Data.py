import pandas as pd
from pathlib import Path
import numpy as np

ds = pd.read_csv(Path().joinpath('data', 'Data_test.csv'))
data = np.array([ds['x'], ds['y']])
dataT = np.array([ds['x'], ds['y']]).T
abs_list = ds[["x"]]
ord_list = ds[["y"]]
abs = ds["x"]
ord = ds["y"]