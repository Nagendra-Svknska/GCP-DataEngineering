import pandas as pd
import numpy as np
import  seaborn as sbr
import sklearn.impute
import sklearn.impute
from sklearn.impute import SimpleImputer

dataval=pd.read_csv('/home/admin1/Desktop/sample datasets/data_preprocessing.csv')
# dataval=sbr.re('/home/admin1/Desktop/sample datasets/data_preprocessing.csv')
# print(dataval)
# print(type(dataval))
# dataval[]
a=dataval[:,:-1]
print(dataval[:,:-1])
#
b=dataval[:,3]
# print(b)
print(type(a))
print(a.info())
print("a val:",a)
# k=a.iloc[:,1:2]
# print(k)
#
#
# imputer=SimpleImputer(missing_values='NaN',strategy='mean')
# imputer=imputer.fit(a.iloc[:,1:3])
# a=imputer.transform(a.iloc[:,1:3])
#
# print("a :",a)




