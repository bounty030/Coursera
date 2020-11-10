import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

path2 = '/home/tbfk/Documents/VSC/Coursera/Data_Analysis_with_Python/'
fn = 'automobileEDA.csv'
df = pd.read_csv(path2 + fn)
print(df.head(5))

# Model 1: Simple Linear Regression
lm = LinearRegression()
print(lm)

X = df[['highway-mpg']]
Y = df[['price']]

lm.fit(X, Y)

Yhat = lm.predict(X)
print(Yhat[0:5])

print('Interceptor: ', lm.intercept_)
print('Coefficient: ', lm.coef_)

# Model 2: Multiple Linear Regression
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])

Y_hat = lm.predict(Z)

width = 12
height = 10
"""
plt.pyplot.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.pyplot.title('Actual vs Fitted Values for Price')
plt.pyplot.xlabel('Price (in dollars)')
plt.pyplot.ylabel('Proportion of Cars')

plt.pyplot.show()
plt.pyplot.close()

"""

# Model 3: Polynomial Fit

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.pyplot.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.pyplot.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.pyplot.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.pyplot.gcf()
    plt.pyplot.xlabel(Name)
    plt.pyplot.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']
# Here we use a polynomial of the 3rd order (cubic) 
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

#PlotPolly(p, x, y, 'highway-mpg')

#-----------------------Pipeline
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
print(pipe)
print(pipe.fit(Z,df['price']))
ypipe = pipe.predict(Z)
print(ypipe[0:4])


#--------------------Measures for In-Sample Evaluation
#---------Model 1: Simple Linear Regression
lm.fit(X, Y)
print('The R-square is: ', lm.score(df[['highway-mpg']], df[['price']]))

Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)

#--------Model 2: Multiple Linear Regression
# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))

Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit))

#--------Model 3: Polynomial Fit
r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)

