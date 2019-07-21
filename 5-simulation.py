#!/usr/bin/env python
# coding: utf-8

# In[319]:


import pandas as pd
from random import shuffle,random


# In[2]:


df  = pd.read_pickle('df3x.pickle')
df.head()


# In[3]:


clean = pd.read_pickle('df_clean.pickle')
clean.head()


# In[4]:


falta = [x for x in list(clean.id) if x not in list(df.id)]
falta[:10]


# In[5]:


all_words = list(' '.join(list(clean.content)).split())
all_words_dict = list(set(all_words))
words = pd.DataFrame(columns=['word','count_word'])
words.word = all_words
words2 = words.groupby(['word']).sum()
words2 = words2.sort_values('count_word', ascending=False)
words2 = words2.reset_index()
w2 = list(words2['word'][:50000])
shuffle(w2)
w2[:10]


# In[ ]:



clean = pd.read_pickle('df_clean.pickle')
df  = pd.read_pickle('df3x.pickle')
print(df.shape)
falta = [x for x in list(clean.id) if x not in list(df.id)]
clean = clean.set_index('id')
clean = clean.loc[falta]


cleanx = clean[:50]
d = pd.DataFrame()
for row in cleanx.iterrows():
    print('.',end='', flush=True)
    e = dict()
    idc = row[0]
    content = row[1][0].split()
    e['id'] = idc

    for w in content:
        if w in w2:
            e['word_'+str(w)] = True
    d = df.append(e, ignore_index=True)
df = df.append(d, ignore_index=True)
df.to_pickle('df3x.pickle')
print(df.shape)


# In[ ]:


df


#     "df = pd.DataFrame()\n",
#     "train=train.head(16000)\n",
#     "for word in words:\n",
#     "    df[word] = train.txt.apply(lambda x: (word in x)*1)\n",
#     "df.to_pickle('DONORSCHOOSE\\matrix.pickle')"

# In[76]:


import pandas as pd
import numpy as np
pd.options.display.max_rows = 20
pd.options.display.max_columns = 999


# In[2]:


data_clean = pd.read_pickle('df_clean.pickle')
data_clean.head()


# In[3]:


all_words = list(' '.join(list(data_clean.content)).split())
all_words_dict = list(set(all_words))
words = pd.DataFrame(columns=['word','count_word'])
words.word = all_words
words2 = words.groupby(['word']).sum()
words2 = words2.sort_values('count_word', ascending=False)
words2 = words2.reset_index()
w2 = list(words2['word'][:50000])


# In[14]:


print(len(w2))
x = 0
#df_final = data_clean
df_final = pd.read_pickle('df_final.pickle')
col = list(df_final.columns)
for word in w2:
    x += 1
    if ('word_'+str(word)) not in col:
        df_final['word_'+str(word)] = df_final.content.apply(lambda x: (word in x))
    if x % int(len(w2)/100) == 0:
        print(str(x),flush=True)
        df_final.to_pickle('df_final.pickle')
df_final


# In[7]:


df_final = pd.read_pickle('df_final.pickle')
df_final.describe()


# In[8]:


df_final.shape


# In[23]:


dfg = df_final
dfg


# In[24]:


dfg['total'] = dfg.iloc[:,2:].sum(axis=1)


# In[25]:


dfg.total


# In[29]:


dfg['total'].hist(figsize=(20,20), bins=100)


# In[31]:


dfg = dfg.sort_values('total', ascending = False)
dfg


# In[34]:


data = pd.read_pickle('data.pickle')
print(data.columns)
data.head()


# In[56]:


data['IDMovieImdb'] = data['IDMovieImdb'].apply(int)
data.dtypes


# In[35]:


movie = pd.read_pickle('final.pickle')
print(movie.columns)
movie.head()


# In[48]:


data[data['IDMovieImdb'] == '192528']['MovieName']


# In[38]:


movie[movie['tconst'] == 'tt0192528']


# In[50]:


def tconst_to_imdb(string):
    return int(string[2:])

movie['IDMovieImdb'] = movie['tconst'].apply(tconst_to_imdb)


# In[80]:


movie


# In[79]:


total = pd.merge(data, movie, how='inner', on='IDMovieImdb', sort=True,
         suffixes=('_data', '_movie'))
total


# In[78]:


total2 = total[['IDMovieImdb','IDSubtitleFile', 'MovieImdbRating', 'MovieKind', 'MovieName',
       'MovieYear',  'Score', 'SubAutoTranslation', 'SubBad',
       'SubDownloadsCnt', 'SubEncoding','SubFeatured',  'SubForeignPartsOnly', 'SubFormat',
       'SubFromTrusted', 'SubHearingImpaired','titleType', 'primaryTitle',
       'originalTitle', 'isAdult', 'startYear', 'runtimeMinutes','genres', 'averageRating', 'numVotes']]
total2


# In[81]:


bag = pd.read_pickle('df_final.pickle')
bag['total'] = bag.iloc[:,2:].sum(axis=1)


# In[82]:


bag


# In[83]:


totalx = pd.merge(total2, bag, how='inner', left_on='IDSubtitleFile' , right_on='id',suffixes=('_total2', '_bag'))
totalx


# In[84]:


totalx = totalx.sort_values('Score', ascending = False)
totalx


# In[85]:


totalx.drop_duplicates('IDMovieImdb', keep='first', inplace=True)


# In[4]:


totalx['MovieImdbRating'] = pd.to_numeric(totalx['MovieImdbRating'], errors='coerce')
totalx.dtypes


# In[5]:


totalx.to_pickle('totalx.pickle')


# In[1]:


import pandas as pd
import numpy as np

totalx = pd.read_pickle('totalx.pickle')


# In[51]:


totalx['MovieImdbRating'].hist()


# In[52]:


totalx['Score'].hist(figsize=(20,10),bins=100)


# In[53]:


totalx[totalx['Score'] <0]


# In[54]:


colunas = [x for x in totalx.columns if x.startswith('word_')]
colunas


# In[55]:


colunas_10 = [x for x in colunas if sum(totalx[x]) >5]
for  x in colunas_10:
    print(x,sum(totalx[x]))


# In[56]:


len(colunas_10)


# In[62]:


totalx[colunas].dtypes


# In[118]:


t = totalx[:20]


# In[120]:


t[colunas_10]


# In[110]:


t = t[colunas_10[:29]]


# In[132]:


from random import shuffle


# In[133]:


colunas_10


# In[135]:


shuffle(colunas_10)
colunas_10


# In[139]:


totalx['total'] = totalx[colunas_10].apply(lambda x: ''.join((x*1).map(str)), axis=1)


# In[140]:


totalx['total']


# In[150]:


genres = list(set(','.join(list(totalx.genres.unique())).split(',')))
genres


# In[153]:


df_genre = totalx
for g in genres:
    df_genre['genre_'+str(g)] = df_genre.genres.apply(lambda x: (g in x.split(',')))
df_genre


# In[152]:


totalx


# In[154]:


df_genre['output'] = df_genre[['genre_'+str(g) for g in genres]].apply(lambda x: ''.join((x*1).map(str)), axis=1)


# In[177]:


most_genre = [x for x in df_genre.columns if x.startswith('genre_') and sum(df_genre[x]) > 700]
df_genre['output_most'] = df_genre[most_genre].apply(lambda x: ''.join((x*1).map(str)), axis=1)


# In[182]:


most_genre


# In[183]:


df_genre.output_most


# In[186]:


col_util = list(df_genre.columns)
col_util[-5:]


# In[187]:


col_util = [x for x in col_util if not x.startswith('word_')]
col_util = [x for x in col_util if not x.startswith('genre_')]
df_consolidaded = df_genre[col_util]
df_consolidaded


# In[188]:


out = list(df_consolidaded['output_most'])
for x in df_consolidaded['output_most'].unique():
    print(x, out.count(x))


# In[191]:


list(df_consolidaded.columns)


# In[195]:


df_last = df_consolidaded[['IDMovieImdb','IDSubtitleFile','MovieImdbRating','MovieName', 'MovieYear', 
                           'primaryTitle', 'total', 'output_most']]


# In[196]:


df_last


# In[298]:


def nota(rating,size=20):
    try:
        n = int(round(rating/10*size,0))
    except:
        n = 5
    return (size-n)*'0'+n*'1'

def denota(rating,size=20):
    return rating.count('1')/size*10
nota(.4)
denota('00000011111111111111')


# In[229]:


df_last['output_rating'] = df_last['MovieImdbRating'].apply(nota)


# In[230]:


df_last['output_rating']


# In[249]:


df_last.to_pickle('df_last.pickle')


# In[2]:


df_last = pd.read_pickle('df_last.pickle')


# In[3]:


import wisardpkg as wp


# In[4]:


def reduz(vector,size=3):
    tam = int(len(vector)/size)
    result = []
    for i in range(tam):
        result.append(max(vector[i*size:i*size+size]))
    if len(vector) > tam*size:
        result.append(max(vector[tam*size:]))
    return result
print(reduz([1,2,3,4,5,6,1,1,1,1,12,4]))


# In[395]:


t = 640
output2 =df_last['output_most'].unique()
addressSize = 3 
ignoreZero  = False
verbose = False
for _ in range(10):        
    for t in [50]:
        for out2 in output2:
            erro_benchmarck = []
            erro_proposal_3 = []
            erro_proposal_5 = []
            erro_proposal_10 = []
            df_last2 = df_last[df_last['output_most'] == out2]
            if df_last2['output_most'].shape[0] >100:
                df_last2['random'] = [random() for x in range(len(df_last2))]
                df_last2 = df_last2.sort_values('random')
                X = [list(map(lambda y: int(y), x)) for x in list(df_last2['total'])]
                y = list(df_last2['output_rating'])
                train_X = X[:t]
                train_y = y[:t]
                classify_X = X[-100:]
                classify_y = y[-100:]
                wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
                wsd.train(train_X,train_y)
                out = wsd.classify(classify_X)
                erro = 0
                for i,d in enumerate(classify_X):
                    a,b = denota(out[i]),denota(classify_y[i])
                    erro += (a-b)**2
                erro_benchmarck.append(np.average(erro)**0.5)


                X2 = [reduz(x,3) for x in X]
                train_X2 = X2[:t]
                classify_X2 = X2[t:t+100]
                wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
                wsd.train(train_X2,train_y)
                out = wsd.classify(classify_X2)
                for i,d in enumerate(classify_X2):
                    a,b = denota(out[i]),denota(classify_y[i])
                    erro += (a-b)**2
                erro_proposal_3.append(np.average(erro)**0.5)

                X2 = [reduz(x,5) for x in X]
                train_X2 = X2[:t]
                classify_X2 = X2[t:t+100]
                wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
                wsd.train(train_X2,train_y)
                out = wsd.classify(classify_X2)
                for i,d in enumerate(classify_X2):
                    a,b = denota(out[i]),denota(classify_y[i])
                    erro += (a-b)**2
                erro_proposal_5.append(np.average(erro)**0.5)

                X2 = [reduz(x,10) for x in X]
                train_X2 = X2[:t]
                classify_X2 = X2[t:t+100]
                wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
                wsd.train(train_X2,train_y)
                out = wsd.classify(classify_X2)
                for i,d in enumerate(classify_X2):
                    a,b = denota(out[i]),denota(classify_y[i])
                    erro += (a-b)**2
                erro_proposal_10.append(np.average(erro)**0.5)

                print(t,np.average(erro_benchmarck),np.average(erro_proposal_3),
                  np.average(erro_proposal_5),np.average(erro_proposal_10), out2)


# In[388]:


df_last


# In[389]:


df_last2 = df_last[df_last['output_most'] == '000001']


# In[390]:


df_last2


# In[12]:


def compara(a,b):
    erro = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            erro += 1
    return erro / len(a)

a,b = '111011', '000000'
compara(a,b)


# In[391]:


output=df_last['output_most'].unique()


# In[392]:


output


# In[394]:


for x in output:
    df_last2 = df_last[df_last['output_most'] == x]
    print(df_last2.shape)


# In[396]:


len(X)


# In[398]:


np.average([np.average(x) for x in X])


# In[7]:


from random import random
df_last


# In[14]:


t = 640
df_last2 = df_last
addressSize = 3 
ignoreZero  = False
verbose = False
for _ in range(10):        
    for t in [50,100,200,400,600,800]:
        erro_benchmarck = []
        erro_proposal_3 = []
        erro_proposal_5 = []
        erro_proposal_10 = []
        df_last2['random'] = [random() for x in range(len(df_last2))]
        df_last2 = df_last2.sort_values('random')
        X = [list(map(lambda y: int(y), x)) for x in list(df_last2['total'])]
        y = list(df_last2['output_most'])
        train_X = X[:t]
        train_y = y[:t]
        classify_X = X[-100:]
        classify_y = y[-100:]
        wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
        wsd.train(train_X,train_y)
        out = wsd.classify(classify_X)
        erro = 0
        for i,d in enumerate(classify_X):
            a,b = out[i],classify_y[i]
            erro += compara(a,b)
        erro_benchmarck.append(np.average(erro)**0.5)


        X2 = [reduz(x,3) for x in X]
        train_X2 = X2[:t]
        classify_X2 = X2[t:t+100]
        wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
        wsd.train(train_X2,train_y)
        out = wsd.classify(classify_X2)
        for i,d in enumerate(classify_X2):
            a,b = out[i],classify_y[i]
            erro += compara(a,b)
        erro_proposal_3.append(np.average(erro)**0.5)

        X2 = [reduz(x,5) for x in X]
        train_X2 = X2[:t]
        classify_X2 = X2[t:t+100]
        wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
        wsd.train(train_X2,train_y)
        out = wsd.classify(classify_X2)
        for i,d in enumerate(classify_X2):
            a,b = out[i],classify_y[i]
            erro += compara(a,b)
        erro_proposal_5.append(np.average(erro)**0.5)

        X2 = [reduz(x,10) for x in X]
        train_X2 = X2[:t]
        classify_X2 = X2[t:t+100]
        wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
        wsd.train(train_X2,train_y)
        out = wsd.classify(classify_X2)
        for i,d in enumerate(classify_X2):
            a,b = out[i],classify_y[i]
            erro += compara(a,b)
        erro_proposal_10.append(np.average(erro)**0.5)

        print(t,np.average(erro_benchmarck),np.average(erro_proposal_3),
          np.average(erro_proposal_5),np.average(erro_proposal_10))


# In[ ]:





# In[ ]:




