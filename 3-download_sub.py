#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def arruma(series):
    return pd.to_numeric(series, errors='coerse', downcast ='integer')


# In[3]:


data = pd.read_pickle('data.pickle')
data['MovieYear'] = arruma(data['MovieYear'])
data['MovieImdbRating'] = arruma(data['MovieImdbRating'])
data = data[data['MovieYear'] > 2010]
data = data[data['MovieImdbRating'] > 6]
data.sort_values(['MovieYear','MovieImdbRating'], ascending=False, inplace=True)

print(data.shape)
data.head() 


# In[147]:


list(data.ZipDownloadLink)[:6]


# In[148]:


from multiprocessing import Pool

mypath='subs/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]


user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]



lista = list(data.SubDownloadLink)
shuffle(lista)

#proxies = list(get_proxies())
def reseta():
    global user_agent_list    
    global proxies
    user_agent = choice(user_agent_list)
    header = {'User-Agent': user_agent}
    proxy = {'http' : choice(proxies),'https' : choice(proxies)}
    return header,proxy


def download_file(url):
    #header,proxy = reseta()
    name = url.split('/')[-1]
    name = str(name.split('.')[0])+ '.txt'
    if name not in files:
        try:
            fullname = mypath  + name
            raw_data = requests.get(url) #, proxies=proxy, headers=header)
            with open(fullname, 'wb+') as file:
                content = gzip.decompress(raw_data.content)
                file.write(content)
                print('O',end='', flush=True)
                sleep(random.random()+.5)
        except Exception as e:
            print('E',end='', flush=True)
    else:
        print('_',end='', flush=True)

with Pool(4) as p:
    p.map(download_file, lista)


# In[149]:


data.SubtitlesLink[:5]


# In[150]:


data.ZipDownloadLink.head()


# In[151]:


from torrequest import TorRequest
tr=TorRequest(password='juju')


# In[47]:


import requests
response= requests.get('http://ipecho.net/plain')
print("My Original IP Address:",response.text)


# In[48]:


def reset_ip():
    tr=TorRequest(password='juju')
    tr.reset_identity() #Reset Tor
    response= tr.get('http://ipecho.net/plain')
    print("New Ip Address",response.text)
reset_ip()


# In[24]:


import requests
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
proxies = get_proxies()
proxies


# In[50]:


#  https://www.scrapehero.com/make-anonymous-requests-using-tor-python/


# In[51]:


reset_ip()


# In[ ]:





# In[ ]:


mypath='subs/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

lista = list(data.SubDownloadLink)
shuffle(lista)
# print(lista[:20])

def download_file(url):
    name = url.split('/')[-1]
    name = str(name.split('.')[0])+ '.txt'
    if name not in files:
        try:
            fullname = mypath  + name
            raw_data = requests.get(url)
            with open(fullname, 'wb+') as file:
                content = gzip.decompress(raw_data.content)
                file.write(content)
                #print('.',end=' ', flush=True)
                print(name,len(content))
                #sleep(random.random()+.5)
        except:
            print(name, 'erro')
            return 'erro'
    else:
        print(name, 'já tinha')
i = 0
for url in lista:
    if download_file(url) == 'erro':
        #reset_ip()
        i += 1
        sleep(10)


# In[4]:


import xmlrpc.client as xrpc
import base64
import gzip
import json


mypath='subs/'


server = xrpc.ServerProxy("http://api.opensubtitles.org/xml-rpc")

def baixa(subtitle_id):
    result = server.DownloadSubtitles(token, subtitle_id)
    for d in result['data']:
        filename = str(d['idsubtitlefile'])+".txt"
        if filename not in files:
            #print(filename)
            with open(mypath + filename, 'wb+') as file:
                content = gzip.decompress(base64.b64decode(d['data']))
                print('.',end='',flush=True)
                file.write(content) #.decode()))
#baixa([1956249062,1952281521,1952503920])

credentials_list = [server.LogIn("randomwalker", "sub1machine", "en", "MachineTitle"),
                   server.LogIn("omerakgul58", "omeromer", "en", "2016experimentingwithnlp"),
                   server.LogIn("mrkopp", "mymoviez00", "en", "SubtitleClassification"),
                   server.LogIn("mrkopp2", "mymoviez00", "en", "SubtitleClassification"),
                    server.LogIn("mrkopp4", "mymoviez00", "en", "SubtitleClassification"),
                   server.LogIn("mrkopp5", "mymoviez00", "en", "SubtitleClassification"),
                   server.LogIn("mrkopp7", "mymoviez00", "en", "SubtitleClassification"),
                   server.LogIn("mrkopp8", "mymoviez00", "en", "SubtitleClassification"),
                   server.LogIn("mrkopp9", "mymoviez00", "en", "SubtitleClassification")]
shuffle(credentials_list)
#credentials_list = [server.LogIn("mrkopp9", "mymoviez00", "en", "SubtitleClassification")]

for credentials in credentials_list:
    #credentials['data']['IsVIP'] = 1
    #credentials['data']['DownloadCnt'] = 1
    print(credentials)
    token = credentials.get("token")
    info = server.ServerInfo()
    #print(info)
    print(info['download_limits']['client_24h_download_count'])
    for f in range(20):
        try:
            h=20
            files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            ja_tem = [x[:-4] for x in files]
            falta = [x for x in list(data.IDSubtitleFile) if x not in ja_tem]
            shuffle(falta)
            print()
            print(falta[f*h:f*h+h])
            baixa(falta[f*h:f*h+h])
            sleep(1)
        except Exception as e:
            print(e)
            break


# In[6]:


def get_info(id_imdb):
    data = server.SearchSubtitles(token, [ {'imdbid': int(id_imdb[2:]), 'sublanguageid': 'eng'}])
    try:
        return pd.DataFrame.from_dict(data['data'])
    except:
        return False
    
get_info('tt5773402')


# In[ ]:





# In[33]:



ja_tem


# In[125]:



falta


# In[12]:


baixa([0])


# In[138]:


files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
ja_tem = [x[:-4] for x in files]
falta = [x for x in list(data.IDSubtitleFile) if x not in ja_tem]
len(ja_tem)


# In[139]:


len(falta)


# In[38]:


a = server.LogIn("mrkopp9", "mymoviez00", "en", "SubtitleClassification")


# In[39]:


print(a)


# In[42]:


a['data']['IsVIP'] = 1
a['data']['DownloadCnt'] = 1


# In[43]:


a


# In[71]:


ja_tem


# In[13]:


try:
    raw = pd.read_pickle('raw.pickle')
except:
    raw = pd.DataFrame(columns=['IDSubtitleFile','raw_content','size'])
raw.head()


# In[141]:


files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
falta_raw = [x[:-4] for x in files if x[:-4] not in list(raw.IDSubtitleFile)]
falta_raw


# In[142]:


mypath='subs/'
try:
    raw = pd.read_pickle('raw.pickle')
except:
    raw = pd.DataFrame(columns=['IDSubtitleFile','raw_content','size'])

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
falta_raw = [x[:-4] for x in files if x[:-4] not in list(raw.IDSubtitleFile)]
print(len(falta_raw))
print(raw.shape)

for x in falta_raw:
    with open(mypath + x+'.txt','rb') as f:
        z = str(f.read())
        #print(z)
        c = dict({'IDSubtitleFile': x, 'raw_content' : z, 'size': len(z)})
        raw = raw.append(c,ignore_index=True)
raw.to_pickle('raw.pickle')

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
falta_raw = [x[:-4] for x in files if x[:-4] not in list(raw.IDSubtitleFile)]
print(len(falta_raw))
print(raw.shape)


# In[123]:


raw.head()


# In[3]:


mypath='subs/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
falta_raw = [x[:-4] for x in files if x[:-4] not in list(raw.IDSubtitleFile)]


# In[271]:


import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def cleaner(string):
    whitelist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    string = string.replace('\n', ' ')
    string = cleanhtml(string)
    string = ''.join(filter(whitelist.__contains__, string.upper())).strip()
    if len(string)>0:
        return string
    else:
        return ''
def get_clean(x):
    with open(mypath + x+'.txt',encoding='utf-8', errors='ignore') as f:
        z = f.read().split('\n\n')
        k = ' '.join([cleaner(zz.split('\n',2)[2]) for zz in z])
        return ' '.join([x for x in list(set(k.split())) if len(x.strip())>3])


# In[272]:


for x in falta_raw[:2]:
    c = get_clean(x)
    print(c)


# In[296]:


with open(mypath +'1952893019.txt', 'r') as f:
    z = f.read()
    print(z)


# In[2]:


mypath='subs/'
try:
    df_clean = pd.read_pickle('df_clean.pickle')
except:
    df_clean = pd.DataFrame(columns=['id','content'])

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
falta_raw = [x[:-4] for x in files if x[:-4] not in list(df_clean.id)]

for idc in falta_raw:
    #print(idc)
    try:
        c = dict({'id': idc, 'content' : get_clean(idc)})
        df_clean = df_clean.append(c,ignore_index=True)
    except:
        print(idc)
df_clean.to_pickle('df_clean.pickle')


# In[3]:


all_words = list(' '.join(list(df_clean.content)).split())


# In[4]:


all_words_dict = list(set(all_words))


# In[99]:


print(len(all_words))
print(len(all_words_dict))


# In[100]:


#all_words = all_words[:1000]
#all_words_dict = list(set(all_words))


# In[101]:


all_words.count(all_words_dict[0])


# In[102]:


words = pd.DataFrame(columns=['word','count_word'])


# In[103]:


words.word = all_words


# In[104]:


words['count_word'] = 1
words


# In[105]:


words2 = words.groupby(['word']).sum()


# In[106]:


words2.shape


# In[107]:


words2 = words2.sort_values('count_word', ascending=False)


# In[14]:


for i in range(20):
    print(i,words2[words2.count_word > i].shape[0])


# In[15]:


for i in range(1000):
    print(i,words2.index[i],words2.count_word[i])


# In[37]:


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


# In[46]:


words2 = words2.reset_index()
#words2['stem'] = words2['word'].apply(tokenize_string)
words2['stem'] = words2['word'].apply(ps.stem)


# In[47]:


words2.sort_values('stem')


# In[50]:


words3 = words2.groupby('stem').sum()


# In[53]:


words3.sort_values('count_word', ascending = False)


# In[61]:


words3 = words3.reset_index()
for i in range(200):
    print(i,words3[words3.count_word > i].shape[0])


# In[66]:


words3 = words3[['stem','count_word']].sort_values('count_word', ascending=False)
words3


# In[67]:


words3.to_pickle('words3.pickle')


# In[108]:


words2


# In[109]:


words2 = words2.reset_index()
words2


# In[110]:


words2 = words2[['word','count_word']]

w2 = list(words2['word'][:50000])
df2 = df_clean
shuffle(w2)
w2


# In[ ]:


k=500
l = int(len(w2)/k)

for v in range(l):
    print(v,l)
    for w in w2[v*k:v*k+k]:
        df2['word_'+str(w)] = df2['content'].str.count(w)
    df2.to_pickle('df2.pickle')
df2


# In[20]:


words2.head()


# In[21]:


df_clean.head()


# In[185]:


df = df_clean #.head()
df


# In[ ]:


dfx = pd.DataFrame([])
total = df.shape[0]
quantum = int(total/250)+1
print('total',total,'quantum',quantum)
for j in range(0,250):
    kk=0
    e = dict()
    for line in df[j*quantum:j*quantum+quantum].iterrows():
        kk = kk + 1
        print('.',end='',flush=True)
        content = line[1][1]
        idc = line[1][0]
        e[kk] = dict({'id':idc})
        for w in content.split():
            if w in w2:
                e[kk]['word_'+w] = True
    for f in e:
        dfx = dfx.append(e[f], ignore_index=True)
    print('\n',j,dfx.shape)
    dfx.to_pickle('df2.pickle')

dfx


# In[ ]:



df


# In[88]:


w3 = list(words3[:50000]['stem'])


# In[83]:


df = df_clean
df['stem'] = df['content'].apply(tokenize_string)
df


# In[92]:


shuffle(w3)

for w in w3[:100]:
    df['word_'+str(w)] = df['stem'].str.count(w)
df


# In[ ]:




