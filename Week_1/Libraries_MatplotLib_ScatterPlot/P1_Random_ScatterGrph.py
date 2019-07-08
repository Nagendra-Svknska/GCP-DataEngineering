import matplotlib.pyplot as plt
import random
x=[random.random() for i in range(25)]
y=[random.gauss(0.5,0.76) for i in range(25)]
plt.scatter(x,y,s=90,facecolor='  ',edgecolors='blue')
plt.show()

print()
