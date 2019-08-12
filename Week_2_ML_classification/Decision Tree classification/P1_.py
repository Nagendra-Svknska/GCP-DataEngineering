import  pandas as pd

dataset=pd.read_csv("/home/admin1/Desktop/sample datasets/classification/Social_Network_Ads.csv")
print(dataset.head())
x_val=dataset.iloc[:,2:4]
# print(x_val)
y_val=dataset.iloc[:,-1]
print(type(y_val))

from sklearn.model_selection  import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.25,random_state=0)
print(type(x_train),y_train)

from sklearn.tree import DecisionTreeClassifier
classfier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classfier.fit(x_train,y_train)
y_pred=classfier.predict(x_test)

from sklearn import metrics
from sklearn.metrics import confusion_matrix

print("Confision Matrix :",confusion_matrix(y_test,y_pred))
print("accuracy Score :",metrics.accuracy_score(y_test,y_pred))
print("precision Score",metrics.precision_score(y_test,y_pred))
