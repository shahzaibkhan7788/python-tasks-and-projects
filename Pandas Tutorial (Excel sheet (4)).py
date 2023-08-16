#!/usr/bin/env python
# coding: utf-8

# # Pandas tutorial

# Pandas is an open source , BSD -licensed library providing high performance 
# easy to use data structures and data analysis tools for the python programming 
# language

# Agenda....
# what is data frames....
# what is data series...
# different operation in pandas..
# 
# 
# Both pandas and Numpy library is very imporant for practice....these two are the most important loibraries......

# ##First of all import pandas library....
# What is data frames ?
# Suppose you are given an excel sheet or other documents ..But each will have 
# different types of  features ...if i read the particulart data form that sheet
# then i can basically use the pandas...and pandas will actually load that data 
# and after loading that data it gets usually...converted that data into data frame...
# Data frame is a combination of col and reows ..it will show you repesentation format...
# where how your data looks like in the excel sheet ...in the same way...it will be loaded
# 

# In[1]:


##First of all we can create a data frames and then load it..
##df ..for data frame
import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["row1",'row2','row3','row4','row5'],columns=['col1','col2','col3','col4'])
##  Here we can form an excel sheet...it is two dimesnional....
##Here index show the number of rows ...
##While column show the number of columns..
## Here np.arange is an inbuilt function used to take value form 0 to 20..
##Reshape function will give shape ..distribute it in row and cols...
##Remember that as you want to create a data frame..then you can add three
##Things ..one is data ..other is rows..and third is columns...
df.head()


# In[3]:


##This is an excel sheet...Here we can use inbuilt function name as df.head...
##It is used to generate an excel sheet....
##We can also convert this into an excel sheet....it will be open in a new tab...
##We can use an inbuilt funcion...
df.to_csv("Test1.csv")        ###this is an inbuilt function.....Test1.csv is the name of the file##
##Now go to file ...click oprion...check name of the file....


# ##Acessing an elements of the data frames...
# ##There are two ways to access the data frames..one is...
# ## 1) .loc...................show location
# ## 2) .iloc........show index location...

# In[4]:


df.loc["row1"]
##This will show you the first row...


# In[5]:


type(df.loc["row1"])
##We will see the series in a data series ...
##For a data frame there must be at least two rows or greater and same for
##Columns...
##But if we consider one row or col..then it is called a series..series it either
##one row or one column...


# In[6]:


##Now we use to check iloc....this will work as numpy array...left side will give 
##you row and right side will give you columns...
df.iloc[:,:]


# In[8]:


###If we need first three row and first two columns..then
df.iloc[0:3,0:2]
#3Each index start from zero..


# In[9]:


type(df.iloc[0:3,0:2])
#3NBow check the difference ..since thismultui dimensional ..so it is ...dataframes..


# In[10]:


##Try to note difference between data frame and series...
type(df.iloc[0:2,0:1])
##Because it has two rows ..and 1 col


# In[11]:


(df.iloc[0:2,0:1])


# In[15]:


(df.iloc[0:2,0])


# In[16]:


type(df.iloc[0:2,0])
#3If there is at least more than one col...it become a data frame..but the given
##show the series beacuse ot is one col...


# In[18]:


##Take some more elements from col2...and onward...
df.iloc[:,1:]


# In[20]:


##  Here is an important funciton..itr will convert data frame into arrasy...
df.iloc[:,1:].values
##It means that name lke row and columns will dissappear...


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




