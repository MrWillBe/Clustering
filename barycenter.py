from pathlib import Path
import numpy.random
import numpy as np
import pandas as pd
import random


class Barycenter:
    def __init__(self, abs_list, ord_list):
        self.abs = numpy.random.uniform(np.amin(abs_list), np.amax(abs_list), 1)
        self.ord = numpy.random.uniform(np.amin(ord_list), np.amax(ord_list), 1)

