from asyncore import file_dispatcher

import  matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np




file_val=pd.read_csv("/home/admin1/Desktop/sample datasets/Salary_Data.csv")
print(type(file_val['YearsExperience']))
# print(file_val)
exp_val=np.array(file_val['YearsExperience'])
sal_val=np.array(file_val['Salary'])

print("len val :",len(exp_val))

exp_val=exp_val.reshape(len(exp_val),1)
sal_val=sal_val.reshape(len(sal_val),1)


expval_test=exp_val[:15]
sal_val_test=sal_val[:15]

expval_train=exp_val[15:]
sal_val_train=sal_val[15:]


# creating model
reg=LinearRegression()

# train the model
reg.fit(expval_train,sal_val_train)


plt.scatter(x=expval_train,y=sal_val_train)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("predicting salary")
plt.plot(expval_train,reg.predict(expval_train),linewidth=3,color='red')
plt.show()




