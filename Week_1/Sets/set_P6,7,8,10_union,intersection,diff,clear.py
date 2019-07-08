setTest=set((1,2,3,4,4,4,5,5,6))
setTest2=set((1,0,98,65,2))
print("intersection :",setTest.intersection(setTest2))   #6   #to find intersection of two sets
print("Union :",setTest.union(setTest2))                 #7   #to find union of two sets
print("Difference :",setTest-setTest2)                   #8    #to get difference of two sets
setTest.clear()                                          #10   # to clear the values from a set
print(setTest)