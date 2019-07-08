d={}
st=str(input("enter the value of the string :"))
l=list(st)
for i in range(len(l)-1):
    #print("char :",l[i]," count :",st.count(l[i]))
    d.update({l[i]:st.count(l[i])})
print(d)                            #dictionary does not allow duplicate keys
