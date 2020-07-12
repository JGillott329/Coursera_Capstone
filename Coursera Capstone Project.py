#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests 


# In[30]:


website_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text


# In[31]:


# Start by extracting the HTML data from the wikipedia page using BeautifulSoup

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url, 'xml')
print(soup.prettify())


# In[32]:


# Take the table we are looking to scrape 

My_table = soup.find("table",{"class":"wikitable sortable"})
My_table


# In[33]:


table_rows = My_table.find_all("tr")
table_rows


# In[34]:


# Move the data from the wikipedia page into a Python list 

data = []
for rows in table_rows:
    td = []
    for t in rows.find_all("td"):
        td.append(t.text.strip())
    data.append(td)


# In[35]:


# Use pandas to transfer to a data frame 

import pandas 
df = pandas.DataFrame(data, columns = ["PostalCode", "Borough", "Neighborhood"])
df.head()


# In[36]:


# Remove unwanted rows with no borough or neighborhood assigned 

df.drop(df[df.Borough == "Not assigned"].index, inplace = True)
df.head()


# In[37]:


df.reset_index(drop = True, inplace = True)
df.drop(labels = 0, axis = 0, inplace = True)
df.head()


# In[38]:


# Reset indexes

df.reset_index(drop = True, inplace = True)
df.head()


# In[39]:


df.shape


# In[40]:


url = "http://cocl.us/Geospatial_data"
df_geo = pandas.read_csv(url)
df_geo.head()


# In[41]:


# Rename Postal Code column for consistency 
df_geo.rename(columns = {"Postal Code": "PostalCode"}, inplace = True)
df_geo.head()


# In[42]:


# merge the two data frames 
frames = [df, df_geo]
df_full = pandas.concat(frames)
df_full


# In[43]:


df_full.isnull().sum()


# In[27]:





# In[ ]:




