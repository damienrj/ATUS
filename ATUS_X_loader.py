# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 16:02:46 2015

@author: damienrj
"""
import numpy as np
import pandas as pd
caseid=[]
year = []
state_fip = []
person_num = []
person_line_num = []
weight = [] 
time_looking = [] 
with open('atus_00001.dat', 'r') as f:
    for line in f:
        caseid.append(int(line[0:14]))
        year.append(int(line[14:14+5]))
        state_fip.append(int(line[19:21]))
        person_num.append(int(line[21:23]))
        person_line_num.append(int(line[23:26]))
        weight.append(float(line[26:43]))
        time_looking.append(int(line[43:47]))
 
data = {'case_id' : caseid, 'year' : year, 'FIP' : state_fip, 'Person_num' : person_num, 'Person_lin_num' : person_line_num, 'Weight' : weight, 'Time_looking' : time_looking}
df = pd.DataFrame(data)
groups = df.groupby('FIP')

result = groups.sum()