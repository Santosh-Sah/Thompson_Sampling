# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:35:47 2020

@author: Santosh Sah
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
Visualizing ThompsonSampling result
"""
def visualisingThompsonSamplingResult():
    
    thompsonSamplingResult = pd.read_csv("advertisementsSelected.csv")
    
    plt.hist(thompsonSamplingResult.values)
    plt.title('Histogram of the advertisement selected')
    plt.xlabel('Advertisement')
    plt.ylabel('Number of times each advertisement was selected')
    
    plt.savefig("Thompson_Sampling_result.png")
    
    plt.show()

if __name__ == "__main__":
    visualisingThompsonSamplingResult()