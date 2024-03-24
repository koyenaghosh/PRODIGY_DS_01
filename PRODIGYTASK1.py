#!/usr/bin/env python
# coding: utf-8

# # Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',None)


# In[57]:


d1=pd.read_csv('heartdata.csv')


# In[58]:


d1=d1.drop(['age.1','cholesterol','gluc','active','cardio'],axis=1)
#d1['gender']=d1['gender'].replace({1:'M',2:'F'})


# In[59]:


d1


# In[71]:


cols=['age','gender']
d1[cols].hist(figsize=(20,5))
plt.show()


# In[ ]:




