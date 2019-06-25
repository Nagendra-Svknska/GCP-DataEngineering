tup=(1,2,3,4,5,6,7)
n_val=input("enter value to be checked")
if int(n_val) in tup:
    print("yes")
else:
    print("false")

#problem 7 conversion of list to tuple
li=[1,2,3,4,5,6,7]
t=tuple(li)
print(t)