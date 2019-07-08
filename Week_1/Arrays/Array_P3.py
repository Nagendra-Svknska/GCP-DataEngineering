import array as ar
from Week_1.Utils.utils import prblm2 as UTIL

arr_1=ar.array('i',[1,2,3,4,5,5,5,5])
chk_val=input("enter the value to check for occurence :")
print("Value Occured :",UTIL.Count_occur_Array(arr_1,int(chk_val)))

# using count

print("Value Occured :",arr_1.count(int(chk_val)))

