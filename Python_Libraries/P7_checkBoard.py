import numpy as np

mat_val=np.zeros(64)
print(mat_val)

for i in range(64):
    if(i==0):
     mat_val[i]=0
    elif(i%2==0):
     mat_val[i]=0
    else:
     mat_val[i]=1
print(mat_val)

mat_val.reshape(8,8)