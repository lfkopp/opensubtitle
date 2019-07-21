#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
pd.set_option('display.max_columns', 500)
import base64
import numpy as np
import requests
import gzip
from os import listdir
from os.path import isfile, join
from random import shuffle,choice
from time import sleep
import random


# In[18]:





# In[ ]:





# In[22]:


def arruma(series):
    return pd.to_numeric(series, errors='coerse', downcast ='integer')

data = pd.read_pickle('data.pickle')
data['MovieYear'] = arruma(data['MovieYear'])
data['MovieImdbRating'] = arruma(data['MovieImdbRating'])
data = data[data['MovieYear'] > 2010]
data = data[data['MovieImdbRating'] > 6]
data.sort_values(['MovieYear','MovieImdbRating'], ascending=False, inplace=True)

print(data.shape)
data.head() 


# In[24]:


lista = list(data.SubDownloadLink)
shuffle(lista)
lista


# In[28]:


from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()

options.binary_location = '/usr/bin/chromium-browser'
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)
url = lista[0]
driver.get(url)


print(driver.page_source)
driver.close()


# In[ ]:




