list_temp=['1ff','2uyt','3','4','5','9','8','10','66']
del list_temp[1]
print(list_temp.pop(1))
print(list_temp)

list_temp1=[1,2,3,4,5,6,7,8,9,10]
if(len(list_temp1)>int(5)):
     list_temp1.pop(0)
     list_temp1.pop(4)
     list_temp1.pop(5)
     print(list_temp1)