import pandas as pd

dataval=pd.read_csv('/home/admin1/Desktop/sample datasets/data_preprocessing.csv')
print("Before :",dataval)
# dataval.dropna(axis=1,inplace=True)
dataval.Salary.fillna(dataval.Salary.mean(),inplace=True)
# dataval.dropna(subset=['Age','Salary'],inplace=True)

# o=dataval.Country.str.upper()
# print(o)
print("after :",dataval)
