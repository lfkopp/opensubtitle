#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xmlrpc.client as xrpc
server = xrpc.ServerProxy("http://api.opensubtitles.org/xml-rpc")
import base64
import gzip


import json


# In[2]:


credentials = server.LogIn("omerakgul58", "omeromer", "en", "2016experimentingwithnlp")
#credentials = server.LogIn("randomwalker", "sub1machine", "en", "MachineTitle")

token = credentials.get("token")
info = server.ServerInfo()
info['download_limits']['client_download_quota']


# In[3]:


# server.GetSubLanguages()
# server.SearchMoviesOnIMDB(token, "troy")
action_imdb_ids = ['1375666', '0120737', '0167260', '0167261', '0944947', '0172495', '0372784', 
                   '0816692', '0076759', '0361748', '0499549', '0080684', '0325980', '0088763', 
                   '0910970', '1392170', '0266543', '0371746', '2015381', '0086190', '1049413', 
                   '0082971', '0110357', '0903624', '0114709', '0107290', '0198781', '2488496', 
                   '1454468', '1392190', '1300854', '0770828', '0435761', '1201607', '0145487', 
                   '0800369', '0120915', '1431045', '1228705', '0383574', '1074638', '0121766',
                   '1270798', '0097576', '1877832', '0458339', '0418279', '0796366', '1843866',
                   '3659388', '1951264', '0090605', '0892769', '2278388', '1170358', '0317705', 
                   '0988045', '2395427', '0449088', '0381061', '0126029', '0816711', '0121765', 
                   '1446714', '0120903', '0948470', '0241527', '0454876', '1663202', '1631867', 
                   '0116629', '0062622', '0758758', '0245429', '0369610', '2294629', '1981115', 
                   '0073195', '0316654', '2975590', '0290334', '2802144', '0119654', '0450259', 
                   '1408101', '0162222', '0295297', '0330373', '1483013', '1156398', '1323594', 
                   '0120363', '0304141', '0413300', '0376994', '0071853', '0332452', '1663662', 
                   '0411008', '1298650', '1229238', '2096673', '0458525', '2310332', '0373889', 
                   '0319061', '0119116', '0096874', '1840309', '3498820', '1515091', '0407304', 
                   '0337978', '0367882', '0319262', '0087469', '0830515', '0926084', '1430132', 
                   '0268380', '0478970', '0800080', '0417741', '1399103', '0367594', '1872181', 
                   '0120591', '1055369', '2103281', '0120616', '0298148', '0360717', '1951265', 
                   '0441773', '1014759', '2193021', '0117060', '0831387', '0112864', '0398286', 
                   '0093779', '0032138', '1690953', '0363771', '0099088', '0438488', '2245084', 
                   '2379713', '1190080', '0119567', '1542344', '1217209', '0087332', '0092005', 
                   '1772341', '1320253', '0096895', '0120912', '0351283', '0120667', '1409024', 
                   '0317219', '1104001', '0103639', '0399201', '0111257', '0117500', '0462538', 
                   '0317919', '1386697', '1587310', '0368891', '1490017', '0209163', '1764651', 
                   '0970179', '0120755', '2109248', '0489099', '0379786', '1403865', '1748122', 
                   '2381249', '0348150', '0212720', '0381849', '1453405', '0359950', '0477347', 
                   '0472043', '1194173', '0047478', '1735898', '0800320', '1037705', '0190590', 
                   '0119698', '1646971', '1133985', '0473075', '0053125', '0120201', '0163025', 
                   '1259571', '2948356', '0320661', '0347149', '0190332', '0120669', '0486576', 
                   '0413267', '3385516', '0401729', '0120623', '0486655', '0955308', '0429493', 
                   '0112384', '0113497', '0411477', '0181875', '1601913', '0104431', '1386703', 
                   '1440129', '1959490', '0113189', '0338526', '0438097', '1464540', '0056172', 
                   '1092026', '3107288', '1340138', '0112462', '0448134', '0303461', '0099348', 
                   '1673434', '0825232', '1638355', '1302011', '1325004', '1192628', '0296572', 
                   '0102057', '0465234', '1324999', '1210819', '0120655']

# subtitles = server.SearchSubtitles(token, [ {'imdbid': '1515091', 'sublanguageid': 'eng'} ])
subtitles = server.SearchSubtitles(token, [ {'imdbid': id, 'sublanguageid': 'eng'} for id in action_imdb_ids]) #[:20]])

# impaired_support = True

# subtitles = list(filter(lambda sub: sub['SubHearingImpaired'] == '1', subtitles))
# print([(sub['SubFormat']) for sub in subtitles['data']])
print(len(subtitles['data']))


# In[4]:




subtitle_ids = [ sub['IDSubtitleFile'] for sub in subtitles['data']]
#print(subtitle_ids)
for x in range(0,len(subtitles['data']),10):
    result = server.DownloadSubtitles(token, subtitle_ids[x:x+10])
    print(result)
#     for d in result['data']:
#         with open("subs"+str(d['idsubtitlefile'])+".txt", 'wb+') as file:
#             file.write(gzip.decompress(base64.b64decode(d['data']))) #.decode()))

    


# In[103]:


# print([res['idsubtitlefile'] for res in result['data']])
# # print(subtitle_ids[:10])



# In[57]:


# -*- coding: utf-8 -*-

# subtitles_path = "/Users/mesutgurlek/Documents/Machine Learning/project/Movie-Category-Classification-from-Subtitles/Subtitles"
subtitles_path = ""
url_template = "http://www.imdb.com/search/title?genres=%s&explore=genres&sort=num_votes,desc&view=simple"
imdb_page_limit = 1

server = xrpc.ServerProxy("http://api.opensubtitles.org/xml-rpc")
token = server.LogIn("randomwalker", "sub1machine", "en", "MachineTitle").get("token")
remaining_quota = server.ServerInfo()['download_limits']['client_download_quota']

print(server.ServerInfo())

categories = ['action', 'comedy', 'horror', 'war', 'romance', 'adventure']
subtitle_per_category = int(remaining_quota / len(categories))



def parse_movies(imdb_ids=['0172495'], category_name='War'):
        #movie_links = response.css(".bnone").xpath('@href').extract()
        #for link in movie_links:
             #yield scrapy.Request(url=response.urljoin(link), callback=self.parse_movie)
        #print("Listing scraped IMDB ids for%s: ", category_name)
        #print(imdb_ids)
        impaired_support = True

        subtitles = {} # key => IDSubtitleFile, value => Metadata of subtitle
        yy = 1
        # USING IMDB ID'S, DOWNLOAD THEIR METADATA AND SELECT ID OF A SUITABLE SUBTITLE FOR EACH MOVIE
        for imdb_id in imdb_ids[:subtitle_per_category]:
            #print("Searching subtitle for movie with ID: %s" % imdb_id)
            found_subtitles = server.SearchSubtitles(token, [{'imdbid': imdb_id, 'sublanguageid': 'eng'}])['data']

            #print("!!!!! Found subtitles: %s" % found_subtitles)

            if impaired_support:
                impaired_subtitles = list(filter(lambda sub: sub['SubHearingImpaired'] == '1', found_subtitles))

            impaired_label = ""
            if len(impaired_subtitles) > 0:
                subtitle = impaired_subtitles[0]
                impaired_label = "(IMPAIRED)"
            else:
                subtitle = found_subtitles[0] # for now get the first subtitle

            filename = "%s/%s/%s %s" % (subtitles_path, category_name, subtitle['MovieName'], impaired_label)

            subtitles[subtitle['IDSubtitleFile']] = {'imdb_id': imdb_id, 'filename': filename,
                                                     'movie_name': subtitle['MovieName'],
                                                    'SubDownloadLink': subtitle['SubDownloadLink']}

            #with open(str(imdb_id)+".txt", 'w+') as f:
            #    f.write(json.dumps(subtitle['SubDownloadLink']))
            #    yield parse_movie(imdb_id)
            #
            yy +=1


        #DOWNLOAD SUBTITLES AND WRITE THEM INTO FILES
        print("Downloading subtitles of %s" % category_name)
        subtitle_ids = [ idsubtitlefile for idsubtitlefile, val in subtitles.items()]
        subtitle_files_response = server.DownloadSubtitles(token, subtitle_ids)

        import base64
        import gzip

        
        if subtitle_files_response['status'] == '200 OK':
            print("Subtitles downloaded, writing to files...")
            for subtitle_object in subtitle_files_response['data']: #each subtitle_object has base64 data and idsubtitlefile key
                sub = subtitles[subtitle_object['idsubtitlefile']]

                try:
                    with open(str(imdb_id)+".srt", 'wb+') as file:
                        file.write(gzip.decompress(base64.b64decode(subtitle_object['data']))) #.decode())
                        print("Subtitle file saved into: %s" % yy ) #sub['filename'])
                except:
                    print("erro:",sub['filename'])


parse_movies(subtitle_ids)

                    


# In[ ]:




