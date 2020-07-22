#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np


# In[32]:


a = np.array([[1, 6],
                        [2, 8],
                        [3, 11],
                        [3, 10],
                        [1, 7]])


# In[33]:


mean_a = a.mean(axis = 0)


# In[34]:


mean_a


# In[45]:


a_centered = a - mean_a


# In[46]:


a_centered


# In[47]:


a_centered_sp = (a_centered[:,1]*a_centered[:,0]).sum(axis = 0)


# In[48]:


a_centered_sp / (a_centered.shape[0]-1)


# In[49]:


a.transpose()


# In[41]:


np.cov(a.transpose())

