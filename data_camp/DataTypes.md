# Data Types

## 1. Basic types

### 1.1 Lists

`.extend()`: combine another list <br/>
`.index()`: find the posiiton of an item <br/>
`.pop()`: remove item <br/>
`sorted(list, reverse = True))`: sort in order <br/>

### 1.2 Tuples

**immutable and ordered**


```python
# make something immediately a tuple
error = 'trailing comma',
print(type(error))
```

    <class 'tuple'>


### 1.3 Sets

**unique and unordered**

`.union`: set 1 + set 2 <br/>
`.inntersection`: set 1 overlaps with set2 <br/>
`.difference`: difference between set 1 and set 2

### 1.4 Dictionaries

`for key, value in dictionary.items()` <br/>
`dict[key] = value` <br/>
`.get(key, 'not found')`: safely find key from the dict or 'not found' <br/>
`.update([key1, value1], [key2, value2])` <br/>
`.pop(key, {})`: safely remove key's value with an empty dict
`del dict[key]` <br/>
`if key in dict`<br/>

### 1.5 Read file using CSV reader
`import csv`
`csvfile = open('name.csv', 'r')`
`for row in csv.reader(csvfile)`

## 2. Collections Module for Counting
Counter <br/>
defaultdict <br/>
OrderedDict <br/> 
namedtuple <br/>



```python
from collections import Counter

stations = ['stationname', 'Austin-Forest Park', 
            'Austin-Forest Park', 'Austin-Forest Park', 
            'Austin-Forest Park', 'Austin-Forest Park', 
            'Austin-Forest Park', 'Austin-Forest Park', 
            'Austin-Forest Park', 'Austin-Forest Park']

station_count = Counter(stations)

print(station_count)
print(station_count.most_common(1))
```

    Counter({'Austin-Forest Park': 9, 'stationname': 1})
    [('Austin-Forest Park', 9)]



```python
from collections import defaultdict

entries = [('01/01/2015', 'Austin-Forest Park', 587),
 ('01/02/2015', 'Austin-Forest Park', 1386),
 ('01/03/2015', 'Austin-Forest Park', 785),
 ('01/04/2015', 'Austin-Forest Park', 625),
 ('01/05/2015', 'Austin-Forest Park', 1752),
 ('01/06/2015', 'Austin-Forest Park', 1777),
 ('01/07/2015', 'Austin-Forest Park', 1269),
 ('01/08/2015', 'Austin-Forest Park', 1435),
 ('01/09/2015', 'Austin-Forest Park', 1631),
 ('01/10/2015', 'Austin-Forest Park', 771)]

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

for date, stop, riders in entries:
    ridership[stop].append(riders)

print(list(ridership.items()))
```

    [('Austin-Forest Park', [587, 1386, 785, 625, 1752, 1777, 1269, 1435, 1631, 771])]



```python
from collections import OrderedDict

ridership_date = OrderedDict()

for date, stop, riders in entries:
    if date not in ridership_date:
        ridership_date[date] = 0
    ridership_date[date] += riders

print(list(ridership_date.items()))

# pop the first item and print it
print(ridership_date.popitem(last=False))
print(ridership_date.popitem(last=True))

```

    [('01/01/2015', 587), ('01/02/2015', 1386), ('01/03/2015', 785), ('01/04/2015', 625), ('01/05/2015', 1752), ('01/06/2015', 1777), ('01/07/2015', 1269), ('01/08/2015', 1435), ('01/09/2015', 1631), ('01/10/2015', 771)]
    ('01/01/2015', 587)
    ('01/10/2015', 771)



```python
from collections import namedtuple

DateDetails = namedtuple('Datedetails', ['date', 'stop', 'riders'])
labeled_entries = []

for date, stop, riders in entries:
    labeled_entries.append(DateDetails(date, stop, riders))

print(labeled_entries)
```

    [Datedetails(date='01/01/2015', stop='Austin-Forest Park', riders=587), Datedetails(date='01/02/2015', stop='Austin-Forest Park', riders=1386), Datedetails(date='01/03/2015', stop='Austin-Forest Park', riders=785), Datedetails(date='01/04/2015', stop='Austin-Forest Park', riders=625), Datedetails(date='01/05/2015', stop='Austin-Forest Park', riders=1752), Datedetails(date='01/06/2015', stop='Austin-Forest Park', riders=1777), Datedetails(date='01/07/2015', stop='Austin-Forest Park', riders=1269), Datedetails(date='01/08/2015', stop='Austin-Forest Park', riders=1435), Datedetails(date='01/09/2015', stop='Austin-Forest Park', riders=1631), Datedetails(date='01/10/2015', stop='Austin-Forest Park', riders=771)]



```python
for item in labeled_entries[9:]:
    print(item.stop)
    print(item.date)
    print(item.riders)
```

    Austin-Forest Park
    01/10/2015
    771


## 3.1 DateTime module and usage in python

`.striptime()`: convert date to a datetime object <br/>
`.strftime()` : print out item in a format <br/>
`.isoformat()` : print out item as an ISO standard string <br/>
`.astimezone()`: get the time in another timezone <br/>


```python
from datetime import datetime
local_dt = datetime.now()
print(local_dt)
local_dt.strftime('%m-%d-%Y')
```

    2021-10-11 09:12:44.050877





    '10-11-2021'




```python
from pytz import timezone
record_dt = datetime.strptime('07/12/2016 04:39PM','%m/%d/%Y %H:%M%p')
ny_tz = timezone('US/Eastern')
la_tz = timezone('US/Pacific')
ny_dt = record_dt.replace(tzinfo = ny_tz)
la_dt = ny_dt.astimezone(la_tz)
print(ny_dt)
print(la_dt)
```

    2016-07-12 04:39:00-04:56
    2016-07-12 02:35:00-07:00



```python
from datetime import timedelta
record_dt = datetime.strptime('07/12/2016 04:39PM','%m/%d/%Y %H:%M%p')
flashback = timedelta(days = 90)
print(record_dt)
print(record_dt - flashback)
print(record_dt + flashback)
```

    2016-07-12 04:39:00
    2016-04-13 04:39:00
    2016-10-10 04:39:00



```python
%%capture
import sys
!conda install --yes --prefix {sys.prefix} pendulum
```


```python
# Import the pendulum module
import pendulum

# Create a now datetime for Tokyo: tokyo_dt
tokyo_dt = pendulum.now('Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
la_dt = tokyo_dt.in_timezone('America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())
```

    2021-10-11T09:55:26.861311-07:00



```python
# Iterate over date_ranges
date_ranges = [('01/30/2001', '03/01/2001'), ('03/31/2001', '04/30/2001'), ('05/30/2001', '06/29/2001')]
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt 
    start_dt = pendulum.parse(start_date, strict = False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict = False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())
```

    2001-03-01T00:00:00+00:00 2001-01-30T00:00:00+00:00
    30
    2001-04-30T00:00:00+00:00 2001-03-31T00:00:00+00:00
    30
    2001-06-29T00:00:00+00:00 2001-05-30T00:00:00+00:00
    30



```python

```

    0
    4
    1
    5
    2
    6

