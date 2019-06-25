import array as ar
from Utils.utils import prblm2 as UTIL

arr_1=ar.array('i',[1,2,3,4,5])
chk_val=input("enter the value to check for occurence :")
print("Value Occured :",UTIL.Count_occur_Array(arr_1,int(chk_val)))


