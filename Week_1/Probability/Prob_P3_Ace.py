s=0
tries=0
for i in range(0,52):
    if(i<3):
     tries+=1
    if(i!=1):
     s+=1
print("total no of possible outcomes:",s,"total no of fav outcomes:",tries)
print("probability :",tries/s)
