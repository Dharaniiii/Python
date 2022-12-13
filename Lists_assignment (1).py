#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to sum all the items and multiply all the items 


# In[2]:


l=[1,2,3,4,5]
x=0
y=1
for i in l:
    x+=i
    y*=i
print("sum=",x)
print("mul=",y)


# In[ ]:


#2. Write a Python function that takes two lists and returns True if they have at least one common member.


# In[3]:


l1=[1,2,3,4,5]
l2=[6,7,8,9] 
for i in l1:
    for j in l2:
        if i==j:
            print("true")
else:
            print("none")


# In[ ]:


#3. Write a Python program to compute the difference between two lists.


# In[4]:


a= ["red", "orange", "green", "blue", "white"]
b=["black", "yellow", "green", "blue"] 
c=set(a)-set(b)
print('color1-color2:',list(c))
d=set(b)-set(a)
print('color2-color1:',list(d))


# In[ ]:





# In[ ]:




