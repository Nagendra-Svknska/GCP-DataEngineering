list_a=[1,2,3,4,5,6,7,1,2]
print(list_a)
sett=set(list_a)  # since set does not allow duplicates
#print(sett)
print("List after removing Duplicates :",list(sett))

#problem 7 of copy
list2=list(list_a)
list3=list_a
#list2=list_a.copy()
print(list2)
print(list3)