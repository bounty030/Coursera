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

# Plotting in pandas is as simple as appending a .plot() method 
# to a series or dataframe.

#---Line Pots (Series/Dataframe)

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
# Since the x-axis (years) is type 'integer', we specified x as a year. 
# The y axis (number of immigrants) is type 'integer', so we can just 
# specify the value y = 6000.

plt.show() # need this line to show the updates made to the figure
plt.close()


# plot china and india
df_CI = df_can.loc[['China', 'India'], years]
print(df_CI.head(10))

df_CI.plot(kind='line')
plt.show()
plt.close()

# This does not look right because rows and columns are swaped
# So we need to swap rows with columns 
df_CI = df_CI.transpose()
print(df_CI.head())
df_CI.plot(kind='line')
plt.title('Immigration from China and India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
plt.close()

# we did not have to transpose haiti because it is a series and not a
# dataframe


#---------Compare the trend of top 5 countries that contributed the 
# most to immigration to Canada.
# Get the top 5 countries
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)
print(df_top5)
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line')
plt.title('Immigration of top5  Countries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
plt.close()