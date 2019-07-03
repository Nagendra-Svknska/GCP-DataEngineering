import matplotlib.pyplot as plt
f=open("/home/admin1/Desktop/Python_MatplotLib/Multiple Line data")
read_list=f.read().splitlines()
print(read_list)
date=[row.split(',')[0] for row in read_list]
open=[row.split(',')[1] for row in read_list]
high=[row.split(',')[2] for row in read_list]
low=[row.split(',')[3] for row in read_list]
close=x=[row.split(',')[4] for row in read_list]
print(date," ",open," ",high," ",low," ",close)


plt.plot(date,open,color='black',linewidth=2,linestyle='dashed')
plt.plot(date,high,color='green',linewidth=4)
plt.plot(date,low,color='red',linewidth=1.5)
plt.plot(date,close,color='yellow',linewidth=0.5)
plt.gca().legend(('Open','High','Low','Close'))

plt.xlabel("Date")
plt.ylabel("Y-axis")
plt.show()

# limitations its taking all the y values instead of values divided between the interval
