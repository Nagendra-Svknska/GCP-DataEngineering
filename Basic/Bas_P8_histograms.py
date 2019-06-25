import matplotlib.pyplot as plt
from matplotlib import style
from Utils.utils import prblm2 as prb

style.use("ggplot")

# obj=Fnction_check_Datatype.prblm2()
values=input("enter x axis values sepearted by space")
list1=values.split()
print(list1)
list1=prb.find_datatype(list1) #to check values entered are int

values2=input("enter Y axis values seperated by space")
list2=values2.split()
list2=prb.find_datatype(list2) #to check values entered are int

style.use("ggplot")
#plt.plot(list1,list2)
plt.hist(list1,list2,rwidth=0.95)

plt.title("Info_Values")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.savefig('demo.png')
#plt.show()

