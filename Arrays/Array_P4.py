import array as ar
from Utils.utils import prblm2 as UTIL

arr_val=ar.array('i',[1,2,3,4,5,5,6])
chk_val=input("enter value to be removed :")
arr_val=UTIL.remov_first_occ_array(arr_val,int(chk_val))
print(arr_val)