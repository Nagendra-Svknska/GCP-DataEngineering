from Week_1.Utils.utils import prblm2 as prbl
# def find_datatype(abc) :
#         list2 = ([])
#         print(abc)
#         for i in abc :
#             try:
#                 list2.append(int(i))
#             except:
#                 pass
#         return list2

values=input("enter values seperated by comma :")
list=values.split(',')
list2=prbl.find_datatype(list)
print("list value",list2)
print("tupple Value :", tuple(list2))