#!/usr/bin/env python
# coding: utf-8

# # TECHNOHACKS TASK 1 - PERFORM DATA CLEANING

# # Importing the libraries and loading the data

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
get_ipython().run_line_magic('', 'matplotlib in line')


# In[2]:


titanic=pd.read_csv("C:/Users/vaish/Downloads/train.csv")
titanic.head()


# In[3]:


titanic.shape


# # Data Cleaning

# In[4]:


titanic.isnull().sum()


# In[5]:


sns.heatmap(titanic.isnull(),cmap='spring')


# In[6]:


sns.boxplot(x='Pclass',y='Age',data=titanic)


# In[7]:


titanic.head()


# In[25]:


titanic.head(3)#dropped the cabin column


# In[26]:


titanic.isnull().sum()


# In[10]:


titanic.head(2)


# In[11]:


pd.get_dummies(titanic['Sex']).head()


# In[12]:


sex=pd.get_dummies(titanic['Sex'],drop_first=True)
sex.head(3)


# In[13]:


embark=pd.get_dummies(titanic['Embarked'])


# In[14]:


embark.head(3)


# In[15]:


embark=pd.get_dummies(titanic['Embarked'],drop_first=True)


# In[16]:


embark.head(3)


# In[17]:


Pcl=pd.get_dummies(titanic['Pclass'],drop_first=True)
Pcl.head(3)


# In[20]:


titanic=pd.concat([titanic,sex,embark,Pcl],axis=1)


# In[21]:


titanic.head(3)


# In[22]:


titanic.drop(['Name','PassengerId','Pclass',"Ticket",'Sex','Embarked'],axis=1,inplace=True)


# In[23]:


titanic.head(3)

