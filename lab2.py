#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv("./Desktop/lab-02-titanic-eggchul/titanic.csv")
df


# In[7]:


df.describe()


# In[21]:


import matplotlib.pyplot  as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter('Survived', 'Fare', data = df)
plt.xlabel('Survived')
plt.ylabel('Fare')
#as we can see from the scatter plot below, there is not a strong relationship between 'survied' and 'fare'
#however, people paying higer price were all survived
#therefore, we continue with box plot to analysis


# In[104]:


# the fare those dead paid
df0 = df.loc[df['Survived'] == 0]
df0['Fare']
df00 = df0['Fare'].rename("Dead's Fare")
fig1, ax1 = plt.subplots()
fig1.set_size_inches(10, 5)
ax1.set_title('Fare (Dead)')
ax1.set_yticklabels('Dead')
ax1.boxplot(df00, vert= False)
plt.show()


# In[105]:


# the fare those survived paid
df1 = df.loc[df['Survived'] == 1]
df1['Fare']
df11 = df1['Fare'].rename("Survived's Fare")
fig2, ax2 = plt.subplots()
fig2.set_size_inches(10, 5)
ax2.set_yticklabels('Survived')
ax2.boxplot(df11, vert = False)
plt.show()


# In[87]:


data = [df00, df11]
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = plt.subplot()
#ax.set_xticks([1, 2])
ax.set_xticklabels(['Dead', 'Survived'])
ax.set_ylabel('Fare')
ax.boxplot(data)
plt.show()
#from the box plot below we could find that
#1.the mean fare price of those who failed to survive is lower than those survivors'
#2.non of the dead had a fare at 500

