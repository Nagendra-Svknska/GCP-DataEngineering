import numpy as np
import array as arr

# Prob 1- conversion of list of numeric values to array
list_val=[1.7,2.9,33,46]
matVal=arr.array('f',list_val)
matVal_num=np.array(list_val)
print("array :",matVal)
print("Numpy :",matVal_num)

# prob 2
mat1=np.arange(1,10).reshape(3,3)
print("Prob 2 :",mat1)

# prob 3
mat2=np.zeros(10)
 # print(mat2)
mat2[6]=11
print("Prob 3:",mat2)

# prob 4
mat2=mat2[::-1]
print("Prob 4 :",mat2)


# prob 5
row=int(input("enter the row value"))
col=int(input("enter the column value"))
mulList=np.ones(row*col)
# print("mullist 1",mulList)
mulList=np.reshape(mulList,(row,col))

print("mulList 2 before change",mulList)
mulList[1:-1,1:-1]=0
print("Prob 5:",mulList)


# not working (logic not correct)
# abc=[[0 if col >0 and row<4  else 1 for col in range(5) ]for row in range(5) ]
# print(np.array(abc))





