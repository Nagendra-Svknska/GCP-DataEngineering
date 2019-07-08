import pandas as pd
import seaborn as sb
import  matplotlib.pyplot as plt

box_val=pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
# print(box_val)

sb.boxplot(x='lifeExp',y='continent',data=box_val)
plt.show()
