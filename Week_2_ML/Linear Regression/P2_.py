import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split as train_test
from sklearn.linear_model import LinearRegression

fileval=pd.read_csv("/home/admin1/Desktop/sample datasets/bike_sharing.csv")

# print(fileval.head())                           #to find the info
# print(fileval.info())

# print(fileval['cnt'])                           #different type of slicing
# print(fileval['temp'])

# print(fileval.temp)
# print(fileval.cnt)

# print(fileval.iloc[:,-7])
# print(fileval.iloc[:,-1])



Temp_Train,Temp_test,Bik_train,Bik_test=train_test(fileval[['temp']],fileval[['cnt']].values,test_size=0.5)

from sklearn.preprocessing import StandardScaler
scaling=StandardScaler()
Temp_Train=scaling.fit_transform(Temp_Train)
Temp_test=scaling.fit_transform(Temp_test)

# print(Temp_test,"yes",Temp_Train)

reg=LinearRegression()
reg.fit(Temp_Train,Bik_train)
plt.plot(Temp_test,reg.predict(Temp_test),linewidth=1,color='cyan')
plt.scatter(x=Temp_test,y=Bik_test,s=50,facecolor='yellow',edgecolors='black')

import pickle
test_pick=open('test_pickle2.sav','wb')
pickle.dump(Temp_Train,test_pick)


plt.show()

