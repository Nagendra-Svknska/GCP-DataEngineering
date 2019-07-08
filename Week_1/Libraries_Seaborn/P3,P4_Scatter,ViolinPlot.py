import seaborn as sb
import  matplotlib.pyplot as plt

scatter_dataset=sb.load_dataset('tips')
print(scatter_dataset)

# Prob 3
sb.scatterplot(x='day',y='total_bill',hue='sex',data=scatter_dataset)


# Prob 4
# sb.violinplot(x='day',y='total_bill',hue='sex',data=scatter_dataset)


plt.show()