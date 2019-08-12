import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


data_val=pd.read_csv('/home/admin1/Desktop/sample datasets/GOOGLE_CLOUD_TASK/Google_Stock_Price_Train.csv')

# print(abc.iloc[:3,:])
# val= data_val.iloc[:3, :-1]
# print(val)
# date= data_val.iloc[:, :1]
# print(date)

# print(abc.Date)

data_val['Date'] = pd.to_datetime(data_val.Date,format='%m/%d/%Y')
# print(type(abc.values))
# print (type(abc['Date']))


x_val=np.array(data_val['Date']).reshape(len(data_val['Date']),1)
x_val=np.array(data_val.iloc[:, 1:])
# print(abc)
y_val=data_val.iloc[:, 2:4]
y_val[y_val<0]=0
y_val=np.array(y_val)

# print(y_val):Q
# .reshape(np.size(abc['Date']),1)






x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.5,random_state=0)

# print(np.shape(x_train))
# print(np.shape(y_train))

reg=LinearRegression()


print ("x_train",x_train)
print ("y_train",y_train)
print (type(y_train))

reg.fit(x_train,y_train)
print(reg.score(x_test,reg.predict(x_test)))

