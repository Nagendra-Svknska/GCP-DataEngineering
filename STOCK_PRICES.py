import pandas as pd
import numpy as np
from sklearn import model_selection

dat_set=pd.read_csv('/home/admin1/Desktop/sample datasets/GOOGLE_CLOUD_TASK/Google_Stock_Price_Train.csv')
dat_set['Date'] = pd.to_datetime(dat_set.Date,format='%m/%d/%Y')
# print dat_set
x_val=dat_set.iloc[:,:1]
y_val=dat_set.iloc[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_val,y_val,test_size=0.25,random_state=0)
# print len(x_train)
# print len(y_train)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,y_train)

from sklearn.metrics import accuracy_score

ac_score=accuracy_score(y_test,reg.predict(x_test))
print(ac_score)