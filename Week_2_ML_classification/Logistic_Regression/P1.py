import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn import metrics as mt

dataset=pd.read_csv("/home/admin1/Desktop/sample datasets/classification/Social_Network_Ads.csv")
x_val=dataset.iloc[:,2:4]
y_val=dataset.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.25,random_state=0)

sc_ler=StandardScaler()
x_train=sc_ler.fit_transform(x_train)
x_test=sc_ler.transform(x_test)

reg=LogisticRegression(random_state=0)
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)

cm=confusion_matrix(y_test,y_pred)
print(cm)

print("accuracy Score :",mt.accuracy_score(y_test,y_pred))
print("Precisiopn Score:",mt.precision_score(y_test,y_pred))

answer=reg.predict(sc_ler.transform([[37,77000]]))
print(answer)