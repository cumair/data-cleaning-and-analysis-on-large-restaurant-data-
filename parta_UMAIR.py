# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 02:11:42 2019

@author: mkalo
"""

'''********************************
         UMAIR CHAANDA
DSC 450   TAKE HOME FINAL    PART-A
***********************************'''

'''I HANDLED 3 SPECIAL CASES THAT ARE UNLIKE ALL OTHER DATA 
BY CHANGING 3 DATA ROWS IN zagats.txt FILE TO SUIT MY PATTERN
PLEASE USE zagats.txt TO RUN THE CODE WHICH IS BEING SUBMITTED 
ALONG WITH OTHER ASSIGNMENT SUBMISSION FILES'''

import numpy as np
import pandas as pd
import re
import json

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
print(zagat.to_string())


#zagat_data.ix[rname.iloc[:,0].isnull()]
#zagat_data.ix[address.iloc[:,0].isnull()]
#zagat_data.ix[city.iloc[:,0].isnull()]
#zagat_data.ix[phoneAndcuisine.iloc[:,0].isnull()]

