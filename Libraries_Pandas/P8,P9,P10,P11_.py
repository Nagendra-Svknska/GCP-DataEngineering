import pandas as pd
import numpy as np

# prob 8
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

examData_dataFram=pd.DataFrame(exam_data,index=labels)
print("Prob 8:\n",examData_dataFram,"\n")

print(examData_dataFram[['name','score']])

print("===================================")
# prob 9
print("Prob 9: \n",examData_dataFram.iloc[[1,4],[2,3]])

print("===================================")
# prob 10
print("Prob 10: \n",examData_dataFram[examData_dataFram['attempts']>2])

# for i in examData_dataFram.values:
#     print(i[2])

print("===================================")
# Prob 11
print("Prob 11: \n")
print("Number of Rows :",len(examData_dataFram.axes[0]))

print("Number of Columns :",len(examData_dataFram.axes[1]))

