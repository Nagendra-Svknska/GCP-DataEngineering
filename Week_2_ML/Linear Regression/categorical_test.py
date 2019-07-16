import  pandas as pd
from sklearn.preprocessing import LabelEncoder
from  sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer
import numpy as np

from sklearn.linear_model import  LinearRegression

from sklearn import metrics as mt


cat_check=pd.read_csv("/home/admin1/Desktop/sample datasets/data_preprocessing.csv")
# print(cat_check.info())
# print(cat_check.head())

cat_check.Salary.fillna(cat_check.Salary.mean(),inplace=True)
cat_check.Age.fillna(cat_check.Age.mean(),inplace=True)
# print(cat_check)

cat_check.iloc[:,-1]=label_val=LabelEncoder().fit_transform(cat_check.iloc[:,-1])
# print(cat_check)


# a=pd.get_dummies(cat_check['Country'])           # dummy variable columns can be achived via theis aswell
# print(a)


ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)

x_k=np.array(ct.fit_transform(cat_check))
# print(x_k)
# print(x_k[:,0:3])
# print(x_k[:,4])
#
reg=LinearRegression()
reg.fit(x_k[:,0:4],x_k[:,4])
pred_sal=(reg.predict([[1,0,0,44]]))
print("predicted value",pred_sal)
# print(pred_sal.shape,pred_sal,type(pred_sal))

pred_sal=pred_sal.round()
print(pred_sal)
original_sal=np.atleast_1d(7200)
print(len(pred_sal))
print(original_sal.shape,original_sal,type(original_sal))
print(original_sal)
print(mt.accuracy_score(original_sal,pred_sal))
print("pred_sal:",pred_sal,"original_sal :",original_sal)
accuracyScore=mt.accuracy_score(original_sal,pred_sal)

print(accuracyScore)
# print(accuracyScore)

