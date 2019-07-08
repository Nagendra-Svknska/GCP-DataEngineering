import random
import matplotlib.pyplot as plt
import math

x=[random.triangular() for i in range(25)]
y=[random.random() for i in range(25)]

#  for prob 3
areas=[math.pi*random.randint(1,10)**2 for i in range(25)]

plt.scatter(x,y,s=areas,facecolors='none',edgecolors='green')

# plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()