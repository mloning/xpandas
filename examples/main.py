import sys
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import pandas as pd

sys.path.insert(0, '..')

# Read a TimeSeries from URL
url = urlopen("http://timeseriesclassification.com/Downloads/FordA.zip")
zipfile = ZipFile(BytesIO(url.read()))
lines = zipfile.open('FordA/FordA.csv').readlines()
lines = [l.decode('utf-8') for l in lines]
lines = lines[505:]
# lines now is a list of strings with of timeseries in comma separeted format
# 505 is a offset for the beginning of seriases

lines = [list(map(float, l.split(','))) for l in lines]

# now let's create a list of pd.Series
lines = [pd.Series(l) for l in lines]

# create a MultiSeries series of pd.Series objects
X = MultiSeries(lines)

# windows_transformed_data =
