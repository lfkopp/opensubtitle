#!/usr/bin/env python
# coding: utf-8

# In[1]:


file_path = get_ipython().getoutput('pwd  #%cd%')
print(file_path)


# In[2]:


import pandas as pd
pd.set_option('display.max_columns', 500)

import numpy as np
import requests
import base64
import gzip


# In[3]:


for dataset in ['basics','ratings']: #,'akas']:
    raw_data = requests.get('https://datasets.imdbws.com/title.'+dataset+'.tsv.gz')
    with open(dataset+'.gz', 'wb+') as file:
        file.write(raw_data.content)
    df = pd.read_csv(dataset+'.gz', compression='gzip', sep=r'\t', engine='python')
    df.to_pickle(dataset+'.pickle')


# In[4]:


basics = pd.read_pickle('basics.pickle')
ratings = pd.read_pickle('ratings.pickle')
#akas = pd.read_pickle('akas.pickle')


# In[5]:


basics.head()


# In[6]:


ratings.head()


# In[7]:


final = pd.merge(basics,ratings, on='tconst')


# In[8]:


final.plot.scatter('averageRating','numVotes',alpha=0.1, figsize=(15,15))


# In[9]:


final.dtypes


# In[10]:


#final['genres'] = final['genres'].str.split(',')


# In[11]:


final.titleType.unique()


# In[12]:


def arruma(series):
    return pd.to_numeric(series, errors='coerse', downcast ='integer') #.fillna(0).astype(int).replace(0,'')


# In[13]:


final['isAdult'] = final['isAdult'].astype(bool)
final['runtimeMinutes'] = arruma(final['runtimeMinutes'])
final['startYear'] = arruma(final['startYear'])
final['endYear'] = arruma(final['endYear'])


# In[14]:


final.to_pickle('final.pickle')
final.dtypes


# In[15]:


final


# In[16]:


movie = final[final.titleType == 'movie']
movie


# In[27]:


movie.plot.scatter('averageRating','startYear',alpha=0.1, figsize=(15,15))


# In[18]:


def onehot(df):
    categories = []
    lista = list(df['genres'].unique())
    for cat in lista:
        for c in cat.split(','):
            if c not in categories:
                if c != '\\N':
                    categories.append(c)
    for c in categories:
        df['genre_'+c] = df['genres'].apply(lambda x: 1 if c in x else 0)
    return df


# In[19]:


m = onehot(movie)
m


# In[20]:


m.describe(include='all')


# In[21]:


m['output'] = pd.Series(0)
for c in list(m.columns[m.columns.str.startswith('genre_')]):
    m['output'] = m[c].astype(str) + m['output'].astype(str)


# In[22]:


m


# In[312]:





# In[ ]:




