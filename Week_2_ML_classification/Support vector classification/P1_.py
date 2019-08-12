import  pandas as pd
import numpy as np

dataset=pd.read_csv("/home/admin1/Desktop/sample datasets/Position_Salaries.csv")
# print(dataset.head())

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer([('onehotencoder',OneHotEncoder(),[0])],remainder='passthrough')
dataset=ct.fit_transform(dataset).toarray()
# x_val=dataset.iloc[:,:-2]
x_val=np.array(dataset[:,:-2])
y_val=np.array(dataset[:,-1])
# print(y_val)
#
# print(y_val)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_val,y_val)
# print(type(y_test),y_val.shape,y_train.size)
# print(y_train)
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(x_train,y_train)

nn=classifier.predict([[1,0,0,0,0,0,0,0,0,0]])
print(nn)

from sklearn.metrics import confusion_matrix
from sklearn import metrics


print("confusion matrix :",confusion_matrix(y_test,classifier.predict(x_test)))
print("accuracy score :",metrics.accuracy_score(y_test,classifier.predict(x_test)))
# print("Precision score :",metrics.precision_score(y_test,classifier.predict(x_test)))


