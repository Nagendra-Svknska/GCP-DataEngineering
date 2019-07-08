tup=(1,2,3,4,5,6)
val=int(input("enter a value to be removed :"))
if(val in tup):

    li=list(tup)
    li.remove(val)
    tup=tuple(li)
    print(tup)



