# import pandas library

import pip
import pandas as pd
import numpy as np

print('pandas version: ', pd.__version__)
print('numpy version: ', np.__version__)

path = '/home/tbfk/Documents/VSC/Coursera/Data_Analysis_with_Python/imports-85.csv'
df = pd.read_csv(path, header=None)

#assign headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers


print(df.head(10))
print(df.tail(10))
print(df.columns)    #get column names
print(df.dtypes)     #get datatypes
print(df.describe()) #get statistics

print(df[['length', 'compression-ratio']].describe())
print(df.info())

"""
# create headers list

df.head(10)

df1=df.replace('?',np.NaN)

df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))
"""