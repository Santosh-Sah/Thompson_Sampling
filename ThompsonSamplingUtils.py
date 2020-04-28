# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:34:55 2020

@author: Santosh Sah
"""

"""
importing the libraries
"""

import pandas as pd

# Importing the dataset
def importThompsonSamplingDataset(thompsonSamplingDatasetFileName):
    
    # Importing the dataset
    thompsonSamplingDataset = pd.read_csv(thompsonSamplingDatasetFileName)
    
    return thompsonSamplingDataset
