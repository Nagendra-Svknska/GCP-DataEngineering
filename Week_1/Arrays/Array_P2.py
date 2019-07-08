import array as ar
from Week_1.Utils.utils import prblm2 as UTIL

list=[]
a_array=ar.array('i',[1,2,3,4,5])
print(a_array)

UTIL.reverseArray(a_array)  #using custom made revers function

a=a_array[::-1]             #using slicing
print("reverse array value using slicing :",a)