import numpy as np
x_val = [[12,7,3],
[4 ,5,6],
[7 ,8,9],
[0 ,1,1]]

y_val = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

print("x matrix row length :",len(x_val)," Column legth",len(x_val[0]))
print("y matrix row length :",len(y_val),"Column legth",len(y_val[0]))

if(len(x_val[0])==len(y_val)):
    print("valid multiplication")
else:
    print("invalid multiplication")

A_val=np.array([[1,2,3],[4,5,6]])
B_val=np.array([[1,2],[3,5],[6,7]])
C_val=A_val.dot(B_val)
print(C_val)


# res1=[[x_val[i][j] for j in range(len(x_val[i]))]for i in range(len(x_val))]
# print(res1)
#
# res2=[[y_val[i][j]for j in range(len(y_val[i]))]for i in range(len(y_val))]
# print(res2)
#
# res=[[x_val[i][j]*y_val[i][j] for j in range(len(x_val[i]))]for i in range(len(x_val))]
# print(res)
