# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:46:48 2019

@author: mkalo
"""

'''********************************
         UMAIR CHAANDA
DSC 450   TAKE HOME FINAL    PART-B
***********************************'''

import numpy as np
import pandas as pd
import re
import json
import sqlalchemy, os


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


'''**********************************
          USING SQLAlchemy
*************************************'''


from sqlalchemy import create_engine
filename="dsc450.db"
if os.path.exists(filename):
    os.remove(filename)
engine = create_engine('sqlite:///dsc450.db', echo=True)
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

query = zagat.to_sql('Restaurants', con=engine, if_exists='replace')
#result = engine.execute("SELECT * FROM Restaurants").fetchall()

#Find the count of restaurants based on city and cuisine
query1 = engine.execute("SELECT city, cuisine, count(*) FROM Restaurants GROUP BY city, cuisine").fetchall()
for i in query1:
    print(i)


#DROP TABLE Restaurants IF EXISTS
sql = text('DROP TABLE IF EXISTS Restaurants;')
result = engine.execute(sql)







