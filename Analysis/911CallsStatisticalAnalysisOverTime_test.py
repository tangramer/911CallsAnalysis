'''
This is a test module to test 911CallsStatisicalAnalysisOverTime module's functionality
'''

import 911CallsStatisticalAnalysisOverTime as ca
import numpy as np
import pandas as pd


#test data clean process functionality.
def test_dataClean():
    '''exception test to check for nan values.
       The function takes in a dataframe that has some columns with missing values
       or Nan values as an argument and then tries to throw a ValueError. If a
       ValueError is caught, the output is pass
    '''
    data1 = pd.read_csv("C:/Users/Runbang Tang/Downloads/Road_Weather_Information_Stations.csv",nrows=500)
    
    try:
        ca.dataClean(data1)
    except ValueError:
        pass

#exception test to Check that if after data cleaning, the data are in the correct form.
def test_rightForm():
    '''exception test to Check if data cleaning process works properly. If TyprError 
    is caught, the output is pass
    '''
    data2 = pd.read_csv("C:/Users/Runbang Tang/Downloads/Seattle_Real_Time_Fire_911_Calls2.csv",nrows=1000)
    df2 = ca.dataProcess(data2)
    try:
        ca.dataRight(df2)
    except TypeError:
        pass

