# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 14:20:55 2015

@author: damienrj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns

#Set the display precision
pd.set_option('precision', 4)

df = pd.DataFrame.from_csv('atus_00004.csv')
df['weighted_sleep']=df.BLS_PCARE_SLEEP * df.WT06
df.EMPSTAT.astype('category')
df['SEX'] = df['SEX'].replace([1, 2], ['Male', 'Female'])
df.SEX.astype('category')
df.AGE = pd.cut(df.AGE, [15, 20, 25, 35, 45, 55, 65, 90], right = 'False')

#Load the state names
num,name = np.loadtxt('state_id.txt',unpack=True,dtype=str,delimiter=',')

# replace with state names
df['STATEFIP'] = df['STATEFIP'].replace(num.astype(np.int64), name)


age_sum = df.groupby(['YEAR',  'AGE', 'SEX' ]).sum()
results = age_sum.weighted_sleep / age_sum.WT06
results = results.unstack(0)/60

f = plt.figure(figsize=(12, 8))
data = results[2013].unstack(1)
data.plot(ax=f.gca(), kind='bar', ylim=(7,10), y = ['Male', 'Female'])
print(data)

#This section finds the number of people in eac state, each year. 
grouped_state = df.groupby(['YEAR', 'STATEFIP'])
num_per_state = grouped_state.size()
num_per_state = num_per_state.unstack(0)

d = {'Mean' : num_per_state.mean(1), 'STD' : num_per_state.std(1)}
pd.DataFrame(d)


#This section groups the data by metro area
grouped = df.groupby(['YEAR', 'METAREA', 'SEX' ] )
num_LA_NY=grouped.size().unstack(0).loc[[4481, 5601]]
results = grouped.weighted_sleep.sum() / grouped.WT06.sum()
results = results.unstack(0)/60
la_ny_sleep = results.loc[[4481, 5601]]
la_ny_sleep = la_ny_sleep.rename(index={4481:"LA Metro", 5601: "NY Metro"})
la_ny_sleep = la_ny_sleep.stack(0).unstack(1)



f = plt.figure()
f.gca().get_xaxis().get_major_formatter().set_useOffset(False)
la_ny_sleep['Male'].unstack(0).plot(ax = f.gca())
plt.ylabel("Hours Slept")

