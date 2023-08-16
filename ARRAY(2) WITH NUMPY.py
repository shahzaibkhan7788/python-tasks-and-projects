#!/usr/bin/env python
# coding: utf-8

# # Arrays and its inbuilt functions

# In[8]:


import numpy as np


# In[10]:


np.linspace(1,10,50)
## Try to check its syntax...then check its working ...i think it will produce a 
##random array....


# In[11]:


## Try to do something more interestong ...use of copy function and 
### and broadcasting.....
###Example of multi array....
lst1=[1,2,3,4,5]
lst2=[3,4,5,6,7]
lst3=[3,4,6,7,7]
arr=np.array([lst1,lst2,lst3])
arr


# In[12]:


lst1


# In[23]:


### Accessing the array elements....
arr=np.array([1,2,3,4,5,6,7,8])
arr[3]


# In[25]:


arr[3:]=100
arr
## this is the copy function and broadcasting....Using this function we can 
## Replace an elements...


# In[26]:


##Now we want to assign the whole aray to the arr1...
arr1=arr
arr1


# In[30]:


arr1[3:]=400
arr1


# In[31]:


arr
### Here is a difference between python and c and c++ language that it update 
## all the elements ...Array is a reference type not a value type...


# In[ ]:


### But we can prevent this..that your array should not be updated....Arr will be 
## stored in one position and arr1 will store at another position....


# In[ ]:


##Use of copy function for this purpose...
arr1=arr.copy


# In[32]:


print(arr)
arr1[3:]=340
print(arr1)
##So arr is not updated....


# In[33]:


arr


# In[35]:


##Some condition are very useful in ecploratory data analysis....
##Define a variable
## it check it each elements..
val=2
arr<2


# In[42]:


arr[arr<10]
##it will show all the elements where the conditon satisfaied...
##You can also write multiple conditions...inside the square braces...
##arr*2


# In[49]:


##arr/2
###We can use arange to quickly form an array...
arr1=np.arange(0,10).reshape(5,2)
arr1


# In[50]:


##arr%2
##arr/2
###We can use arange to quickly form an array...
arr2=np.arange(0,10).reshape(5,2)
arr2


# In[51]:


arr1*arr2


# In[ ]:


###Now there is another function..that is np.ones...


# In[52]:


np.ones(5)
## this is the function where alll the elements of the array is replaced by 1..


# In[54]:


np.ones(5,dtype=int)
##Always check its syntax.....


# In[55]:


np.ones((2,5),dtype=float)


# In[57]:


##Now we apply random functions.....
## This will give you random value ..by default give you from 0 to 1
np.random.rand(3,3)
##This random distribution always change...


# In[ ]:


###There is another function....which is called randn...
##Check the playlist of "standard normal" distribution...it is statistical problems...


# # Check the playlist of standard normal distribution.

# In[61]:


example=np.random.randn(4,4)
## This is one of the important function ..but to understand it check the playlist..
example


# In[64]:


import seaborn as sns
import pandas as pd
##This will be explained in the next videos....


# In[ ]:


###Try other funcions like randint ....


# In[65]:


np.random.randint(0,100,8)


# In[66]:


np.random.randint(0,100,8)


# In[67]:


np.random.randint(0,100,8).reshape(4,2)


# In[ ]:


##There is another funcion which is random sample....


# In[71]:


## try random_sample function....np.random.random_sample(1,5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




