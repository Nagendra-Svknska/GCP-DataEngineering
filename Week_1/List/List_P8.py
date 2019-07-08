str_input=str(input("enter the string values seperated by space :"))
list_val=str_input.split()
int_Var=int(input("enter a value of n:"))
list_fin=[];
for i in list_val:
    if(len(list(i))>int_Var):
        list_fin.append(i)
    # if(len(i.split())>int_Var):
print(list_fin)
