
# coding: utf-8

# In[15]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.style.use('ggplot')


                EMPSTAT		Labor force status
01		Employed - at work
02		Employed - absent
03		Unemployed - on layoff
04		Unemployed - looking
05		Not in labor force
99		NIU (Not in universe)
                
# In[49]:

df = pd.DataFrame.from_csv('atus_00003.csv')
df['weighted_sleep']=df.BLS_PCARE_SLEEP * df.WT06
df.EMPSTAT.astype('category')
df.iloc[0:10]


# In[34]:

state_group_sum = df.groupby(['YEAR', 'STATEFIP']).sum()

results = state_group_sum.weighted_sleep / state_group_sum.WT06

results = results.unstack(0)

results.plot()
results.describe()
#plt.figure()
#plt.plot(results[1,1], results[1,1])


# In[85]:

state_age_sum = df.groupby(['YEAR', 'STATEFIP', 'EMPSTAT']).sum()
results = state_age_sum.weighted_sleep / state_age_sum.WT06
results = results.unstack(0)
results


# In[ ]:




#### 
