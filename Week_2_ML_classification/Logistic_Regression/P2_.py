import pandas as pd
import numpy as np
amino_acids="ARNDCQEGHILKMFPSTWYV"
valid_columns=list(amino_acids)
# print(valid_columns)
valid_columns.append('cleav')
valid_columns.append('Name')

row_insert=list(np.zeros(21))
row_insert.append('New Name')

data_val=pd.DataFrame(data=valid_columns, index=row_insert)
data_val=pd.DataFrame(columns=valid_columns)
colum_list=list(data_val.columns)
# print(colum_list)
colum_list=colum_list[:-2]
# print(colum_list)
data_val=data_val.append(pd.Series(row_insert, index=data_val.columns), ignore_index=True)
# print(data_val)
file=open('/home/admin1/Desktop/sample datasets/classification/newHIV-1_data/746Data.txt')
file_val=file.read().splitlines()
# print(len(file_val))
for i in file_val:

    val_temp=i.split(',')
    cleav=int(val_temp[1])
    name=val_temp[0]
    data_val.loc[data_val['Name']=='New Name',colum_list]=0
    data_val.loc[data_val['Name']=='New Name', ['Name','cleav']] =name,cleav
    amin=list(val_temp[0])

    for j in amin:
        count_val=amin.count(j)
        data_val.loc[data_val['Name'] == name, [j]] = count_val
    data_val = data_val.append(pd.Series(row_insert, index=data_val.columns), ignore_index=True)

# print(data_val)

x_val=data_val.iloc[:,:-2]
y_val=data_val.iloc[:,-2:-1]

# print("x_val shape :",x_val.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.25,random_state=0)

print(type(y_train.values),y_train.size,y_train.shape)
# print(y_train)
from sklearn.linear_model import LogisticRegression
reg=LogisticRegression(random_state=0)
reg.fit(x_train,y_train.values)
y_pred=reg.predict(x_test)

from sklearn import metrics
from sklearn.metrics import confusion_matrix
metrics.accuracy_score(y_test,y_pred)
# print(reg.predict([[1,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,2]]))
# print(reg.predict([[4,0,0,0,0,0,0,0,0,1,0,0,1,0,0,2,0,0,0,0]]))
cm=confusion_matrix(y_test,y_pred)
print(cm)

print("accuracy Score:",metrics.accuracy_score(y_test,y_pred))
print("Precision Score :",metrics.precision_score(y_test,y_pred))
# print(y_val)
