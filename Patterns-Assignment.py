#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sub: Write a python code to print the following patterns


# In[18]:


#Pattern 1

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[19]:


#Pattern 2

for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print()


# In[23]:


#Pattern 3

for i in range(6):
    print("* "*i)


# In[69]:


#Pattern 4

for i in range(0,5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()


# In[51]:


#Pattern 5

for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
    


# In[53]:


# Pattern 6

for i in range(5,0,-1):
    print("* "*i)


# In[67]:


# Pattern 7

a=1
b=2
for i in range(4):
    for j in range(1,b):
        print(a,end=" ")
        a+=1
    print()
    b+=1
    


# In[68]:


#Pattern 8

for i in range(6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()


# In[ ]:




