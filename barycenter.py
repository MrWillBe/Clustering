from pathlib import Path
import numpy.random
import numpy as np
import pandas as pd


class Barycenter:
    def __init__(self):
        ds = pd.read_csv(Path().joinpath('data', 'Data_test.csv'))
        self.indices = ds[["indice"]]
        self.abs = ds[["x"]]
        self.ord = ds[["y"]]
        self.barycenter_list = []
        # End builder

    # Generate random point named barycenter
    def random_barycenter(self, p_barycenter_number):
        random_abs = numpy.random.uniform(np.amin(self.abs), np.amax(self.abs), p_barycenter_number)
        random_ord = numpy.random.uniform(np.amin(self.ord), np.amax(self.ord), p_barycenter_number)
        for i in range(p_barycenter_number):
            self.barycenter_list.append([random_abs[i], random_ord[i]])
        return self.barycenter_list

    # Get the abs from specified barycenter
    def get_abs_barycenter(self, p_line, p_barycenter_number):
        barycenter_list = self.random_barycenter(p_barycenter_number)
        # Used to compare the value of "x" and the original list
        print(barycenter_list)
        # We want as "x" as line
        for i in range(0, p_line):
            # We want "x", not "y"
            for j in range(0, 1):
                # Print the value of "x"
                print("The value corresponding to the line " + str(i) + " from the 'x' column is : " + str(
                    barycenter_list[i][j]))

    # Get the ord from specified barycenter
    def get_ord_barycenter(self, p_line, p_barycenter_number):
        barycenter_list = self.random_barycenter(p_barycenter_number)
        # Used to compare the value of "y" and the original list
        print(barycenter_list)
        # We want as "y" as line
        for i in range(0, p_line):
            # We want "y", not "x"
            for j in range(1, 2):
                # Print the value of "y"
                print("The value corresponding to the line " + str(i) + " from the 'y' column is : " + str(
                    barycenter_list[i][j]))

coucou c'est moi '