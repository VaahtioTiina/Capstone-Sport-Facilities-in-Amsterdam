#!/usr/bin/env python
# coding: utf-8

# Toronto Neighborhood Assignment 20191216 - Coursera Data Science Capstone Course

# In[6]:


#import libraries 
import pandas as pd   
import numpy as np


# In[19]:


#read data 
toronto_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0] 
df_toronto = pd.DataFrame(data = toronto_data)
df_toronto.head()


# In[20]:


#Data Preparation
#filter not assigned values 
df_toronto = df_toronto[(df_toronto.Borough!= "Not assigned")]   
#Assign Borough value for the neighborhodos that == Not Assigned 
df_toronto.Neighborhood.replace("Not Assigned",df_toronto.Borough,inplace=True)

#group by Postcode and merge rows  

df_toronto_2 = df_toronto.groupby(by=['Postcode','Borough']).agg(lambda x: ','.join(x))

df_toronto_2.reset_index(level=['Postcode','Borough'], inplace=True)


# In[23]:


# return head tp check neighborhoods are correctly merged
df_toronto_2.head()


# In[24]:


#return shape 
df_toronto_2.shape


# In[ ]:




