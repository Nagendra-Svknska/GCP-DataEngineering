from Utils.utils import prblm2 as UTILS

tup=(1,2,2,2,3,3,4,3,7,7,9,0,8,1)
print(UTILS.repeated_items_Tup(tup))  #using custom method


#using count function
list_val=[]
for i in tup:
 if(tup.count(i)>int(1)):
  if(i not in list_val):
   list_val.append(i)
 else: pass
print(list_val)