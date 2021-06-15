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

    def create_barycenter(self, nbr_barycentre):
        for i in range(nbr_barycentre):
            self.barycenter_list.append(Barycenter(Data.abs_list, Data.ord_list))


