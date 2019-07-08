s=0            #total no of ways possible
tries=0        #toal no of possible outcomes
for i in range(1,53):
 if(tries<4): #total no of aces =4
   tries+=1
 s+=1         #total no of cards 52

print("S:",s," tries:",tries)
print("Probabilit :", float(tries)/s) #probability= no of ways possible / total no of possible outcomes