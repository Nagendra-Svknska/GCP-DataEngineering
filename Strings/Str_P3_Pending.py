import string
str_val=str(input("enter the value of string :"))
str_li=list(str_val)
print(str_li)

for i in range(len(str_li)):
   if i<1:
    temp_replace=str_li[0]
   elif(str_li[i]==temp_replace):
    str_li[i]="$"


# print(string.join(str_li,''))
print(''.join(str_li))
