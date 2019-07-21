

```python
from collections import namedtuple
from itertools import groupby

def parse_subtitle(filename):
    # "chunk" our input file, delimited by blank lines
    with open(filename) as f:
        res = [list(g) for b,g in groupby(f, lambda x: bool(x.strip())) if b]

    Subtitle = namedtuple('Subtitle', 'number start end content')

    subs = []

    for sub in res:
        if len(sub) >= 3: # not strictly necessary, but better safe than sorry
            sub = [x.strip() for x in sub]
            number, start_end, *content = sub # py3 syntax
            start, end = start_end.split(' --> ')
            subs.append(Subtitle(number, start, end, content))
    
    return subs

subs = parse_subtitle("/home/burak/Documents/Courses-2016f/CS464/Project/tension-measuring/castaway.srt")
```


```python
import datetime as dt
from datetime import timedelta 

def str_to_timedelta(str_tm="02:14:53,085"):
    hours, mins, secs = str_tm.split(':')
    millis = secs[3:]
    secs = secs[:2]
    return timedelta(hours=int(hours), minutes=int(mins), seconds=int(secs), milliseconds=int(millis))

def count_intervals(subs, minute_interval):
        end_of_movie = subs[-1].end
        curr_time = timedelta() #this is our t_0
        
        movie_length_mins = int(str_to_timedelta(end_of_movie).total_seconds() / 60 ) + 1
        # counts = [ [] for i in range(movie_length_mins)]
        counts = [0] * (int(movie_length_mins / minute_interval) + 1)
#         for index, sub in enumerate(subs):
#             if (str_to_timedelta(sub.start) - curr_time).seconds <= 60:
#                 counts[index]

        mins = minute_interval
        hours = 0
        index = 0
        for sub in subs:
            if int(sub.start[3:5]) <= mins and \
                int(sub.start[:2]) == hours:
                counts[index] += 1
            elif int(sub.start[:2]) == hours + 1: 
                hours += 1
                mins = 0
                index += 1
                counts[index] += 1
            elif int(sub.start[3:5]) > mins:
                mins += minute_interval
                index += 1
                counts[index] += 1

        return counts
    
count_intervals(subs, 10)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-26-eef5bb958bc6> in <module>()
         37         return counts
         38 
    ---> 39 count_intervals(subs, 10)
    

    <ipython-input-26-eef5bb958bc6> in count_intervals(subs, minute_interval)
         33                 mins += minute_interval
         34                 index += 1
    ---> 35                 counts[index] += 1
         36 
         37         return counts


    IndexError: list index out of range



```python
import datetime as dt
from datetime import timedelta 

# start_time = dt.time(0, 0, 0, 0)
str_tm = "02:14:53,085"
# # millis = int(str_tm[str_tm.find(',')+1:])
# # str_tm = str_tm[:str_tm.find(',')]
# tm = dt.datetime.strptime(str_tm, "%H:%M:%S,%f").time()
hours, mins, secs = str_tm.split(':')
millis = secs[3:]
secs = secs[:2]
print(timedelta(hours=int(hours), minutes=int(mins), seconds=int(secs), milliseconds=int(millis)))
# print(tm)
# tm + timedelta(seconds=3)
```

    2:14:53.085000



```python
start='00:03:00,613'
```
