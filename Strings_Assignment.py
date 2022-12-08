#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a python program to convert a string to lower case


# In[3]:


s="Dharani"
s.lower()


# In[4]:


#Write a python program to convert only odd indexed characters to lower case


# In[35]:


s="PYTHON"
m=" "
for i in range(len(s)):
    if i%2==0:
        m=m+s[i].upper()
    else:
        m=m+s[i].lower()
m


# In[36]:


# Write a python program to convert only even indexed characters to lower case , Output: - pYtHoN


# In[96]:


s="PYTHON"
n=" "
for i in range(len(s)):
    if i%2==0:
        n=n+s[i].lower()
    else:
        n=n+s[i].upper()
n


# In[39]:


#Write a python program to convert only odd indexed characters to upper case , Output: pYtHoN


# In[97]:


u="python"
l=" "
for i in range(len(s)):
    if i%2==0:
        l=l+u[i].lower()
    else:
        l=l+u[i].upper()
l


# In[43]:


# Write a python program to convert only even indexed characters to upper case , Output: - PyThOn


# In[98]:


u="python"
l=" "
for i in range(len(s)):
    if i%2==0:
        l=l+u[i].upper()
    else:
        l=l+u[i].lower()
l


# In[46]:


#Write a python program where you have different variable which contains your 
#name, gender, age, phone number, father’s name and mother’s name.
#And by using this variable create a variable named bio-data where you will use all
#this variable


# In[150]:


bio_data={"name":"Dharani",
          "gender":"Female",
          "age":21,
          "phn_num":12345,
          "f_name":"simhachalam",
          "m_name":"anu"}
print("this is",bio_data["name"]," and my age is",bio_data["age"],"nd phn num is",bio_data["phn_num"],"nd im a",bio_data["gender"],"so my father is",bio_data["f_name"],"nd my name is",bio_data["m_name"])


# In[49]:


# Write a python program to count how many times “@” occurred


# In[115]:


E='S@ndhy@'
E.count('@')


# In[60]:


#Write a python program to get only names from the string


# In[138]:


s="name1.@gmail.com, name2.@gmail.com, name3.@gmail.com"
b=s.split(".@gmail.com")
b
c=" ".join(b)
c


# In[69]:


#Write a program to remove vowels from the entire alphabets


# In[140]:


s="abcdefghijklmnopqrstuvwxyz"
d=['a','e','i','o','u']
e=""
for i in s:
    if i not in d:
        e=e+i
print(e)      


# In[105]:


#Find all occurrences of a substring in a given string by ignoring the case


# In[145]:


str1 = "Welcome to Innomatics. innomatics awesome, isn't it?"
s=str1.lower()
d=s.count("innomatics")
print("the innomatics count is",d)


# In[ ]:




