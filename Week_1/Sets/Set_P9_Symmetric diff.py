n_Set=set((1,2,3,4))
setTest=set((7,9,0,2,3))
print(n_Set,setTest)
res=n_Set.symmetric_difference(setTest)           #returns symmetric difference set
print("symmetric Diff",res)
n_Set.symmetric_difference_update(setTest)        # updates set on which symmetric diff is applies and return value as null
print("Symmetric diff Update",n_Set)
