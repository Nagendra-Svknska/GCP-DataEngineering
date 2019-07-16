import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


file_val=pd.read_csv("/home/admin1/Desktop/sample datasets/Salary_Data.csv")
# print(type(file_val))
# # print(file_val.YearsExperience)
# # print(file_val.Salary)
x_val=np.array(file_val["YearsExperience"]).reshape(len(file_val["YearsExperience"]),1)
y_val=np.array(file_val["Salary"]).reshape(len(file_val["Salary"]),1)
print(len(x_val))


# expval_train=x_val[:15]
# salval_train=y_val[:15]
#
# expval_test=x_val[15:]
# salval_test=y_val[15:]

expval_train,expval_test,salval_train,salval_test=train_test_split(x_val,y_val,test_size=0.4)

# print("x:",x_val)
# print("y:",y_val)



# creating a model
reg=LinearRegression()

# training the model
reg.fit(expval_train,salval_train)
reg.score(salval_test,reg.predict(expval_test))


plt.scatter(x=expval_test,y=salval_test,s=90,facecolor='cyan',edgecolor='black')
plt.plot(expval_test,reg.predict(expval_test),linewidth=3,color='red')






plt.show()

