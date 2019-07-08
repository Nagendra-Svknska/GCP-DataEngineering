import  random
import  plotly as pl
import  plotly.graph_objs as obj
import matplotlib.pyplot as plt

x_val=[random.randint for i in range(1000)]
y_val=[random.randint for i in range(1000)]
print(type(x_val))
d=obj.Scatter(x=x_val,y=y_val)
pl.offline.plot(d)

