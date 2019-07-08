f=open("/home/admin1/Desktop/Python_TestDoc")
read_List=f.read()
read_List=read_List.splitlines()
print(read_List)
x=[row.split(' ')[0] for row in read_List]
y=[row.split(' ')[1] for row in read_List]
print(x,"  ",y)