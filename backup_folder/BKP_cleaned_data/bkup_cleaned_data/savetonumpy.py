#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import os


# In[3]:


allFiles = [files for _,_a,files in os.walk('./faults_current_only/')]
allFiles = allFiles[0]


# In[6]:


TrainData = []
for f in allFiles:
    x = np.loadtxt('./faults_current_only/'+f)
    y = float( f[2:-5] )
    TrainData += [[x,y]]


# In[8]:


TrainData = np.array(TrainData, dtype=object)


# In[9]:


np.save('numpyData',TrainData)

