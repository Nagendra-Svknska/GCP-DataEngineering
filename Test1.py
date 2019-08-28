f=open('/home/admin1/Desktop/Sony Service Centre')
read_List=f.read()
read_List=read_List.splitlines()
print(read_List)
count=0
for i in range(len(read_List)):
    count=count+1
print(count)