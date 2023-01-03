#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# - what products are sold at your Staten Island location?
# - what types of seeds are sold at the Brooklyn location.
# - Add a column called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
# - Create a column called  total_value that is equal to price multiplied by quantity.
# - create a new column called  full_description that has the complete description of each product. ( product type and product description)
# 

# In[2]:


df=pd.read_csv(r"C:\Users\HP\Downloads\inventory.csv")
df


# In[38]:


df[df.location=='Staten Island'].product_description


# In[40]:


df[df.location=='Brooklyn'].product_description.unique()


# In[41]:


df['in_stock']=df.quantity.apply(lambda x:True if x>0 else False )
df


# In[43]:


df[' total_value']=df.apply(lambda x:x['quantity']*x['price'],axis=1)
df


# In[52]:


df['full_description']=df.apply(lambda x: x['product_description'] +" , "+x['product_type'],axis=1)
df


# In[ ]:




