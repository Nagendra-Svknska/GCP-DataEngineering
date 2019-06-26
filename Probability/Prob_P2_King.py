s=0
tries=0
for i in range(1,53):
  if(i<5):
     tries+=1
  if(i!=1):            # this condition is to remove king
      s+=1
print("total No of possible outcomes:",s," total no of valid outcomes:",tries)
print("probability :",tries/s)