# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:55:23 2020

@author: Abdulziz Al Omran
"""


import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] = df ['Start Time'].apply(pd.to_datetime)

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour
# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()
print('Most Frequent Start Hour:', popular_hour[0])
print(df.columns)