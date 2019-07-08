import seaborn as sb
import matplotlib.pyplot as plt

dat_val=sb.load_dataset('titanic')
set_v=set(dat_val['sex'])
print(type(dat_val))
# print(dat_val.info())
sb.barplot(x='sex',y='survived',hue='class',data=dat_val)



# sb.pointplot(x='sex',y='survived',hue='class',data=dat_val)
#
plt.show()

