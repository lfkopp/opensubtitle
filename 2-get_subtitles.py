#!/usr/bin/env python
# coding: utf-8

# In[15]:


import xmlrpc.client as xrpc
server = xrpc.ServerProxy("http://api.opensubtitles.org/xml-rpc")

import pandas as pd
pd.set_option('display.max_columns', 500)

from time import sleep
from random import shuffle


# In[16]:


#credentials = server.LogIn("omerakgul58", "omeromer", "en", "2016experimentingwithnlp")
credentials = server.LogIn("mrkopp", "mymoviez00", "en", "SubtitleClassification")
token = credentials.get("token")
info = server.ServerInfo()
info['download_limits']['client_download_quota']


# In[23]:


df = pd.read_pickle('final.pickle')
df2 = df[df.startYear >= 2010]
df2 = df2[df2.titleType == 'movie']
df2 = df2[df2.runtimeMinutes > 60]
#df2 = df2[df2.averageRating > 9]
#df2 = df2[df2.numVotes > 50]
print(df2.shape)
df2.sort_values('startYear', ascending=False)


# In[24]:


moviesImdb = list(df2.tconst) #[:8])
print(moviesImdb)


# In[25]:


def get_info(id_imdb):
    data = server.SearchSubtitles(token, [ {'imdbid': int(id_imdb[2:]), 'sublanguageid': 'eng'}])
    try:
        return pd.DataFrame.from_dict(data['data'])
    except:
        return False
get_info('tt5773402')


# In[29]:


len(list(data.IDMovieImdb))


# In[30]:


xlista = [movie for movie in moviesImdb if int(movie[2:]) not in [60317]]
len(xlista)


# In[31]:


try:
    data = pd.read_pickle('data.pickle')
    data.drop_duplicates('IDSubtitleFile',inplace=True)
except:
    data = pd.DataFrame([])
    
lista = list(data.IDMovieImdb)
shuffle(lista)
lista = [int(x) for x in lista]

xlista = [movie for movie in moviesImdb if int(movie[2:]) not in lista]
print(xlista)


# In[7]:


print(len(xlista))


# In[32]:


print(data.shape)
shuffle(xlista)
for movie in xlista[:50000]:
    try:
        data = pd.concat([data,get_info(movie)], sort=False)
        #data.drop_duplicates('IDSubtitleFile',inplace=True)
        #data.to_pickle('data.pickle')
        #print(movie, data.shape)
        #sleep(.03)
    except:
        pass #print('\n---')
data.to_pickle('data.pickle')
print(data.shape)


# In[33]:


data.head(200)


# In[34]:


data.shape


# In[ ]:




