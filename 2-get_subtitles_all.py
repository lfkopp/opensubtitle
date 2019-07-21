#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
pd.set_option('display.max_columns', 500)

import numpy as np
import requests
import gzip


# In[4]:


url =' http://dl.opensubtitles.org/addons/export/subtitles_all.txt.gz'
raw_data = requests.get(url)
with open('subtitles_all.gz', 'wb+') as file:
    file.write(raw_data.content)


# In[ ]:


quotechar 
error_bad_lines 
warn_bad_lines 


# In[10]:


def download_file(url,local_filename):
    #local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
    return local_filename


# In[11]:


download_file(url,'subtitles_all.gz')


# In[14]:


df = pd.read_csv('subtitles_all.gz', compression='gzip', sep=r'\t', engine='python', 
                 quotechar='"', error_bad_lines=False, warn_bad_lines=True )
df.to_pickle('subtitles_all.pickle')
    


# In[15]:


df


# In[16]:


df.shape


# In[18]:


df2 = df[df.MovieKind == 'movie']
df2 = df2[df2.ISO639 == 'en']
df2.shape


# In[19]:


df2


# In[20]:


df2.URL[:2]


# In[21]:


df2.sort_values('ImdbID')


# In[23]:


for d in df.URL[:3]:
    print(d)


# In[ ]:




