from pathlib import Path
import numpy.random
import numpy as np
import pandas as pd
from pathlib import Path
import numpy as np
import pandas as pd

import Data
from barycenter import Barycenter


class Barycenter_List:
    def __init__(self, nbr_barycentres):
        self.barycenter_list = []
        self.create_barycenter(nbr_barycentres)


        # End builder

    def create_barycenter(self, nbr_barycentre):
        for i in range(nbr_barycentre):
            self.barycenter_list.append(Barycenter(Data.abs_list, Data.ord_list))

    # Get the abs from specified barycenter
    def get_abs_barycenter_list(self, p_line, p_barycenter_number):
        barycenter_list = self.random_barycenter(p_barycenter_number)
        # Used to compare the value of "x" and the original list
        print(barycenter_list)
        # We want as "x" as line
        for i in range(0, p_line):
            # Print the value of "x"
            self.barycenter_abs_list.append([barycenter_list[i][0]])
        print(self.barycenter_abs_list)

    # Get the ord from specified barycenter
    def get_ord_barycenter_list(self, p_line, p_barycenter_number):
        barycenter_list = self.random_barycenter(p_barycenter_number)
        # Used to compare the value of "y" and the original list
        print(barycenter_list)
        # We want as "y" as line
        for i in range(0, p_line):
            # Print the value of "y"
            self.barycenter_ord_list.append([barycenter_list[i][1]])
        print(self.barycenter_ord_list)