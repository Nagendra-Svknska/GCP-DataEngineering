import seaborn as sb
import matplotlib.pyplot as plt

iris_val=sb.load_dataset('iris')
print(iris_val)
sb.violinplot(x='species',y='sepal_length',data=iris_val)
plt.show()