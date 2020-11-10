import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#--------------------------pandas Basics
path = '/home/tbfk/Documents/VSC/Coursera/Applied_Data_Science_Specialization_IBM/Data_Visualization_with_Python/'
df_can = pd.read_csv(path + 'Canada.csv')
print(df_can.head(5))

# To get the list of column headers we can call upon the 
# dataframe's .columns parameter.
print(df_can.columns.values)

# Similarly, to get the list of indicies we use the .index parameter.
print(df_can.index.values)

# Let's clean the data set to remove a few unnecessary columns. 
# We can use pandas drop() method as follows:

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

# Let's rename the columns so that they make sense. 
# We can use rename() method by passing in a dictionary 
# of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

print(df_can.head(5))

# We will also add a 'Total' column that sums up the total 
# immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1)

# We can check to see how many null objects we have in the 
# dataset as follows:
print(df_can.isnull().sum())

print(df_can.describe())


#-------------------pandas Intermediate: Indexing and Selection (slicing)

# Select Column
print(df_can.Country)
print(df_can[['Country', '1980', '1981', '1982', '1983', '1984', '1985']])  # returns a series

# Select Row
"""
There are main 3 ways to select rows:

    df.loc[label]        
        #filters by the labels of the index/column
    df.iloc[index]       
        #filters by the positions of the index/column
"""

# Before we proceed, notice that the defaul index of the dataset is 
# a numeric range from 0 to 194. This makes it very difficult to 
# do a query by a specific country. For example to search for data 
# on Japan, we need to know the corressponding index value.

# This can be fixed very easily by setting the 'Country' column as 
# the index using set_index() method.

df_can.set_index('Country', inplace=True)
print(df_can.head(3))

# Let's view the number of immigrants from Japan (row 87) for the 
# following scenarios: 1. The full row data (all columns) 2. 
# For year 2013 3. For years 1980 to 1985
# 1. the full row data (all columns)
print(df_can.loc['Japan'])
# or with the index
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', '2013'])

# alternate method
#print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36 

# 3. for years 1980 to 1985
print(df_can.loc['Japan', ['1980', '1981', '1982', '1983', '1984', '1984']])
#print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])


# Convert all column names to strings
df_can.columns = list(map(str, df_can.columns))
[print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# Since we converted the years to string, let's declare a variable 
# that will allow us to easily call upon the full range of years:
years = list(map(str, range(1980, 2014)))
print(years)


#---------------------Filtering based on a criteria
# To filter the dataframe based on a condition, we simply pass 
# the condition as a boolean vector. 
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataFrame
print(df_can[condition])

# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia

condition2 = df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
print(condition2)
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses


#-------------------Visualizing Data using Matplotlib

#---Area Plots
# Visualize top 5 countries with an area plot
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

print(df_top5.head())

# Area plots are stacked by default. And to produce a stacked area 
# plot, each column must be either all positive or all negative 
# values (any NaN values will defaulted to 0). To produce an 
# unstacked plot, pass stacked=False. 

df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='area', 
             alpha=0.25, #transparency value, default is 0.5
             stacked=False,
             figsize=(20, 10), # pass a tuple (x, y) size
             )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()
plt.close()


#---Histograms
# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can['2013'])
print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins

# count, bin_edges = np.histogram(df_can['2013'], 20) #20 bins

df_can['2013'].plot(kind='hist', figsize=(8, 5))

plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()
plt.close()

# to match the x-axis with the bins we have to include 'xticks=bin_edges'
#df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)


#---Bar Charts
# step 1: get the data
df_iceland = df_can.loc['Iceland', years]
print(df_iceland.head())

df_iceland.plot(kind='bar', figsize=(10, 6), rot=90, color='r') 

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',                      # s: str. will leave it blank for no text
             xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis', # text to display
             xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
             rotation=72.5,                  # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )

plt.show()
plt.close()
