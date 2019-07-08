import  seaborn as sb
import matplotlib.pyplot as plt

swarm_val=sb.load_dataset('tips')
print(swarm_val)

sb.swarmplot(x='total_bill',y='size',data=swarm_val,color='red')
plt.show()