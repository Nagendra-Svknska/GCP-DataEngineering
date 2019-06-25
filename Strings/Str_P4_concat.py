str_val=str(input("enter the value :"))
print(len(str_val))
if(int(len(str_val))>=3):
    #print("last 3",str_val[-3:])
    #print("except last 3",str_val[:-3])
    if(str_val[-3:]=="ing"):
        str_val=str_val[:-3]+"ly"
    else:
        str_val=str_val[:-3]+"ing"
    print(str_val)
else:
    print("not applicable")