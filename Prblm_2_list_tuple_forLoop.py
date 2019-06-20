def find_datatype(abc) :
    list=abc
    list2 = ([])
    print(list)
    for i in list :

        try:
            int(i)
            #list2=([])
            list2.append(i)
        except:
           pass

    print("tupple Value :",tuple(list2))
    return list2

values=input("enter values seperated by comma :")
list=values.split(',')
list2=find_datatype(list)
print("list value",list2)