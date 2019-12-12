# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:27:47 2019

@author: mkalo
"""

'''********************************
         UMAIR CHAANDA
DSC 450   TAKE HOME FINAL    PART-C
***********************************'''

'''I HANDLED 10 SPECIAL CASES THAT ARE UNLIKE ALL OTHER DATA 
BY CHANGING 10 DATA ROWS IN fodors.txt FILE TO SUIT MY PATTERN
PLEASE USE fodors.txt TO RUN THE CODE WHICH IS BEING SUBMITTED 
ALONG WITH OTHER ASSIGNMENT SUBMISSION FILES'''

import numpy as np
import pandas as pd
import re, os
import json


'''********************************
  zagats.txt DATAFRAME FROM PART-A
***********************************'''
#READING .txt FILE INTO PANDAS DATAFRAME
filename = 'zagats.txt'
zagat_data = pd.read_csv(filename, header=None)
zagat_data.columns = ['line']


#FETCHING rname COLUMN
rname = zagat_data['line'].str.extract(
        r'^([^\d]*)(\d.*)$', 
        expand=True)
rname.columns = ['rname','line']


#FETCHING address COLUMN
address = rname['line'].str.extract(
        r'^([0-9]{1,6}.*(?:Blvd\.|Ave\.|PCH|Broadway|Plaza|Walk|level|Dr\.|Rd\.|St\.|Way\.|Way|West\.|Pkwy\.|fl\.|Court|Sq\.|Hwy\.|Circle\.|Ln\.))', 
        expand=True)
address.columns = ['address']


#FETCHING city COLUMN
city_str = rname['line'].str.extract(
        r'(?=(?:Blvd\.|Ave\.|PCH|Broadway|Plaza|Walk|level|Dr\.|Rd\.|St\.|Way\.|Way|West\.|Pkwy\.|fl\.|Court|Sq\.|Hwy\.|Circle\.|Ln\.)(?s)(.*$))', 
        expand=True)
city_str.columns = ['city_str']

city = city_str['city_str'].str.extract(
        r'(.*)(?:\d{3}\-\d{3}\-\d{4})', 
        expand=True)
city.columns = ['city']


#FETCHING phone and cuisine COLUMN
phoneAndcuisine = rname['line'].str.extract(
        r'(?=(\d{3}\-\d{3}\-\d{4})(?s)(.*$))', 
        expand=True)
phoneAndcuisine.columns = ['phone','cuisine']


#zagat DATAFRAME WITH ALL COLUMNS
zagat = pd.concat([rname['rname'], address, city, phoneAndcuisine], axis=1)


'''********************************
       fodors.txt DATASET
***********************************'''
#READING .txt FILE INTO PANDAS DATAFRAME
filename2 = 'fodors.txt'
fodors_data = pd.read_csv(filename2, header=None)
fodors_data.columns = ['line']


#FETCHING rname COLUMN
rname2 = fodors_data['line'].str.extract(
        r'^([^\d]*)(\d.*)$', 
        expand=True)
rname2.columns = ['rname','line']


#FETCHING address COLUMN
address2 = rname2['line'].str.extract(
        r'^([0-9]{1,6}.*(?:Blvd\.|Ave\.|PCH|Broadway|Plaza|Condominium|Plaza\.|Walk|level|St\.|Dr\.|Drive|Rd\.|Way\.|Way|West\.|Pkwy\.|fl\.|Court|Sq\.|Hwy\.|Circle\.|Circle|Cienega|Sts\.|Center|Pl\.|Road|Mall|Mason|Northpoint|La\.|Central\sPark\sS|South\sPark|Redwood\sAlley|Atlanta\.|Ravinia\.|Marcus\.|Sq\.|Flamingo\.|Stars\.|Ln\.))',
        expand=True)
address2.columns = ['address']


#FETCHING city COLUMN
city_str2 = rname2['line'].str.extract(
        r'(?=(?:Blvd\.|Ave\.|PCH|Broadway|Plaza|Condominium|Plaza\.|Walk|level|St\.|Dr\.|Drive|Rd\.|Way\.|Way|West\.|Pkwy\.|fl\.|Court|Sq\.|Hwy\.|Circle\.|Circle|Cienega|Sts\.|Center|Pl\.|Road|Mall|Mason|Northpoint|La\.|Central\sPark\sS|South\sPark|Redwood\sAlley|Atlanta\.|Ravinia\.|Marcus\.|Sq\.|Flamingo\.|Stars\.|Ln\.)(.*$))',
        expand=True)
city_str2.columns = ['city_str']

city2 = city_str2['city_str'].str.extract(
        r'(Los\sAngeles|Studio\sCity|Beverly\sHills|Malibu|Santa\sMonica|Sherman\sOaks|West\sHollywood|Pacific\sPalisades|Bel\sAir|Toluca\sLake|Los\sFeliz|New\sYork|Brooklyn|Atlanta|Las\sVegas|S\sLas\sVegas|San\sFrancisco)',
        expand=True)
city2.columns = ['city']


#FETCHING phone AND cuisine COLUMNS
phoneAndcuisine2 = rname2['line'].str.extract(
        r'(?=(\d{3}\/\d{3}\-\d{4}\s.*\s\d{3}\/\d{3}\-\d{4}|\d{3}\/\d{3}\-\d{4}|\d{3}\/\s\d{3}\-\d{4}|\d{3}\/\d{3}\-\w{4}|\d{3}\/\d{3}\--\d{4})(?s)(.*$))', 
        expand=True)
phoneAndcuisine2.columns = ['phone','cuisine']
phoneAndcuisine2['phone'] = phoneAndcuisine2['phone'].str.replace('/','-')
phoneAndcuisine2['phone'] = phoneAndcuisine2['phone'].str.replace('--','-')
phoneAndcuisine2['phone'] = phoneAndcuisine2['phone'].str.replace('- ','-')


#fodors DATAFRAME WITH ALL COLUMNS
fodors = pd.concat([rname2['rname'], address2, city2, phoneAndcuisine2], axis=1)
print(fodors.to_string())


'''********************************
      FIND MATCHING PAIRS
***********************************'''
#MERGE zagat AND fodors DATAFRAMES ON phone
match_pairs = pd.merge(zagat, fodors, on='phone')

#WRITE MATCHING PAIRS INTO Matching.txt FILE
tfile = open('Matching.txt', 'w')
tfile.write(match_pairs.to_string())
tfile.close()





#fodors_data.ix[address2.iloc[:,0].isnull()]
#fodors_data.ix[city_str2.iloc[:,0].isnull()]
#fodors_data.ix[city2.iloc[:,0].isnull()]
#fodors_data.ix[phoneAndcuisine2.iloc[:,0].isnull()]
#fodors_data.ix[rname2.iloc[:,0].isnull()]



