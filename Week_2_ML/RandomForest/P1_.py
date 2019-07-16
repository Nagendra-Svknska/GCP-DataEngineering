import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

val=pd.read_csv('/home/admin1/Desktop/sample datasets/Position_Salaries.csv')
# print(val)
#
# print(type(val['Level']))
# print(type(val.Level))

x_vaal= np.array(val[['Level']].values ).reshape(len(val['Level']),1)
y_vaal= np.array(val[['Salary']].values).reshape(len(val['Salary']),1)
print((x_vaal).shape,y_vaal.shape,type(x_vaal))

# lvl_train,lvl_test,slry_train,slry_test=train_test_split(x_vaal,y_vaal,test_size=0.5)
# print(lvl_test.shape)

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=10,random_state=0)
reg.fit(x_vaal,y_vaal)

y_pred=reg.predict(np.atleast_2d(3))
print("value :",y_pred)
