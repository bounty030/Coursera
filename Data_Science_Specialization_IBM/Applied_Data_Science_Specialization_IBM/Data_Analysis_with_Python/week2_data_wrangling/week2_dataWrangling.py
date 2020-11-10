#What is the purpose of Data Wrangling?

#Data Wrangling is the process of converting data from the initial 
# format to a format that may be better for analysis.

import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np


path = '/home/tbfk/Documents/VSC/Coursera/Data_Analysis_with_Python/'
filename = 'imports-85.csv'
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(path + filename, names = headers)

print(df.head(10))

#--------------------Replace missing data
#replace missing data '?' to NaN
df.replace("?", np.nan, inplace = True)
print(df.head(5))

missing_data = df.isnull()
print(missing_data.head(5))

#count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

"""
Deal with missing data
How to deal with missing data?

    drop data
    a. drop the whole row
    b. drop the whole column
    replace data
    a. replace it by mean
    b. replace it by frequency
    c. replace it based on other functions
"""

#Calculate the average of the column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

#Replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

#Calculate the mean value for 'bore' column
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

#Replace NaN by mean value
df["bore"].replace(np.nan, avg_bore, inplace=True)

#To see which values are present in a particular column, we can 
# use the ".value_counts()" method:
print(df['num-of-doors'].value_counts())

#We can see that four doors are the most common type. We can also 
# use the ".idxmax()" method to calculate for us the most 
# common type automatically:
print(df['num-of-doors'].value_counts().idxmax())

df["num-of-doors"].replace(np.nan, 'four', inplace=True)


avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

#Finally, let's drop all rows that do not have price data:
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

print(df.head())


#--------------------Correct data format
#In Pandas, we use
#.dtype() to check the data type
#.astype() to change the data type
#in pandas type 'object' is a string
print(df.dtypes)

#Convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#--------------------Data Standardization
#Standardization is the process of transforming data into a 
# common format which allows the researcher to make the 
# meaningful comparison. E.g. converts miles to km

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-mpg'] = 235/df["city-mpg"]
df.rename(columns={"city-mpg" : 'city-L/100km'}, inplace=True)


#-------------------Data Normalization
# Normalization is the process of transforming values of several 
# variables into a similar range. Typical normalizations include 
# scaling the variable so the variable average is 0, scaling 
# the variable so the variance is 1, or scaling variable so 
# the variable values range from 0 to 1 

# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


#-----------------Binning
# Binning is a process of transforming continuous numerical 
# variables into discrete categorical 'bins', for grouped analysis. 

df["horsepower"]=df["horsepower"].astype(int, copy=True)
#plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
#plt.pyplot.figure()
"""
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.savefig( path + 'horsepower_hist', format='jpg')
"""

# Creating bins for horsepower
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)
group_names = ['Low', 'Medium', 'High']

# We apply the function "cut" the determine what each value 
# of "df['horsepower']" belongs to. 
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
print(df[['horsepower','horsepower-binned']].head(20))

print(df["horsepower-binned"].value_counts())

#plot distribution of each bin
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
#plt.pyplot.figure(2)
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.savefig( path + 'horsepower_bins', format='jpg')

#---------------------Indicator variable (or dummy variable)
#An indicator variable (or dummy variable) is a numerical 
# variable used to label categories. They are called 
# 'dummies' because the numbers themselves don't have inherent meaning. 
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
print(dummy_variable_1.head())


# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)