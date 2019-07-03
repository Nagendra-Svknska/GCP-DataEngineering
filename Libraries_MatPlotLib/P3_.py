import matplotlib.pyplot as plt

f=open("/home/admin1/Desktop/Python_MatplotLib/Python_TestDoc")
read_List=f.read()
read_List=read_List.splitlines()
print(read_List)
x=[row.split(' ')[0] for row in read_List]
y=[row.split(' ')[1] for row in read_List]
print(x,"  ",y)
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Test_Plot")
plt.show()



