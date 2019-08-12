import pandas as pd
import numpy as np
amino_acids="ARNDCQEGHILKMFPSTWYV"
aa=list(amino_acids)
print(aa)
aa.append('cleav')
aa.append('Name')

cc=list(np.zeros(21))
cc.append('New Name')

bc=list(np.zeros(21))

data_val=pd.DataFrame(columns=aa)
data_val=data_val.append(pd.Series(cc,index=data_val.columns),ignore_index=True)
print(data_val)
data_val['Name']='New Name'
print(data_val)

file=open('/home/admin1/Desktop/sample datasets/classification/newHIV-1_data/746Data.txt')
file_val=file.read().splitlines()

print(len(bc))
for i in file_val:
    print(i)
    val_temp=i.split(',')
    cleav=val_temp[1]
    name=val_temp[0]
    data_val.loc[data_val['Name']=='New Name',bc]=name
    # amin=list(val_temp[0])
    # for j in amin:
    #     count_val=amin.count(j)
    #     # data_val[j]=count_val
    #  # print("amin :",val_temp[0].count(j),"count :",j)
    #
    # # data_val = data_val.append(pd.Series(cc, index=data_val.columns), ignore_index=True)


print(data_val)