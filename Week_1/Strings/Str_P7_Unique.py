str_val=str(input("enter the values comma sepearted :"))
li=str_val.split(',')
print(li)
li_val=[]
for i in li:
    #print("i :",i," count :",li.count(i))
    if(int(li.count(i))==1):
        if(i not in li_val):
         li_val.append(i)
print(li_val)
