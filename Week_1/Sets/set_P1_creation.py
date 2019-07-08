setTest=set()

set_Str=input("enter SET values with a space in between")
set_List=set_Str.split()
for i in set_List:
  setTest.add(i)

print("Set is :",setTest)