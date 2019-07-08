str_input=input("enter the values seperated by space for List1 :")
list_val=str_input.split()


str_input2=input("enter the values seperated by space for List2 :")
list_val2=str_input.split()

for i in list_val:
   if(i in list_val2):
      print("true")
      break
if(len(list_val)>int(5)):
     list_val.pop(0)
     list_val.pop(4)
     list_val.pop(5)
     print(list_val)