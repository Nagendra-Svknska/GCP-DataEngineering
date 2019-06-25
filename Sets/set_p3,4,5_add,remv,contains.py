setTest=set((1,2,3,4,4,4,5,5,6))
setTest.add(77)   #add method #only one element can be added via this method
print(setTest)
setTest.remove(2) #remove method
print("after removal 1 :",setTest)

#to check  aparticluar item is present in a set
if(1 in setTest):
    setTest.remove(4)
    print("after removal 2 :",setTest)