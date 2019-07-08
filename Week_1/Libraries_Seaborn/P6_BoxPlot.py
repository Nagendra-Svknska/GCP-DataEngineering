import seaborn as sb
import matplotlib.pyplot as plt

testBox=sb.load_dataset('tips')
print(testBox)
# sb.boxplot(x='day',y='tip',data=testBox)
sb.boxplot(x='tip',y='day',data=testBox)
plt.show()