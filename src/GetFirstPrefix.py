# -*- coding: utf-8 -*-
"""
Created on Tue May 15 03:54:54 2018

@author: User
"""

import pandas as pd
import re

dataset = pd.read_csv('final_result.csv')
newDataset = pd.DataFrame(columns=['ProjectName','methodName','methodBody','methodBodyLength','TotalMN','Prefix','Rank','AllOccurrance', 'FirstOccurrance', 'LastOccurrance'])

for j in range(0, len(dataset)):
    if dataset['Rank'][j] == 1:
        print(j)
        ProjectName = dataset['ProjectName'][j]
        methodName = dataset['methodName'][j]
        methodBody = dataset['methodBody'][j]
        methodBodyLength = dataset['methodBodyLength'][j]
        TotalMN = dataset['TotalMN'][j]
        Prefix = dataset['Prefix'][j]
        Rank = dataset['Rank'][j]
        occurrance = dataset['AllOccurrance'][j]
        firstOcc =  dataset['FirstOccurrance'][j]
        lastOcc =  dataset['LastOccurrance'][j]
        dict = {'ProjectName': ProjectName, 'methodName': methodName, 'methodBody': methodBody,'methodBodyLength':methodBodyLength, 'TotalMN': TotalMN, 'Prefix': Prefix, 'Rank': Rank , 'AllOccurrance': occurrance, 'FirstOccurrance':firstOcc , 'LastOccurrance':lastOcc}  
        newDataset = newDataset.append(dict, ignore_index= True)


newDataset.to_csv('final_result_first_prefix.csv')       

        