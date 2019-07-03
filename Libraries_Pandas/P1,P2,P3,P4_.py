import pandas as pd

# prob 1 -create one dimensional array
test1=pd.array([1,2,3,4],dtype=int)
print("prob1 :",test1)
print("===================================")

# prob 2-convert a pandas module series to list
test2_ser=pd.Series([2, 4, 6, 8, 10])
print("test2 :",test2_ser)
test2_list=test2_ser.tolist()
print("prob 2 :",test2_list)
print("===================================")


# prob 3 -add,subtract,multiply and divison of two arrays
test2_ser_cln=pd.Series([1, 3, 5, 7, 9])
print("Prob 3,clone test2 :",test2_ser_cln)


sum_val=test2_ser+test2_ser_cln
print("Prob 3,sum_val :",sum_val)

diff_val=test2_ser-test2_ser_cln
print("Prob 3,diff val:",diff_val)

mul_val=test2_ser*test2_ser_cln
print("Prob 3,mul val:",mul_val)

div_val=test2_ser/test2_ser_cln
print("Prob 3,divison val:",div_val)

print("===================================")


# prob 4 rise to power
test4=pd.array([0,1,2,3,4,56],dtype=int)

temp=test4**2
print("test 4 (power of 2 val)",temp)
