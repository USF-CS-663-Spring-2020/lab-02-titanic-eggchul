#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv("./Desktop/lab-02-titanic-eggchul/titanic.csv")
df


# In[7]:


df.describe()


# In[9]:


import matplotlib.pyplot  as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter('Survived', 'Fare', data = df)
plt.xlabel('Survived')
plt.ylabel('Fare')
#as we can see from the scatter plot below, there is not a strong relationship between 'survied' and 'fare'
#however, people paying higer price were all survived


# In[ ]:




