def cust_fn(list_val):
    count=0;
    for i in list_val:
        if(len(i)>2):
           tempList=list(i)
           print(tempList)
           if(tempList[0]==tempList[len(tempList)-1]):
            count=count+1


    return count


stry=input("enter the string values with space in between")
lis=stry.split()
count=cust_fn(lis)
print(count)
