import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from ipywidgets import interact, interactive, fixed, interact_manual
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

path2 = '/home/tbfk/Documents/VSC/Coursera/Data_Analysis_with_Python/'
path1 = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv'
fn = 'module_5_auto.csv'
df = pd.read_csv(path2 + fn)
df=df._get_numeric_data()
print(df.head(5))

#------------Functions for plotting
def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color="r", label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()

def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    
    
    #training data 
    #testing data 
    # lr:  linear regression object 
    #poly_transform:  polynomial transformation object 

    xmax=max([xtrain.values.max(), xtest.values.max()])

    xmin=min([xtrain.values.min(), xtest.values.min()])

    x=np.arange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    plt.close()

#----------Part 1: Training and Testing
# An important step in testing your model is to split your data into 
# training and testing data. We will place the target data price in a 
# separate dataframe y:
y_data = df['price']

# drop price data in x data
x_data=df.drop('price',axis=1)

# Now we randomly split our data into training and testing data 
# using the function train_test_split.
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)


print("number of test samples :", x_test.shape[0])
print("number of training samples:",x_train.shape[0])


lre=LinearRegression()
# we fit the model using the feature horsepower 
print(lre.fit(x_train[['horsepower']], y_train))

# Let's Calculate the R^2 on the test data:
print(lre.score(x_test[['horsepower']], y_test))

# R^2 on the training data
print(lre.score(x_train[['horsepower']], y_train))
# The R^2 is much smaller on the test data


#------------------Cross-validation Score
# We input the object, the feature in this case ' horsepower', the 
# target data (y_data). The parameter 'cv' determines the number 
# of folds; in this case 4.

Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)

print(Rcross)

# We can calculate the average and standard deviation of our estimate:
print("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())

# We can use negative squared error as a score by setting the parameter 
# 'scoring' metric to 'neg_mean_squared_error'. 
mse = -1 * cross_val_score(lre,x_data[['horsepower']], y_data,cv=4,scoring='neg_mean_squared_error')
print(mse)

# We input the object, the feature in this case 'horsepower' , the target 
# data y_data. The parameter 'cv' determines the number of folds; in 
# this case 4. We can produce an output for horsepower '0, 1, 2, 3, 4':
yhat = cross_val_predict(lre,x_data[['horsepower']], y_data,cv=4)
print(yhat[0:5])


#----------------Part 2: Overfitting, Underfitting and Model Selection
# Let's create Multiple linear regression objects and train the model 
# using 'horsepower', 'curb-weight', 'engine-size' and 'highway-mpg' 
# as features.
lr = LinearRegression()
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)

# Prediction using training data:
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
print(yhat_train[0:5])

# Prediction using test data:
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
print(yhat_test[0:5])

# Let's perform some model evaluation using our training and testing 
# data separately. Red = Actual Values, Blue = Predicted Values
Title = 'Distribution  Plot of  Predicted Value Using Training Data vs Training Data Distribution'
DistributionPlot(y_train, yhat_train, "Actual Values (Train)", "Predicted Values (Train)", Title)

# So far the model seems to be doing well in learning from the training 
# dataset. But what happens when the model encounters new data from the 
# testing dataset? When the model generates new values from the test 
# data, we see the distribution of the predicted values is much 
# different from the actual target values. 

Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",Title)

#--Overfitting 
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.45, random_state=0)

# We will perform a degree 5 polynomial transformation on the feature 'horse power'. 
pr = PolynomialFeatures(degree=5)
x_train_pr = pr.fit_transform(x_train[['horsepower']])
x_test_pr = pr.fit_transform(x_test[['horsepower']])
print(pr)

# Now let's create a linear regression model "poly" and train it.
poly = LinearRegression()
poly.fit(x_train_pr, y_train)

yhat = poly.predict(x_test_pr)
print(yhat[0:5])

# Let's take the first five predicted values and compare it to the actual targets.
print("Predicted values:", yhat[0:4])
print("True values:", y_test[0:4].values)

PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train, y_test, poly,pr)

print('R^2 training data:' ,poly.score(x_train_pr, y_train))
print('R^2 training data:' ,poly.score(x_test_pr, y_test))

# We see the R^2 for the training data is 0.5567 while the R^2 on 
# the test data was -29.87. The lower the R^2, the worse the model, 
# a Negative R^2 is a sign of overfitting.

# Let's see how the R^2 changes on the test data for different order 
# polynomials and plot the results:

Rsqu_test = []

order = [1, 2, 3, 4]
for n in order:
    pr = PolynomialFeatures(degree=n)
    
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    
    x_test_pr = pr.fit_transform(x_test[['horsepower']])    
    
    lr.fit(x_train_pr, y_train)
    
    Rsqu_test.append(lr.score(x_test_pr, y_test))

plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')
plt.text(3, 0.75, 'Maximum R^2 ')   
plt.show()
plt.close()

def f(order, test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_data, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_pr,y_train)
    PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train,y_test, poly, pr)

#only works in jupyter notebook
interact(f, order=(0, 6, 1), test_data=(0.05, 0.95, 0.05))


#----------------Part 3: Ridge regression
# In this section, we will review Ridge Regression we will see how 
# the parameter Alfa changes the model. Just a note here our test 
# data will be used as validation data.
pr=PolynomialFeatures(degree=2)
x_train_pr=pr.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr=pr.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

RigeModel=Ridge(alpha=0.1)

# Like regular regression, you can fit the model using the method fit.
RigeModel.fit(x_train_pr, y_train)

yhat = RigeModel.predict(x_test_pr)

# Let's compare the first five predicted samples to our test set 
print('predicted:', yhat[0:4])
print('test set :', y_test[0:4].values)

# We select the value of Alpha that minimizes the test error, 
# for example, we can use a for loop.

Rsqu_test = []
Rsqu_train = []
dummy1 = []
Alpha = 10 * np.array(range(0,1000))
for alpha in Alpha:
    RigeModel = Ridge(alpha=alpha) 
    RigeModel.fit(x_train_pr, y_train)
    Rsqu_test.append(RigeModel.score(x_test_pr, y_test))
    Rsqu_train.append(RigeModel.score(x_train_pr, y_train))

# We can plot out the value of R^2 for different Alphas 
width = 12
height = 10
plt.figure(figsize=(width, height))

plt.plot(Alpha,Rsqu_test, label='validation data  ')
plt.plot(Alpha,Rsqu_train, 'r', label='training Data ')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()
plt.close()


#----------------Part 4: Grid Search
# The term Alfa is a hyperparameter, sklearn has the class GridSearchCV 
# to make the process of finding the best hyperparameter simpler.

parameters1= [{'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000]}]
#parameters2= [{'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000], 'normalize':[True,False]}]
print(parameters1)

RR=Ridge()
print(RR)

Grid1 = GridSearchCV(RR, parameters1,cv=4)
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

# The object finds the best parameter values on the validation data. 
# We can obtain the estimator with the best parameters and assign it 
# to the variable BestRR as follows:

BestRR=Grid1.best_estimator_
print(BestRR)

# We now test our model on the test data 
BestRR.score(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test)