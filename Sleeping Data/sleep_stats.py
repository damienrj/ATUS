import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame.from_csv('atus_00003.csv')
df['weighted_sleep']=df.BLS_PCARE_SLEEP * df.WT06
state_group_sum = df.groupby(['YEAR', 'STATEFIP']).sum()

results = state_group_sum.weighted_sleep / state_group_sum.WT06

results = results.unstack(0)

num,name = np.loadtxt('state_id.txt',unpack=True,dtype=str,delimiter=',')

# replace with state names
results.axis = name

sns.heatmap(results-np.mean(results),annot=True)
