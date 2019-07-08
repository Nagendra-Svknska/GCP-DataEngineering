import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x,popularity,color=(0.4, 0.6, 0.8, 1.0),edgecolor='blue')
plt.show()

