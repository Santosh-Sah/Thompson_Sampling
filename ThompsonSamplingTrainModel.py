# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:35:29 2020

@author: Santosh Sah
"""

import random
import pandas as pd
from ThompsonSamplingUtils import (importThompsonSamplingDataset)

#train ThompsonSampling model
def trainThompsonSampling():
    
    thompsonSamplingDataset = importThompsonSamplingDataset("Ads_CTR_Optimisation.csv")
    
    #number of times the different advertisement shown to the users on the social media.
    N = 10000
    
    #number of version of the advertisement
    d = 10
    
    #different versions of advertisements selected
    advertisementsSelected = []
    
    #there are three steps present in the training of trainUpperConfidenceBound.
    #We are creating a model which used to select the best advertisement of a company.
    #step 1
    #the number of times the ad i got reward 1 up to round n
    #first is the number of times the ad i was selected up to round n
    #second is the number of times the ad i was selected up to round n
    numberOfRewards_1 = [0] * d
    numberOfRewards_0 = [0] * d
    totalRewards = 0
    
    #step 2
    #for each ad i we take a random draw from the distribution
    for n in range(0, N):
        
        advertisementWithMaxRandom = 0
        
        maximumRandom = 0
        
        for i in range(0, d):
            
            #generate the random draw for these 10 advertisement.
            #random draws from the beta distribution.
            randomBeta = random.betavariate(numberOfRewards_1[i] + 1, numberOfRewards_0[i] + 1)
            #step 3
            #select the ad i that has the maximum upper confidence bound
            if randomBeta > maximumRandom:
                
                maximumRandom = randomBeta
                
                advertisementWithMaxRandom = i
        
        advertisementsSelected.append(advertisementWithMaxRandom)
        
        #calculate rewards
        rewards = thompsonSamplingDataset.values[n, advertisementWithMaxRandom]
        
        #update numberOfRewards_1 and numberOfRewards_0
        if rewards == 1:
            
            numberOfRewards_1[advertisementWithMaxRandom] = numberOfRewards_1[advertisementWithMaxRandom] + 1
        
        else:
            
            numberOfRewards_0[advertisementWithMaxRandom] = numberOfRewards_0[advertisementWithMaxRandom] + 1
        
        totalRewards = totalRewards + rewards
    
    advertisementsSelectedDataframe = pd.DataFrame(advertisementsSelected)
    
    #we need to see the last record of the below csv files. It will contains the index of the advertisement which is best among all.
    #selected advertisement index will be 4
    advertisementsSelectedDataframe.to_csv("advertisementsSelected.csv", index = False)
        
        
if __name__ == "__main__":
    trainThompsonSampling()