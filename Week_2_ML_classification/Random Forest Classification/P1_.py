import  pandas as pd

dataset=pd.read_csv("/home/admin1/Desktop/sample datasets/classification/Social_Network_Ads.csv")
print(dataset.head())
x_val=dataset.iloc[:,2:4]
# print(x_val)
y_val=dataset.iloc[:,-1:]
# print(y_val)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.25,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifeir=RandomForestClassifier( n_estimators=100)
classifeir.fit(x_train,y_train)

y_pred=classifeir.predict(x_test)

from sklearn.metrics import confusion_matrix
from sklearn import metrics

print("Accuracy score :",metrics.accuracy_score(y_test,y_pred))
print("Precison Score:",metrics.precision_score(y_test,y_pred))
print("confisuion matrix :",confusion_matrix(y_test,y_pred))