import pandas as pd
import  numpy as np



datval=pd.read_csv('/home/admin1/Desktop/sample datasets/bike_sharing.csv')
# print(datval.head())

x_val=datval.iloc[:,2:-1]
# print(x_val)

y_val=datval.iloc[:,-1:]
# print(y_val)

# y_val=np.array(y_val).reshape(len(y_val),1)
# x_val=np.array(x_val).reshape(len(x_val),1)

print(type(x_val),"space",type(y_val))
from sklearn.preprocessing import  StandardScaler
scale=StandardScaler()
scale.fit_transform(x_val)
# print(x_val)

# from sklearn.ensemble import RandomForestRegressor
# reg=RandomForestRegressor(random_state=0,n_estimators=10)
# reg.fit(x_val,y_val)
#
# print("nnn",reg.predict([[1,0,1,0,0,6,0,1,0.24,0.2879,0.81,0,3,13]]))

from sklearn.svm import SVR
test=SVR(kernel='rbf')
test.fit(x_val,y_val)
print("sdfg")
print("Predicted value:",test.predict([[1,0,1,0,0,6,0,1,0.24,0.2879,0.81,0,3,13]]))


