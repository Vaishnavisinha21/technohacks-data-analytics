#!/usr/bin/env python
# coding: utf-8

# # TECHNOHACKS TASK 3- VISUALIZATION USING HISTOGRAM

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


iris=pd.read_csv("C:/Users/vaish/Downloads/Iris (1).csv")


# In[3]:


iris.head()


# In[4]:


iris.describe()


# In[5]:


iris.columns


# In[6]:


iris[[ 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].hist(bins=22, figsize=(22,22))


# In[7]:


iris.hist(figsize=(30,20))
plt.show()


# In[8]:


sns.distplot(iris['SepalLengthCm'])
plt.title('SepalLengthCm Histogram')


# In[9]:


sns.distplot(iris['SepalWidthCm'])
plt.title('SepalWidthCm Histogram')


# In[10]:


sns.distplot(iris['PetalLengthCm'])
plt.title('PetalLengthCm Histogram')


# In[11]:


sns.distplot(iris['PetalWidthCm'])
plt.title('PetalWidthCm Histogram')


# In[ ]:




