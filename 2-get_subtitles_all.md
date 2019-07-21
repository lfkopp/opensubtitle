

```python
import pandas as pd
pd.set_option('display.max_columns', 500)

import numpy as np
import requests
import gzip
```


```python
url =' http://dl.opensubtitles.org/addons/export/subtitles_all.txt.gz'
raw_data = requests.get(url)
with open('subtitles_all.gz', 'wb+') as file:
    file.write(raw_data.content)

```


    ---------------------------------------------------------------------------

    ParserError                               Traceback (most recent call last)

    <ipython-input-4-4b2752d529cf> in <module>
          3 with open('subtitles_all.gz', 'wb+') as file:
          4     file.write(raw_data.content)
    ----> 5 df = pd.read_csv('subtitles_all.gz', compression='gzip', sep=r'\t', engine='python')
          6 df.to_pickle('subtitles_all.pickle')
          7 


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
        676                     skip_blank_lines=skip_blank_lines)
        677 
    --> 678         return _read(filepath_or_buffer, kwds)
        679 
        680     parser_f.__name__ = name


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
        444 
        445     try:
    --> 446         data = parser.read(nrows)
        447     finally:
        448         parser.close()


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in read(self, nrows)
       1034                 raise ValueError('skipfooter not supported for iteration')
       1035 
    -> 1036         ret = self._engine.read(nrows)
       1037 
       1038         # May alter columns / col_dict


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in read(self, rows)
       2264             content = content[1:]
       2265 
    -> 2266         alldata = self._rows_to_cols(content)
       2267         data = self._exclude_implicit_index(alldata)
       2268 


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in _rows_to_cols(self, content)
       2907                     msg += '. ' + reason
       2908 
    -> 2909                 self._alert_malformed(msg, row_num + 1)
       2910 
       2911         # see gh-13320


    ~/.local/lib/python3.6/site-packages/pandas/io/parsers.py in _alert_malformed(self, msg, row_num)
       2674 
       2675         if self.error_bad_lines:
    -> 2676             raise ParserError(msg)
       2677         elif self.warn_bad_lines:
       2678             base = 'Skipping line {row_num}: '.format(row_num=row_num)


    ParserError: Expected 16 fields in line 2876, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.



```python
quotechar 
error_bad_lines 
warn_bad_lines 

```


```python
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
```


```python
download_file(url,'subtitles_all.gz')
```




    'subtitles_all2.gz'




```python
df = pd.read_csv('subtitles_all.gz', compression='gzip', sep=r'\t', engine='python', 
                 quotechar='"', error_bad_lines=False, warn_bad_lines=True )
df.to_pickle('subtitles_all.pickle')
    
```

    Skipping line 2876: Expected 16 fields in line 2876, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 85576: Expected 16 fields in line 85576, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 137448: Expected 16 fields in line 137448, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 145172: Expected 16 fields in line 145172, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 180188: Expected 16 fields in line 180188, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 184872: Expected 16 fields in line 184872, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 208605: Expected 16 fields in line 208605, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 209341: Expected 16 fields in line 209341, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 239464: Expected 16 fields in line 239464, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 279139: Expected 16 fields in line 279139, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 287216: Expected 16 fields in line 287216, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 287398: Expected 16 fields in line 287398, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 287478: Expected 16 fields in line 287478, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 288214: Expected 16 fields in line 288214, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 289989: Expected 16 fields in line 289989, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 382798: Expected 16 fields in line 382798, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 412726: Expected 16 fields in line 412726, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 415672: Expected 16 fields in line 415672, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 434659: Expected 16 fields in line 434659, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 740175: Expected 16 fields in line 740175, saw 18. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 748547: Expected 16 fields in line 748547, saw 20. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 753414: Expected 16 fields in line 753414, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 754510: Expected 16 fields in line 754510, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1196810: Expected 16 fields in line 1196810, saw 19. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1216901: Expected 16 fields in line 1216901, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1261272: Expected 16 fields in line 1261272, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1450388: Expected 16 fields in line 1450388, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1466795: Expected 16 fields in line 1466795, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 1469780: Expected 16 fields in line 1469780, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2606436: Expected 16 fields in line 2606436, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2652168: Expected 16 fields in line 2652168, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2732212: Expected 16 fields in line 2732212, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2737447: Expected 16 fields in line 2737447, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2966011: Expected 16 fields in line 2966011, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 2971634: Expected 16 fields in line 2971634, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3127974: Expected 16 fields in line 3127974, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3323098: Expected 16 fields in line 3323098, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3330680: Expected 16 fields in line 3330680, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3581929: Expected 16 fields in line 3581929, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3714982: Expected 16 fields in line 3714982, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3764745: Expected 16 fields in line 3764745, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3815723: Expected 16 fields in line 3815723, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3942565: Expected 16 fields in line 3942565, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 3989839: Expected 16 fields in line 3989839, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 4102840: Expected 16 fields in line 4102840, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 4176507: Expected 16 fields in line 4176507, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 4257937: Expected 16 fields in line 4257937, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.
    Skipping line 4303218: Expected 16 fields in line 4303218, saw 17. Error could possibly be due to quotes being ignored when a multi-char delimiter is used.



```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>IDSubtitle</th>
      <th>MovieName</th>
      <th>MovieYear</th>
      <th>LanguageName</th>
      <th>ISO639</th>
      <th>SubAddDate</th>
      <th>ImdbID</th>
      <th>SubFormat</th>
      <th>SubSumCD</th>
      <th>MovieReleaseName</th>
      <th>MovieFPS</th>
      <th>SeriesSeason</th>
      <th>SeriesEpisode</th>
      <th>SeriesIMDBParent</th>
      <th>MovieKind</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alien3</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-10-31 23:54:23</td>
      <td>103644</td>
      <td>sub</td>
      <td>2.0</td>
      <td>Alien.3</td>
      <td>11.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/1/alien...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Identity</td>
      <td>2003.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-10-31 23:54:23</td>
      <td>309698</td>
      <td>sub</td>
      <td>1.0</td>
      <td>Identity.DVDRiP.XViD</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/2/ident...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Ghost in the Shell 2: Innocence</td>
      <td>2004.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-10-31 23:54:23</td>
      <td>347246</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Innocence.2004.DVDRip.XviD</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3/ghost...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Planet of the Apes</td>
      <td>2001.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-10-31 23:54:23</td>
      <td>133152</td>
      <td>sub</td>
      <td>1.0</td>
      <td>Planet.Of.The. Apes.XviD</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4/plane...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>The City of Lost Children</td>
      <td>1995.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-01 20:11:53</td>
      <td>112682</td>
      <td>srt</td>
      <td>2.0</td>
      <td>The.City.Of.Lost.Children.1995.iNTERNAL.DVDRi...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5/the-c...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Antitrust</td>
      <td>2001.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-02 21:30:28</td>
      <td>218817</td>
      <td>sub</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6/antit...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Dirty Pretty Things</td>
      <td>2002.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-03 11:58:18</td>
      <td>301199</td>
      <td>sub</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7/dirty...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Bringing Down the House</td>
      <td>2003.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-03 12:04:20</td>
      <td>305669</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/8/bring...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Cradle 2 the Grave</td>
      <td>2003.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-03 12:06:36</td>
      <td>306685</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/9/cradl...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Death to Smoochy</td>
      <td>2002.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-03 12:09:01</td>
      <td>266452</td>
      <td>sub</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/10/deat...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Hellboy</td>
      <td>2004.0</td>
      <td>Hungarian</td>
      <td>hu</td>
      <td>2004-11-03 13:03:21</td>
      <td>167190</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Hellboy.2004.DVDRip.XviD-DVP</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/11/hell...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>American Gun</td>
      <td>2002.0</td>
      <td>Slovenian</td>
      <td>sl</td>
      <td>2004-11-03 13:36:45</td>
      <td>270197</td>
      <td>sub</td>
      <td>1.0</td>
      <td>American Gun</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/12/amer...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Jui kuen II</td>
      <td>1994.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 17:11:34</td>
      <td>111512</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Drunken.Master.2.Uncut.DVD-Rip.By.Ghost</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/13/jui-...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4062580</td>
      <td>"Bones" The Bodies in the Book</td>
      <td>2007.0</td>
      <td>Portuguese (BR)</td>
      <td>pb</td>
      <td>2011-01-22 07:33:42</td>
      <td>934029</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Bones.02x15</td>
      <td>23.976</td>
      <td>2.0</td>
      <td>15.0</td>
      <td>460627.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/4062580...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>House of Flying Daggers</td>
      <td>2004.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 17:16:21</td>
      <td>385004</td>
      <td>srt</td>
      <td>2.0</td>
      <td>House.Of.Flying.Daggers.2004.RETAIL.DVDRip.XV...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/14/hous...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>Femme Fatale</td>
      <td>2002.0</td>
      <td>Hungarian</td>
      <td>hu</td>
      <td>2004-11-04 20:08:30</td>
      <td>280665</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Femme.Fatale.DVDRip.XViD-ViTE</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/15/femm...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>Lu ding ji</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:45:50</td>
      <td>104770</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Stephen Chow - Royal Tramp 1</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/16/lu-d...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>Rashomon</td>
      <td>1950.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:52:44</td>
      <td>42876</td>
      <td>srt</td>
      <td>1.0</td>
      <td>rashomon_(1950).earthling10480.sharereactor</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/17/rash...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Rashomon</td>
      <td>1950.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:52:44</td>
      <td>42876</td>
      <td>smi</td>
      <td>1.0</td>
      <td>rashomon_(1950).garandou.sharereactor</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/18/rash...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>4419719</td>
      <td>The Valdemar Legacy</td>
      <td>2010.0</td>
      <td>Romanian</td>
      <td>ro</td>
      <td>2011-11-28 00:16:20</td>
      <td>1242744</td>
      <td>srt</td>
      <td>1.0</td>
      <td>La.herencia.Valdemar.2010.720p.BluRay.x264-DON</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4419719...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>4419721</td>
      <td>"The Big Bang Theory" The Flaming Spittoon Acq...</td>
      <td>2011.0</td>
      <td>Hungarian</td>
      <td>hu</td>
      <td>2011-11-28 00:20:11</td>
      <td>2105978</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Big.Bang.Theory.S05E10.HDTV.Swesub.XviD-Fl...</td>
      <td>23.976</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>898266.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/4419721...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>20</td>
      <td>Hei kek ji wong</td>
      <td>1999.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:58:02</td>
      <td>188766</td>
      <td>srt</td>
      <td>1.0</td>
      <td>King of Comedy</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/20/hei-...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>21</td>
      <td>Spirited Away</td>
      <td>2001.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:04:23</td>
      <td>245429</td>
      <td>sub</td>
      <td>2.0</td>
      <td>Spirited Away - DVDRip</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/21/spir...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4420392</td>
      <td>Atlas Shrugged: Part I</td>
      <td>2011.0</td>
      <td>Dutch</td>
      <td>nl</td>
      <td>2011-11-29 00:16:57</td>
      <td>480239</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Atlas.Shrugged.Part.1.LIMITED.2011.BRRip.XviD-...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4420392...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>4420394</td>
      <td>The Pianist</td>
      <td>2002.0</td>
      <td>Slovak</td>
      <td>sk</td>
      <td>2011-11-29 00:18:09</td>
      <td>253474</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Pianist (moviesbyrizzo) HD</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4420394...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>23</td>
      <td>Back to the Future Part II</td>
      <td>1989.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:15:46</td>
      <td>96874</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Back To The Future II - English</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/23/back...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>24</td>
      <td>Ghost Ship</td>
      <td>2002.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:47:29</td>
      <td>288477</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ghost Ship.English</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/24/ghos...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>25</td>
      <td>Ghost Ship</td>
      <td>2002.0</td>
      <td>Hungarian</td>
      <td>hu</td>
      <td>2004-11-04 21:47:29</td>
      <td>288477</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ghost.Ship.DVDRip.XviD-ViTE</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/25/ghos...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>26</td>
      <td>Lu ding ji II: Zhi shen long jiao</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:55:18</td>
      <td>104771</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Stephen Chow - Royal Tramp 2</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/26/lu-d...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>4421144</td>
      <td>"Rome" Death Mask</td>
      <td>2007.0</td>
      <td>Polish</td>
      <td>pl</td>
      <td>2011-11-30 00:20:06</td>
      <td>901366</td>
      <td>mpl</td>
      <td>1.0</td>
      <td>Rome.S02E07.720p.BluRay.x264-MAjUS</td>
      <td>0.000</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>384766.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/4421144...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4336528</th>
      <td>7678533</td>
      <td>"Supergirl" Elseworlds, Part 3</td>
      <td>2018.0</td>
      <td>Italian</td>
      <td>it</td>
      <td>2019-03-07 03:41:04</td>
      <td>8883894</td>
      <td>srt</td>
      <td>1.0</td>
      <td>supergirl.s04e09.WEBRip.sub.ita.A7A</td>
      <td>23.976</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>4016454.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678533...</td>
    </tr>
    <tr>
      <th>4336529</th>
      <td>7678534</td>
      <td>"American Dad!" The Best Christmas Story Never</td>
      <td>2006.0</td>
      <td>Greek</td>
      <td>el</td>
      <td>2019-03-07 03:46:58</td>
      <td>920930</td>
      <td>srt</td>
      <td>1.0</td>
      <td>American Dad S02E09 The Best Christmas Story ...</td>
      <td>25.000</td>
      <td>2.0</td>
      <td>9.0</td>
      <td>397306.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678534...</td>
    </tr>
    <tr>
      <th>4336530</th>
      <td>7678535</td>
      <td>"The Passage" You Are Not That Girl Anymore</td>
      <td>2019.0</td>
      <td>Spanish</td>
      <td>es</td>
      <td>2019-03-07 03:54:32</td>
      <td>9252966</td>
      <td>srt</td>
      <td>1.0</td>
      <td>You are not that girl anymore</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>1074206.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678535...</td>
    </tr>
    <tr>
      <th>4336531</th>
      <td>7678536</td>
      <td>"The Good Doctor" Breakdown</td>
      <td>2019.0</td>
      <td>Portuguese (BR)</td>
      <td>pb</td>
      <td>2019-03-07 03:56:09</td>
      <td>9660060</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Good.Doctor.S02E17.720p.HDTV.x264-KILLERS</td>
      <td>23.976</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>6470478.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678536...</td>
    </tr>
    <tr>
      <th>4336532</th>
      <td>7678538</td>
      <td>"Narcos: Mexico" Camelot</td>
      <td>2018.0</td>
      <td>Croatian</td>
      <td>hr</td>
      <td>2019-03-07 04:16:56</td>
      <td>6038978</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Narcos.Mexico.S01E01.720p.WEBRip.x265-HETeam</td>
      <td>25.000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>8714904.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678538...</td>
    </tr>
    <tr>
      <th>4336533</th>
      <td>7678544</td>
      <td>Koi... Mil Gaya</td>
      <td>2003.0</td>
      <td>Sinhalese</td>
      <td>si</td>
      <td>2019-03-07 05:52:29</td>
      <td>254481</td>
      <td>srt</td>
      <td>1.0</td>
      <td>koi mil gaya full movie hd 1080p full movie i...</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678544...</td>
    </tr>
    <tr>
      <th>4336534</th>
      <td>7678545</td>
      <td>"Grey's Anatomy" Blood and Water</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 05:56:25</td>
      <td>9611710</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Greys.Anatomy.S15E16.HDTV.x264-KILLERS</td>
      <td>23.976</td>
      <td>15.0</td>
      <td>16.0</td>
      <td>413573.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678545...</td>
    </tr>
    <tr>
      <th>4336535</th>
      <td>7678546</td>
      <td>"Grey's Anatomy" Blood and Water</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 05:56:42</td>
      <td>9611710</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Greys.Anatomy.S15E16.HDTV.x264-KILLERS</td>
      <td>23.976</td>
      <td>15.0</td>
      <td>16.0</td>
      <td>413573.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678546...</td>
    </tr>
    <tr>
      <th>4336536</th>
      <td>7678547</td>
      <td>"Miracle Workers" Episode #1.3</td>
      <td>2019.0</td>
      <td>Romanian</td>
      <td>ro</td>
      <td>2019-03-07 05:58:55</td>
      <td>7793086</td>
      <td>srt</td>
      <td>1.0</td>
      <td>miracle.workers.2019.s01e03.720p.webrip.x264-tbs</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>7529770.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678547...</td>
    </tr>
    <tr>
      <th>4336537</th>
      <td>7678550</td>
      <td>"Poirot" The Theft of the Royal Ruby</td>
      <td>1991.0</td>
      <td>Italian</td>
      <td>it</td>
      <td>2019-03-07 06:30:04</td>
      <td>676187</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Theft of the Royal Ruby (1991)</td>
      <td>25.000</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>94525.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678550...</td>
    </tr>
    <tr>
      <th>4336538</th>
      <td>7678552</td>
      <td>Scars of Xavier</td>
      <td>2017.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 06:30:39</td>
      <td>7346786</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Scars.of.Xavier.2017.HDRip.AC3.X264-CMRG</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678552...</td>
    </tr>
    <tr>
      <th>4336539</th>
      <td>7678556</td>
      <td>"I Am the Night" Queen's Gambit, Accepted</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 06:46:50</td>
      <td>7767664</td>
      <td>srt</td>
      <td>1.0</td>
      <td>I.Am.the.Night.S01E06.720p.AMZN.WEBRip.DDP5.1....</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>6.0</td>
      <td>7186588.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678556...</td>
    </tr>
    <tr>
      <th>4336540</th>
      <td>7678557</td>
      <td>"New Amsterdam" Anima Sola</td>
      <td>2019.0</td>
      <td>Finnish</td>
      <td>fi</td>
      <td>2019-03-07 06:48:56</td>
      <td>9556974</td>
      <td>srt</td>
      <td>1.0</td>
      <td>New.Amsterdam.2018.S01E12.720p.HEVC.x265-MeGus...</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>12.0</td>
      <td>7817340.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678557...</td>
    </tr>
    <tr>
      <th>4336541</th>
      <td>7678558</td>
      <td>"Ray Donovan" Chinese Algebra</td>
      <td>2016.0</td>
      <td>Hebrew</td>
      <td>he</td>
      <td>2019-03-07 07:01:26</td>
      <td>5347010</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ray.Donovan.S04E11.720p.HDTV.x264-FLEET (1)</td>
      <td>25.000</td>
      <td>4.0</td>
      <td>11.0</td>
      <td>2249007.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678558...</td>
    </tr>
    <tr>
      <th>4336542</th>
      <td>7678559</td>
      <td>"Documentary Now!" Episode #3.4</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:11:11</td>
      <td>8211428</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Documentary.Now.S03E04.480p.x264-mSD</td>
      <td>0.000</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>4677934.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678559...</td>
    </tr>
    <tr>
      <th>4336543</th>
      <td>7678562</td>
      <td>Mary Poppins Returns</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:22:17</td>
      <td>5028340</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Mary.Poppins.Returns.2019.DVDRip.XviD.AC3-EVO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678562...</td>
    </tr>
    <tr>
      <th>4336544</th>
      <td>7678565</td>
      <td>Ralph Breaks the Internet</td>
      <td>2018.0</td>
      <td>Greek</td>
      <td>el</td>
      <td>2019-03-07 07:31:26</td>
      <td>5848272</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ralph.Breaks.The.Internet.2018.1080p.WEBRip.x2...</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678565...</td>
    </tr>
    <tr>
      <th>4336545</th>
      <td>7678566</td>
      <td>"New Amsterdam" Croaklahoma</td>
      <td>2019.0</td>
      <td>Danish</td>
      <td>da</td>
      <td>2019-03-07 07:33:09</td>
      <td>9809748</td>
      <td>srt</td>
      <td>1.0</td>
      <td>New.Amsterdam.2018.S01E15.iNTERNAL.720p.WEB.h...</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>7817340.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678566...</td>
    </tr>
    <tr>
      <th>4336546</th>
      <td>7678567</td>
      <td>"New Amsterdam" Croaklahoma</td>
      <td>2019.0</td>
      <td>Finnish</td>
      <td>fi</td>
      <td>2019-03-07 07:33:23</td>
      <td>9809748</td>
      <td>srt</td>
      <td>1.0</td>
      <td>New.Amsterdam.2018.S01E15.iNTERNAL.720p.WEB.h...</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>7817340.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678567...</td>
    </tr>
    <tr>
      <th>4336547</th>
      <td>7678569</td>
      <td>La pelle</td>
      <td>1981.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:35:10</td>
      <td>82893</td>
      <td>srt</td>
      <td>1.0</td>
      <td>vsn: 2h13'22''; remestered</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678569...</td>
    </tr>
    <tr>
      <th>4336548</th>
      <td>7678570</td>
      <td>Aki tachinu</td>
      <td>1960.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:35:46</td>
      <td>53578</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Aki.Tachinu.1960.Naruse</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678570...</td>
    </tr>
    <tr>
      <th>4336549</th>
      <td>7678573</td>
      <td>Elephant White</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:39:45</td>
      <td>1578882</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Elephant.White.2011.DUAL.COMPLETE.BLURAY-CLASH</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678573...</td>
    </tr>
    <tr>
      <th>4336550</th>
      <td>7678574</td>
      <td>"Gotham" Legend of the Dark Knight: Nothing's ...</td>
      <td>2019.0</td>
      <td>Spanish</td>
      <td>es</td>
      <td>2019-03-07 07:42:54</td>
      <td>8413462</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Gotham 5x08 - Nothing's Shocking</td>
      <td>0.000</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>3749900.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678574...</td>
    </tr>
    <tr>
      <th>4336551</th>
      <td>7678575</td>
      <td>"White Gold" Episode #2.1</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 08:06:48</td>
      <td>7082412</td>
      <td>srt</td>
      <td>1.0</td>
      <td>White.Gold.S02E01.HDTV.x264-RBB</td>
      <td>25.000</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>6010920.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678575...</td>
    </tr>
    <tr>
      <th>4336552</th>
      <td>7678576</td>
      <td>"Ray Donovan" Rattus Rattus</td>
      <td>2016.0</td>
      <td>Hebrew</td>
      <td>he</td>
      <td>2019-03-07 08:12:59</td>
      <td>4937254</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ray.Donovan.S04E12.720p.HDTV.x264-AVS</td>
      <td>25.000</td>
      <td>4.0</td>
      <td>12.0</td>
      <td>2249007.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678576...</td>
    </tr>
    <tr>
      <th>4336553</th>
      <td>7678582</td>
      <td>"Shameless" BOOOOOOOOOOOONE!</td>
      <td>2019.0</td>
      <td>Bosnian</td>
      <td>bs</td>
      <td>2019-03-07 08:32:19</td>
      <td>8245474</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Shameless.US.S09E09.Boooooooooooone.720p.AMZN...</td>
      <td>23.976</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>1586680.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678582...</td>
    </tr>
    <tr>
      <th>4336554</th>
      <td>7678588</td>
      <td>"The Umbrella Academy" I Heard a Rumor</td>
      <td>2019.0</td>
      <td>Japanese</td>
      <td>ja</td>
      <td>2019-03-07 08:36:19</td>
      <td>8407436</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Umbrella.Academy.S01E08.I.Heard.a.Rumor.10...</td>
      <td>23.976</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>1312171.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678588...</td>
    </tr>
    <tr>
      <th>4336555</th>
      <td>7678591</td>
      <td>"ER" Another Perfect Day</td>
      <td>1994.0</td>
      <td>Polish</td>
      <td>pl</td>
      <td>2019-03-07 08:39:53</td>
      <td>567926</td>
      <td>srt</td>
      <td>1.0</td>
      <td>ER.S01E07.Another.Perfect.Day.1080p.WEB-DL.DD+...</td>
      <td>0.000</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>108757.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678591...</td>
    </tr>
    <tr>
      <th>4336556</th>
      <td>7678594</td>
      <td>Vacation</td>
      <td>1983.0</td>
      <td>Korean</td>
      <td>ko</td>
      <td>2019-03-07 08:59:28</td>
      <td>85995</td>
      <td>srt</td>
      <td>1.0</td>
      <td>National Lampoon's Vacation</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678594...</td>
    </tr>
    <tr>
      <th>4336557</th>
      <td>7678595</td>
      <td>"Suits" Stalking Horse</td>
      <td>2019.0</td>
      <td>Czech</td>
      <td>cs</td>
      <td>2019-03-07 09:00:04</td>
      <td>9318636</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Suits.S08E15.720p.HDTV.x264-AVS</td>
      <td>23.976</td>
      <td>8.0</td>
      <td>15.0</td>
      <td>1632701.0</td>
      <td>tv</td>
      <td>http://www.opensubtitles.org/subtitles/7678595...</td>
    </tr>
  </tbody>
</table>
<p>4336558 rows × 16 columns</p>
</div>




```python
df.shape
```




    (4336558, 16)




```python
df2 = df[df.MovieKind == 'movie']
df2 = df2[df2.ISO639 == 'en']
df2.shape
```




    (228490, 16)




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>IDSubtitle</th>
      <th>MovieName</th>
      <th>MovieYear</th>
      <th>LanguageName</th>
      <th>ISO639</th>
      <th>SubAddDate</th>
      <th>ImdbID</th>
      <th>SubFormat</th>
      <th>SubSumCD</th>
      <th>MovieReleaseName</th>
      <th>MovieFPS</th>
      <th>SeriesSeason</th>
      <th>SeriesEpisode</th>
      <th>SeriesIMDBParent</th>
      <th>MovieKind</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Alien3</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-10-31 23:54:23</td>
      <td>103644</td>
      <td>sub</td>
      <td>2.0</td>
      <td>Alien.3</td>
      <td>11.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/1/alien...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Ghost in the Shell 2: Innocence</td>
      <td>2004.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-10-31 23:54:23</td>
      <td>347246</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Innocence.2004.DVDRip.XviD</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3/ghost...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>The City of Lost Children</td>
      <td>1995.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-01 20:11:53</td>
      <td>112682</td>
      <td>srt</td>
      <td>2.0</td>
      <td>The.City.Of.Lost.Children.1995.iNTERNAL.DVDRi...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5/the-c...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Jui kuen II</td>
      <td>1994.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 17:11:34</td>
      <td>111512</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Drunken.Master.2.Uncut.DVD-Rip.By.Ghost</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/13/jui-...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>House of Flying Daggers</td>
      <td>2004.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 17:16:21</td>
      <td>385004</td>
      <td>srt</td>
      <td>2.0</td>
      <td>House.Of.Flying.Daggers.2004.RETAIL.DVDRip.XV...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/14/hous...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>Lu ding ji</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:45:50</td>
      <td>104770</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Stephen Chow - Royal Tramp 1</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/16/lu-d...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>Rashomon</td>
      <td>1950.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:52:44</td>
      <td>42876</td>
      <td>srt</td>
      <td>1.0</td>
      <td>rashomon_(1950).earthling10480.sharereactor</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/17/rash...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Rashomon</td>
      <td>1950.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:52:44</td>
      <td>42876</td>
      <td>smi</td>
      <td>1.0</td>
      <td>rashomon_(1950).garandou.sharereactor</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/18/rash...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>20</td>
      <td>Hei kek ji wong</td>
      <td>1999.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 20:58:02</td>
      <td>188766</td>
      <td>srt</td>
      <td>1.0</td>
      <td>King of Comedy</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/20/hei-...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>21</td>
      <td>Spirited Away</td>
      <td>2001.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:04:23</td>
      <td>245429</td>
      <td>sub</td>
      <td>2.0</td>
      <td>Spirited Away - DVDRip</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/21/spir...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>23</td>
      <td>Back to the Future Part II</td>
      <td>1989.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:15:46</td>
      <td>96874</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Back To The Future II - English</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/23/back...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>24</td>
      <td>Ghost Ship</td>
      <td>2002.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:47:29</td>
      <td>288477</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Ghost Ship.English</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/24/ghos...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>26</td>
      <td>Lu ding ji II: Zhi shen long jiao</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 21:55:18</td>
      <td>104771</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Stephen Chow - Royal Tramp 2</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/26/lu-d...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>28</td>
      <td>I Spy</td>
      <td>2002.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 22:11:29</td>
      <td>297181</td>
      <td>srt</td>
      <td>1.0</td>
      <td>I Spy.English</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/28/i-sp...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>29</td>
      <td>Dead Ringers</td>
      <td>1988.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-11-04 22:15:53</td>
      <td>94964</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Dead.Ringers.(1988).DVDRip.DivX3LM</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/29/dead...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>32</td>
      <td>Gojira X Mekagojira</td>
      <td>2002.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-12-12 17:45:41</td>
      <td>314111</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Godzilla X MechaGodzilla (Hand Made)</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/32/goji...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>65</td>
      <td>Brainstorm</td>
      <td>1983.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-01-30 15:24:05</td>
      <td>85271</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Brainstorm (1983)</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/65/brai...</td>
    </tr>
    <tr>
      <th>71</th>
      <td>67</td>
      <td>A Boy and His Dog</td>
      <td>1975.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-01-30 15:34:16</td>
      <td>72730</td>
      <td>sub</td>
      <td>1.0</td>
      <td>A Boy And His Dog (1975)</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/67/a-bo...</td>
    </tr>
    <tr>
      <th>76</th>
      <td>72</td>
      <td>Reservoir Dogs</td>
      <td>1992.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-01 00:44:58</td>
      <td>105236</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Reservoir Dogs - 1992 - [TWB]</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/72/rese...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>74</td>
      <td>A Tale of Two Sisters</td>
      <td>2003.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-01 01:06:07</td>
      <td>365376</td>
      <td>srt</td>
      <td>2.0</td>
      <td>A.Tale.of.Two.Sisters.BiFOS</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/74/a-ta...</td>
    </tr>
    <tr>
      <th>79</th>
      <td>75</td>
      <td>Audition</td>
      <td>1997.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-01 01:24:58</td>
      <td>295867</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Audition_(1999).Japanese.SAPHiRE.ShareReactor</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/75/audi...</td>
    </tr>
    <tr>
      <th>80</th>
      <td>76</td>
      <td>Beautiful Creatures</td>
      <td>2000.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-01 01:34:07</td>
      <td>221889</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Beautiful Creatures [dvdrip] [divx pro 5.0.5]</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/76/beau...</td>
    </tr>
    <tr>
      <th>84</th>
      <td>80</td>
      <td>Crumb</td>
      <td>1994.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-03 00:56:49</td>
      <td>109508</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Crumb (1994) Kyprios.English</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/80/crum...</td>
    </tr>
    <tr>
      <th>85</th>
      <td>81</td>
      <td>Shao Lin si</td>
      <td>1982.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-03 01:33:16</td>
      <td>79891</td>
      <td>srt</td>
      <td>2.0</td>
      <td>The.Shaolin.Temple.1979.DVDRip.XviD.AC3.TEAM ...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/81/shao...</td>
    </tr>
    <tr>
      <th>90</th>
      <td>86</td>
      <td>Angel Heart</td>
      <td>1987.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-04 08:53:58</td>
      <td>92563</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/86/ange...</td>
    </tr>
    <tr>
      <th>92</th>
      <td>88</td>
      <td>Hi no tori</td>
      <td>1978.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-05 22:16:59</td>
      <td>77673</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Hi No Tori (The Phoenix) - (Kon Ichikawa, 197...</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/88/hi-n...</td>
    </tr>
    <tr>
      <th>100</th>
      <td>97</td>
      <td>La Grande Illusion</td>
      <td>1937.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-12 21:16:08</td>
      <td>28950</td>
      <td>srt</td>
      <td>2.0</td>
      <td>2_La.Grande.Illusion.(1937).Jean.Renoir</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/97/la-g...</td>
    </tr>
    <tr>
      <th>101</th>
      <td>98</td>
      <td>The Return</td>
      <td>2003.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-14 00:42:56</td>
      <td>376968</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Return</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/98/the-...</td>
    </tr>
    <tr>
      <th>103</th>
      <td>101</td>
      <td>Revenge of the Pink Panther</td>
      <td>1978.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-16 00:52:29</td>
      <td>78163</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Revenge.Of.The.Pink.Panther.(1978)</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/101/rev...</td>
    </tr>
    <tr>
      <th>117</th>
      <td>109</td>
      <td>Persona</td>
      <td>1966.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-02-19 13:27:52</td>
      <td>60827</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Persona</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/109/per...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4336088</th>
      <td>7677655</td>
      <td>A Haunting on Finn Road: The Devil's Grove</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:27:41</td>
      <td>9584192</td>
      <td>srt</td>
      <td>1.0</td>
      <td>DVDRip.x264-REGRET</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677655...</td>
    </tr>
    <tr>
      <th>4336090</th>
      <td>7677659</td>
      <td>Holmes &amp; Watson</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:34:36</td>
      <td>1255919</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Holmes.and.Watson.2018.HDCAM</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677659...</td>
    </tr>
    <tr>
      <th>4336091</th>
      <td>7677660</td>
      <td>Holmes &amp; Watson</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:34:58</td>
      <td>1255919</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Holmes.and.Watson.2018.HDCAM</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677660...</td>
    </tr>
    <tr>
      <th>4336092</th>
      <td>7677661</td>
      <td>Polisse</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:35:21</td>
      <td>1661420</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Polisse.2011.DVDRip.x264</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677661...</td>
    </tr>
    <tr>
      <th>4336093</th>
      <td>7677665</td>
      <td>Glass</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:37:38</td>
      <td>6823368</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Glass.2019.NEW.HDCAM.x264.AC3-ETRG</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677665...</td>
    </tr>
    <tr>
      <th>4336094</th>
      <td>7677668</td>
      <td>Glass</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:38:53</td>
      <td>6823368</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Glass.2019.NEW.HDCAM.x264.AC3-ETRG</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677668...</td>
    </tr>
    <tr>
      <th>4336095</th>
      <td>7677669</td>
      <td>Apocalypse Now</td>
      <td>1979.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 07:39:31</td>
      <td>78788</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Apocalypse.Now.Redux.1979.1080p.BluRay.X264-Ja...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677669...</td>
    </tr>
    <tr>
      <th>4336106</th>
      <td>7677699</td>
      <td>Uri: The Surgical Strike</td>
      <td>2019.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 09:15:21</td>
      <td>8291224</td>
      <td>srt</td>
      <td>1.0</td>
      <td>URI The Surgical Strike (2019) Hindi HDRip - 7...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677699...</td>
    </tr>
    <tr>
      <th>4336188</th>
      <td>7677844</td>
      <td>The Third Secret</td>
      <td>1964.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 13:09:02</td>
      <td>58649</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Third.Secret.1964.720p.BluRay.x264-GHOULS</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677844...</td>
    </tr>
    <tr>
      <th>4336189</th>
      <td>7677845</td>
      <td>The Third Secret</td>
      <td>1964.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 13:09:12</td>
      <td>58649</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Third.Secret.1964.720p.BluRay.x264-GHOULS</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677845...</td>
    </tr>
    <tr>
      <th>4336190</th>
      <td>7677846</td>
      <td>Las palabras de Max</td>
      <td>1978.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 13:10:10</td>
      <td>76520</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.FO.WEB-DL.AAC2.0.H.264-CREATiVE</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677846...</td>
    </tr>
    <tr>
      <th>4336238</th>
      <td>7677942</td>
      <td>A Charlie Brown Valentine</td>
      <td>2002.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 15:01:06</td>
      <td>283987</td>
      <td>srt</td>
      <td>1.0</td>
      <td>A.Charlie.Brown.Valentine.2002.1080p.WEBRip.A...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677942...</td>
    </tr>
    <tr>
      <th>4336254</th>
      <td>7677968</td>
      <td>The Girl in the Spider's Web</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 15:30:28</td>
      <td>5177088</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.BluRay.x264-DRONES (Director Commentary ...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677968...</td>
    </tr>
    <tr>
      <th>4336255</th>
      <td>7677970</td>
      <td>Empire of the Sun</td>
      <td>1987.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 15:33:47</td>
      <td>92965</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Empire of the Sun (1987)23.976fps- 152.49 min...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7677970...</td>
    </tr>
    <tr>
      <th>4336265</th>
      <td>7678011</td>
      <td>Thank You for Smoking</td>
      <td>2005.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 16:11:16</td>
      <td>427944</td>
      <td>srt</td>
      <td>1.0</td>
      <td>thank.you.for.smoking.2005.1080p.hdtv.x264-re...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678011...</td>
    </tr>
    <tr>
      <th>4336266</th>
      <td>7678012</td>
      <td>Thank You for Smoking</td>
      <td>2005.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 16:12:32</td>
      <td>427944</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.AMZN.WEB-DL.DD+5.1.H.264-SiGMA</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678012...</td>
    </tr>
    <tr>
      <th>4336299</th>
      <td>7678088</td>
      <td>Ying</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 17:44:52</td>
      <td>6864046</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Shadow.2018.CHINESE.720p.BluRay.H264.AAC-VXT</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678088...</td>
    </tr>
    <tr>
      <th>4336300</th>
      <td>7678092</td>
      <td>The Intent 2: The Come Up</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 17:54:08</td>
      <td>7613996</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.WEB-DL.H264.AC3-EVO</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678092...</td>
    </tr>
    <tr>
      <th>4336417</th>
      <td>7678314</td>
      <td>City of Ember</td>
      <td>2008.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 21:00:04</td>
      <td>970411</td>
      <td>srt</td>
      <td>1.0</td>
      <td>City.of.Ember.2008.1080p.BluRay.x264.Remux.VC...</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678314...</td>
    </tr>
    <tr>
      <th>4336438</th>
      <td>7678347</td>
      <td>Bad Boys</td>
      <td>1995.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 21:41:38</td>
      <td>112442</td>
      <td>srt</td>
      <td>1.0</td>
      <td>BdBys (1995) BRRip 550mb</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678347...</td>
    </tr>
    <tr>
      <th>4336452</th>
      <td>7678374</td>
      <td>Eloisa esta debajo de un almendro</td>
      <td>1943.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-06 22:00:45</td>
      <td>35840</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.FO.WEB-DL.AAC2.0.H.264-CREATiVE</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678374...</td>
    </tr>
    <tr>
      <th>4336504</th>
      <td>7678483</td>
      <td>L'ordre</td>
      <td>1973.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 01:15:57</td>
      <td>234401</td>
      <td>srt</td>
      <td>1.0</td>
      <td>l'ordre.1973</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678483...</td>
    </tr>
    <tr>
      <th>4336519</th>
      <td>7678517</td>
      <td>Tangent Room</td>
      <td>2017.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 02:55:59</td>
      <td>4230078</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Tangent.Room.2019.HDRip.XviD.AC3-EVO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678517...</td>
    </tr>
    <tr>
      <th>4336521</th>
      <td>7678519</td>
      <td>Tangent Room</td>
      <td>2017.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 02:56:39</td>
      <td>4230078</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Tangent.Room.2019.HDRip.XviD.AC3-EVO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678519...</td>
    </tr>
    <tr>
      <th>4336525</th>
      <td>7678525</td>
      <td>100 Yards</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 03:12:33</td>
      <td>5258106</td>
      <td>srt</td>
      <td>1.0</td>
      <td>100 Yards 2018.HDRip.XviD.AC3-EVO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678525...</td>
    </tr>
    <tr>
      <th>4336538</th>
      <td>7678552</td>
      <td>Scars of Xavier</td>
      <td>2017.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 06:30:39</td>
      <td>7346786</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Scars.of.Xavier.2017.HDRip.AC3.X264-CMRG</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678552...</td>
    </tr>
    <tr>
      <th>4336543</th>
      <td>7678562</td>
      <td>Mary Poppins Returns</td>
      <td>2018.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:22:17</td>
      <td>5028340</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Mary.Poppins.Returns.2019.DVDRip.XviD.AC3-EVO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678562...</td>
    </tr>
    <tr>
      <th>4336547</th>
      <td>7678569</td>
      <td>La pelle</td>
      <td>1981.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:35:10</td>
      <td>82893</td>
      <td>srt</td>
      <td>1.0</td>
      <td>vsn: 2h13'22''; remestered</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678569...</td>
    </tr>
    <tr>
      <th>4336548</th>
      <td>7678570</td>
      <td>Aki tachinu</td>
      <td>1960.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:35:46</td>
      <td>53578</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Aki.Tachinu.1960.Naruse</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678570...</td>
    </tr>
    <tr>
      <th>4336549</th>
      <td>7678573</td>
      <td>Elephant White</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2019-03-07 07:39:45</td>
      <td>1578882</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Elephant.White.2011.DUAL.COMPLETE.BLURAY-CLASH</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7678573...</td>
    </tr>
  </tbody>
</table>
<p>228490 rows × 16 columns</p>
</div>




```python
df2.URL[:2]
```




    0    http://www.opensubtitles.org/subtitles/1/alien...
    2    http://www.opensubtitles.org/subtitles/3/ghost...
    Name: URL, dtype: object




```python
df2.sort_values('ImdbID')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>IDSubtitle</th>
      <th>MovieName</th>
      <th>MovieYear</th>
      <th>LanguageName</th>
      <th>ISO639</th>
      <th>SubAddDate</th>
      <th>ImdbID</th>
      <th>SubFormat</th>
      <th>SubSumCD</th>
      <th>MovieReleaseName</th>
      <th>MovieFPS</th>
      <th>SeriesSeason</th>
      <th>SeriesEpisode</th>
      <th>SeriesIMDBParent</th>
      <th>MovieKind</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3960657</th>
      <td>7270681</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-29 23:14:13</td>
      <td>0</td>
      <td>srt</td>
      <td>3.0</td>
      <td>Itineraire d'un cine-fils 2</td>
      <td>25.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7270681...</td>
    </tr>
    <tr>
      <th>4224585</th>
      <td>7550945</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2018-11-23 07:12:11</td>
      <td>0</td>
      <td>srt</td>
      <td>1.0</td>
      <td>One Direction: I Want</td>
      <td>25.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7550945...</td>
    </tr>
    <tr>
      <th>2759683</th>
      <td>5924110</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2014-12-10 05:38:47</td>
      <td>0</td>
      <td>srt</td>
      <td>112.0</td>
      <td>MOOC Video Collection [ml-class] [Stanford Mac...</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5924110...</td>
    </tr>
    <tr>
      <th>3958932</th>
      <td>7268820</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2005-03-01 00:00:00</td>
      <td>0</td>
      <td>sub</td>
      <td>1.0</td>
      <td>the.sounds.of.soul eng</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7268820...</td>
    </tr>
    <tr>
      <th>188072</th>
      <td>7268819</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2005-03-01 00:00:00</td>
      <td>0</td>
      <td>sub</td>
      <td>1.0</td>
      <td>britan.invades.america.fights.back en</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7268819...</td>
    </tr>
    <tr>
      <th>92669</th>
      <td>7270951</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>English</td>
      <td>en</td>
      <td>2005-03-31 00:00:00</td>
      <td>0</td>
      <td>srt</td>
      <td>4.0</td>
      <td>Prologo</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7270951...</td>
    </tr>
    <tr>
      <th>3419513</th>
      <td>6686908</td>
      <td>Rocco Ravishes St. Petersburg</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2016-07-17 16:39:46</td>
      <td>1000000</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Joseph Stiglitz - Can we make a gobalization t...</td>
      <td>24.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6686908...</td>
    </tr>
    <tr>
      <th>254106</th>
      <td>3102632</td>
      <td>Painful Deceptions</td>
      <td>2006.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-02-12 19:13:45</td>
      <td>10000011</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Painful Deceptions</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3102632...</td>
    </tr>
    <tr>
      <th>378932</th>
      <td>3251921</td>
      <td>Himekishi Lilia</td>
      <td>2006.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-02-21 13:15:53</td>
      <td>10000020</td>
      <td>ssa</td>
      <td>1.0</td>
      <td>Himekishi Lilia Vol.3</td>
      <td>23.976</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3251921...</td>
    </tr>
    <tr>
      <th>378930</th>
      <td>3251919</td>
      <td>Himekishi Lilia</td>
      <td>2006.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-02-21 13:11:46</td>
      <td>10000020</td>
      <td>ssa</td>
      <td>1.0</td>
      <td>[X-SASG] Himekishi Lilia 1.mkv</td>
      <td>23.976</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3251919...</td>
    </tr>
    <tr>
      <th>378931</th>
      <td>3251920</td>
      <td>Himekishi Lilia</td>
      <td>2006.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-02-21 13:13:26</td>
      <td>10000020</td>
      <td>ssa</td>
      <td>1.0</td>
      <td>Himekishi Lilia Vol.2</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3251920...</td>
    </tr>
    <tr>
      <th>380267</th>
      <td>3253382</td>
      <td>Swishahouse feat. Webbie Lil' Keke &amp; Yung Redd...</td>
      <td>2008.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-02-25 15:43:18</td>
      <td>10000023</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Swishahouse feat. Webbie Lil' Keke &amp; Yung Redd...</td>
      <td>29.970</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3253382...</td>
    </tr>
    <tr>
      <th>320839</th>
      <td>3174545</td>
      <td>Billy &amp; Mandy's Big Boogey Adventure</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-01-05 15:38:58</td>
      <td>1000070</td>
      <td>srt</td>
      <td>1.0</td>
      <td>wpi</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3174545...</td>
    </tr>
    <tr>
      <th>788904</th>
      <td>3694495</td>
      <td>Bulletproof</td>
      <td>2006.0</td>
      <td>English</td>
      <td>en</td>
      <td>2010-06-29 03:38:25</td>
      <td>1000072</td>
      <td>srt</td>
      <td>1.0</td>
      <td>bulletproof [A Release-lounge H264]</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3694495...</td>
    </tr>
    <tr>
      <th>128246</th>
      <td>130493</td>
      <td>Liu jai yim taam</td>
      <td>1987.0</td>
      <td>English</td>
      <td>en</td>
      <td>2003-01-14 00:00:00</td>
      <td>100014</td>
      <td>srt</td>
      <td>1.0</td>
      <td>EROTIC GHOST STORY</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/130493/...</td>
    </tr>
    <tr>
      <th>212312</th>
      <td>215629</td>
      <td>Liu jai yim taam</td>
      <td>1987.0</td>
      <td>English</td>
      <td>en</td>
      <td>2005-03-01 00:00:00</td>
      <td>100014</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Erotic ghost story dvdrip engsub</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/215629/...</td>
    </tr>
    <tr>
      <th>296045</th>
      <td>3147544</td>
      <td>Sing kung chok tse sup yut tam</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-09-17 20:41:41</td>
      <td>1000158</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Whispers and Moans</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3147544...</td>
    </tr>
    <tr>
      <th>284088</th>
      <td>3134963</td>
      <td>Sing kung chok tse sup yut tam</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-07-15 13:24:29</td>
      <td>1000158</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Whipsers.And.Moans.2007.DVDRip.XViD-BiEN</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3134963...</td>
    </tr>
    <tr>
      <th>2647307</th>
      <td>5804779</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2014-08-29 04:37:47</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Life.Is.Sweet.1990.Criterion.Collection.720p.B...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5804779...</td>
    </tr>
    <tr>
      <th>1815895</th>
      <td>4865410</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2013-03-14 13:41:03</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Life is Sweet (1990).DVDRip.XviD</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4865410...</td>
    </tr>
    <tr>
      <th>276455</th>
      <td>3127013</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-05-29 22:24:38</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3127013...</td>
    </tr>
    <tr>
      <th>2086238</th>
      <td>5177500</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2013-09-15 07:20:28</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Life.is.Sweet.1990.1080p.Criterion.Bluray.X264...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5177500...</td>
    </tr>
    <tr>
      <th>2031495</th>
      <td>5118353</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2013-08-03 18:25:04</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>life.is.sweet.1990.720p.bluray.x264-unveil</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5118353...</td>
    </tr>
    <tr>
      <th>2981350</th>
      <td>6168489</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-05-10 21:05:34</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Life.Is.Sweet.1990.Proper.1080p.x264-SONiDO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6168489...</td>
    </tr>
    <tr>
      <th>2981349</th>
      <td>6168488</td>
      <td>Life Is Sweet</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-05-10 21:05:16</td>
      <td>100024</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Life.Is.Sweet.1990.Proper.1080p.x264-SONiDO</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6168488...</td>
    </tr>
    <tr>
      <th>1010961</th>
      <td>3903773</td>
      <td>Lionheart</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2010-10-21 01:03:05</td>
      <td>100029</td>
      <td>srt</td>
      <td>1.0</td>
      <td>lh-vh</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3903773...</td>
    </tr>
    <tr>
      <th>3521897</th>
      <td>6796695</td>
      <td>Lionheart</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2016-11-14 22:49:25</td>
      <td>100029</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Lionheart.1990.THEATRICAL.CUT.1080p.BluRay.H2...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6796695...</td>
    </tr>
    <tr>
      <th>2835153</th>
      <td>6002071</td>
      <td>Lionheart</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-01-14 01:13:23</td>
      <td>100029</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Lionheart 1990.srt</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6002071...</td>
    </tr>
    <tr>
      <th>2970012</th>
      <td>6171434</td>
      <td>Lionheart</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-05-13 11:33:46</td>
      <td>100029</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Lionheart.1990.1080p.BluRay.x264.YIFY</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6171434...</td>
    </tr>
    <tr>
      <th>3688126</th>
      <td>7063608</td>
      <td>Lisa</td>
      <td>1989.0</td>
      <td>English</td>
      <td>en</td>
      <td>2017-08-11 09:56:01</td>
      <td>100031</td>
      <td>srt</td>
      <td>1.0</td>
      <td>lisa.1989.dsr.x264-regret</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7063608...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>204502</th>
      <td>6436947</td>
      <td>Korczak</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-12-25 21:54:06</td>
      <td>99949</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Dottor Korczak</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6436947...</td>
    </tr>
    <tr>
      <th>1215995</th>
      <td>4182738</td>
      <td>Korczak</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-05-23 21:26:09</td>
      <td>99949</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4182738...</td>
    </tr>
    <tr>
      <th>1048595</th>
      <td>3938092</td>
      <td>Kracht</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2010-11-06 13:38:02</td>
      <td>99950</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Kracht.1990.DVDRIP</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3938092...</td>
    </tr>
    <tr>
      <th>3065518</th>
      <td>6267685</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-08-11 15:42:36</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Krays 1990 HDRip-BONE en</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6267685...</td>
    </tr>
    <tr>
      <th>388855</th>
      <td>4198503</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-06-26 17:20:28</td>
      <td>99951</td>
      <td>srt</td>
      <td>2.0</td>
      <td>The.Krays.1990.WS.DVDRip.XviD-FiCO</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4198503...</td>
    </tr>
    <tr>
      <th>258712</th>
      <td>3108125</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-03-01 20:58:30</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Krays.1990.LIMITED.DVDRip.MeSSiaah</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3108125...</td>
    </tr>
    <tr>
      <th>402547</th>
      <td>4198500</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-06-26 17:15:09</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Krays-[1990]-Demonuk[NIKONRG]</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4198500...</td>
    </tr>
    <tr>
      <th>246276</th>
      <td>3094153</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2007-01-07 03:48:20</td>
      <td>99951</td>
      <td>srt</td>
      <td>2.0</td>
      <td>The.Krays.1990.WS.DVDRip.XviD-FiCO</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3094153...</td>
    </tr>
    <tr>
      <th>3743939</th>
      <td>7001208</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2017-06-03 05:56:40</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Krays.1990.720p.WEB-DL.AAC2.0.H264-FGT</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7001208...</td>
    </tr>
    <tr>
      <th>1229603</th>
      <td>4198499</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-06-26 17:15:06</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The Krays-[1990]-Demonuk[NIKONRG]</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4198499...</td>
    </tr>
    <tr>
      <th>3743938</th>
      <td>7001207</td>
      <td>The Krays</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2017-06-03 05:56:10</td>
      <td>99951</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Krays.1990.720p.WEB-DL.AAC2.0.H264-FGT</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7001207...</td>
    </tr>
    <tr>
      <th>3109202</th>
      <td>6315316</td>
      <td>Kuai le de xiao ji</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2015-09-24 09:19:43</td>
      <td>99956</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Kuai.le.de.xiao.ji.1990.D5.x264.2Audio.AAC.480...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6315316...</td>
    </tr>
    <tr>
      <th>1808272</th>
      <td>4857252</td>
      <td>Il 7 e l'8</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2013-03-10 19:24:56</td>
      <td>999864</td>
      <td>srt</td>
      <td>1.0</td>
      <td>IL.7.E.L.8-Ficarra_Picone.2007.iTALiAN.DVDRip-...</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4857252...</td>
    </tr>
    <tr>
      <th>462737</th>
      <td>3365225</td>
      <td>Thomas Kinkade's Christmas Cottage</td>
      <td>2008.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-11-07 19:15:31</td>
      <td>999872</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Thomas.Kinkades.Christmas.Cottage-BULLDOZER (a...</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3365225...</td>
    </tr>
    <tr>
      <th>1235633</th>
      <td>4206645</td>
      <td>Heart of a Soul Surfer</td>
      <td>2007.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-07-13 15:47:42</td>
      <td>999890</td>
      <td>srt</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4206645...</td>
    </tr>
    <tr>
      <th>1467473</th>
      <td>4475967</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2012-02-23 01:05:48</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw.Dogs.2011.x264.DTS-WAF</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4475967...</td>
    </tr>
    <tr>
      <th>1421973</th>
      <td>4423154</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-03 16:54:14</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw.Dogs.2011.DVDRip.XviD-ViP3R</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4423154...</td>
    </tr>
    <tr>
      <th>1421250</th>
      <td>4422075</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-01 22:00:37</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw.Dogs.2011.720p.BluRay.x264-Felony</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4422075...</td>
    </tr>
    <tr>
      <th>993363</th>
      <td>4422412</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-02 12:37:27</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw.Dogs.2011.BDRip.XviD-Larceny</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4422412...</td>
    </tr>
    <tr>
      <th>1421972</th>
      <td>4423153</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-03 16:54:11</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw.Dogs.2011.DVDRip.XviD-ViP3R</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4423153...</td>
    </tr>
    <tr>
      <th>993365</th>
      <td>4422414</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2011-12-02 12:38:31</td>
      <td>999913</td>
      <td>srt</td>
      <td>2.0</td>
      <td>Straw.Dogs.2011.BDRip.XviD-Larceny</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/4422414...</td>
    </tr>
    <tr>
      <th>3880705</th>
      <td>7184584</td>
      <td>Straw Dogs</td>
      <td>2011.0</td>
      <td>English</td>
      <td>en</td>
      <td>2017-12-08 11:50:12</td>
      <td>999913</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Straw Dogs (2011)</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7184584...</td>
    </tr>
    <tr>
      <th>3503267</th>
      <td>6775710</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2016-10-27 07:31:17</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>1080p.WEB-DL.AAC2.0.H264-FGT</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/6775710...</td>
    </tr>
    <tr>
      <th>3954287</th>
      <td>7264736</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2018-02-22 18:46:32</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Leatherface.Texas.Chainsaw.Massacre.III.1990.7...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7264736...</td>
    </tr>
    <tr>
      <th>3600164</th>
      <td>7264737</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2018-02-22 18:46:49</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Leatherface.Texas.Chainsaw.Massacre.III.1990.7...</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7264737...</td>
    </tr>
    <tr>
      <th>630745</th>
      <td>3537308</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2009-07-20 12:33:01</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3537308...</td>
    </tr>
    <tr>
      <th>72741</th>
      <td>72459</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2004-05-24 00:00:00</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Leatherface: Texas Chainsaw Massacre III (1990)</td>
      <td>29.970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/72459/l...</td>
    </tr>
    <tr>
      <th>4108930</th>
      <td>7425616</td>
      <td>Leatherface: Texas Chainsaw Massacre III</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2018-07-21 10:27:01</td>
      <td>99994</td>
      <td>srt</td>
      <td>1.0</td>
      <td>LEATHERFACE (TEXAS CHAINSAW MASSACRE 3) (1990)</td>
      <td>23.976</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/7425616...</td>
    </tr>
    <tr>
      <th>2003116</th>
      <td>5086910</td>
      <td>Lebedyne ozero-zona</td>
      <td>1990.0</td>
      <td>English</td>
      <td>en</td>
      <td>2013-07-14 09:09:23</td>
      <td>99995</td>
      <td>srt</td>
      <td>1.0</td>
      <td>Lebedyne ozero-zona</td>
      <td>25.000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/5086910...</td>
    </tr>
    <tr>
      <th>407840</th>
      <td>3289866</td>
      <td>The Fear Chamber</td>
      <td>2009.0</td>
      <td>English</td>
      <td>en</td>
      <td>2008-05-29 14:17:13</td>
      <td>999972</td>
      <td>srt</td>
      <td>1.0</td>
      <td>The.Fear.Chamber.FS.DVDRip.XviD-ARiSCO</td>
      <td>23.980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>movie</td>
      <td>http://www.opensubtitles.org/subtitles/3289866...</td>
    </tr>
  </tbody>
</table>
<p>228490 rows × 16 columns</p>
</div>




```python
for d in df.URL[:3]:
    print(d)
```

    http://www.opensubtitles.org/subtitles/1/alien3-en
    http://www.opensubtitles.org/subtitles/2/identity-sl
    http://www.opensubtitles.org/subtitles/3/ghost-in-the-shell-2-innocence-en



```python

```
