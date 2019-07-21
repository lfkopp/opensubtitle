#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_columns', 500)
from os import listdir
from os.path import isfile, join


# In[2]:


dirty='subs/'
clean='subs_clear/'
files_dirty = [f for f in listdir(dirty) if isfile(join(dirty, f))] #[:20]
files_clean = [f for f in listdir(clean) if isfile(join(clean, f))]
files_dirty


# In[3]:


def remove_dup(s):
    s = list(set(s.split()))
    s.sort()
    s = ' '.join(s)
    return s


# In[4]:


def remove_adv(s):
    advertising = ['SUPPORT AND BECOME VIP MEMBER', 'REMOVE ALL ADS FROM WWWOPENSUBTITLESORG', 
               'VSUBV THE SMARTEST SUBTITLE DOWNLOADER FOR OSX WWWFLIXTOOLSCOM',
               'ADVERTISE YOUR PRODUCT BRAND HERE','CONTACT WWWOPENSUBTITLESORG TODAY',
               'TEAM XRG WWWDESIDHAMALCOM', 'BXEFXBBXBF', 'WWWOPENSUBTITLESORG',
               'THE VENOM MILLION GTD POKER TOURNEY DOWNLOAD AMERICASCARDROOMCOM', 
               'YBUCAPTIONING KOUSHIK DAS THE VENOM MILLION GTD POKER TOURNEYDOWNLOAD AMERICASCARDROOMCOM RONSONS',
               'DOWNLOADED FROM WWWALLSUBSORG','DOWNLOAD SYNC SUBTITLES AUTOMATICALLY WWWFLIXTOOLSCOM',
               'DOWNLOAD SUBTITLES AND CONVERT YOUR VIDEOS ITUNES WITH FLIXTOOLSCOM',
               'THE SMARTEST SUBTITLE DOWNLOADER FOR OSX WWWFLIXTOOLSCOM', 'WWWEASYWINBLOGSPOTCOM',
               'ZEROHACKER LEBANON GOODFELLAS DVDS BWWWSUBSMANIATKB', 'ADDICEDCOM','AMERICASCARDROOMCOM' ]
    for x in advertising:
        s = s.replace(x, ' ')
    return s


# In[5]:


import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def cleaner(file):
    whitelist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    with open(dirty + file,'rb') as d_file:
        d_content = cleanhtml(str(d_file.read()))
        d_content = d_content.replace('\\r\\n',' ')
        d_content = ''.join(filter(whitelist.__contains__, d_content.upper()))
        d_content = ' '.join(d_content.split())
        d_content = ' '.join([word for word in d_content.split() if len(word) >= 3])
        d_content = ' '.join(remove_adv(d_content).split())
    with open(clean + file,'w+') as c_file:
        c_file.write(d_content)
    return file.split('.')[0],d_content


# In[6]:


df_clean = pd.DataFrame(columns=['id','content'])
for f in files_dirty:
    file,content = cleaner(f)
    if len(content) > 10:
        files_clean.append(f)
        c = dict({'id': file, 'content' : content})
        print(f, len(content))
        df_clean = df_clean.append(c,ignore_index=True)
df_clean.drop_duplicates('id', inplace=True)
df_clean.to_pickle('clean.pickle')


# In[7]:


df_clean.head(15)


# In[8]:


df_clean['content_nodup'] = df_clean["content"].apply(remove_dup)
df_clean.sort_values('content_nodup')


# In[9]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')
  
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 

ps = PorterStemmer() 

def tokenize_string(s):
    word_tokens = word_tokenize(s) 
    stop_words = set(stopwords.words('english')) 
    #filtered_sentence = list(set([ps.stem(w)+':'+w for w in word_tokens if not w in stop_words] ))
    filtered_sentence = list(set([ps.stem(w) for w in word_tokens if not w in stop_words] ))
    filtered_sentence.sort()
    
    return ' '.join(filtered_sentence)


# In[10]:


df_clean['content_token'] = df_clean["content_nodup"].apply(tokenize_string)
df_clean.sort_values('content_token')


# In[12]:


all_tokens = df_clean.content_token.str.cat(sep=' ')
all_tokens


# In[13]:


all_tokens = remove_dup(all_tokens)


# In[14]:


all_tokens


# In[16]:


for word in df_clean.content_token[0].split():


# In[79]:


df = df_clean[:2]
all_tokens2 = remove_dup(df.content_token.str.cat(sep=''))


# In[80]:


df


# In[81]:


all_tokens2


# In[ ]:


df.to_pickle('df.pickle')


# In[ ]:


for word in all_tokens2.split():
    df['word_'+str(word)] = df.content_token.apply(lambda row: word in row.split())


# In[ ]:


df


# In[ ]:




