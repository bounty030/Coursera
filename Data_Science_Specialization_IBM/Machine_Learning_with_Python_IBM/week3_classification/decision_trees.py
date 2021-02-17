import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

path = "/home/tbfk/Documents/VSC/Coursera/Applied_Data_Science_Specialization_IBM/Machine_Learning_with_Python/"
df = pd.read_csv(path + "drug200.csv")

print(df.head())
print(df.size)
print(df.tail())
print(df.info)
print(df.describe())

# Preprocessing
# Remove the target variable 'Drug'
X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values #returns an array

# Prepare the X value by transforming labels to numbers
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1]) 

le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3]) 

print(X[0:5])

# Select the target variable
y = df["Drug"]
print(y[0:5])

# Setting up the Decision Tree
# Split dataset in train and test set
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

# Modeling

drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
print(drugTree) # it shows the default parameters

# Fit model
drugTree.fit(X_trainset,y_trainset)

# Predict 
predTree = drugTree.predict(X_testset)
print(predTree[0:5])
print(y_testset[0:5])

# Model Evaluation
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

for row in df.iterrows():
    print(row)