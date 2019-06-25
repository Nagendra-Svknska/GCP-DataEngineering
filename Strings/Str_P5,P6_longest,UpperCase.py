str_val=str(input("enter the value with space in between:"))
li=str_val.split()
temp_val=0;
for i in li:
    if(len(i)>temp_val):
        temp_val=len(i)
print(temp_val)

#problem 6 -to upper and lower case
upper_case=str_val.upper()
print(upper_case)

lower_case=upper_case.lower()
print(lower_case)