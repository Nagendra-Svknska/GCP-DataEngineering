import  pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics as mt


datSet=pd.read_csv('/home/admin1/Desktop/sample datasets/Position_Salaries.csv')
# print(datSet)
# print(len(datSet))


ct=ColumnTransformer([('one hot encoder',OneHotEncoder(),[0])],remainder='passthrough')
# print(type(ct.fit_transform(datSet)))
# print(ct.fit_transform(datSet).toarray())
x_val=ct.fit_transform(datSet).toarray()
print(x_val[:,:-2])
print(len(x_val[:,:-2]))
y_val=x_val[:,-1:]
print(y_val)

from sklearn.tree import  DecisionTreeRegressor,export_graphviz
reg=DecisionTreeRegressor(random_state=0)
reg.fit(x_val[:,:-2],y_val)

a=reg.predict([[0,0,1,0,0,0,0,0,0,0]])
print(a.shape)
accuracyScore=mt.accuracy_score(np.atleast_1d(1000000),np.atleast_1d(reg.predict([[0,0,1,0,0,0,0,0,0,0]])))
print(accuracyScore)

export_graphviz(reg,out_file='dectree.dot')



