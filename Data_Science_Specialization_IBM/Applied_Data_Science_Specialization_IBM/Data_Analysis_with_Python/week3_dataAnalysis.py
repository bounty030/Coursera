import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np
import seaborn as sns
from scipy import stats


path2 = '/home/tbfk/Documents/VSC/Coursera/Data_Analysis_with_Python/'
fn = 'automobileEDA.csv'
df = pd.read_csv(path2 + fn)
print(df.head(10))

print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

"""
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.pyplot.ylim(0,)
plt.pyplot.show()
"""

print(df.head(10))

"""
sns.boxplot(x='body-style', y='price', data=df)
plt.pyplot.show()
"""

print(df['drive-wheels'].unique())
print(df['body-style'].unique())
group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = group_one.groupby(['drive-wheels', 'body-style'],as_index=False).mean()
grouped_pivot = df_group_one.pivot(index='drive-wheels', columns='body-style')
print(grouped_pivot)

group_two = df[['body-style', 'price']]
df_group_two = group_two.groupby(['body-style'], as_index=True).mean()
print(df_group_two)

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  

# Since the p-value is < 0.001, the correlation between wheel-base and 
# price is statistically significant, although the linear 
# relationship isn't extremely strong (~0.585)

#-------------ANOVA: Analysis of Variance

# f_val, p_val = stats.f_oneway(group_one.get_group('fwd')['price'], group_one.get_group('rwd')['price'], group_one.get_group('4wd')['price'])  
# print( "ANOVA results: F=", f_val, ", P =", p_val)
df_gptest = df[['body-style','price', 'drive-wheels']]
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])


f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
print( "ANOVA results: F=", f_val, ", P =", p_val)