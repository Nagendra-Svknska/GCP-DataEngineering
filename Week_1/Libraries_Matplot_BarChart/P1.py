import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popul=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
# x_pos = [i for i, _ in enumerate(lang)]       #did not understand the use of X_pos
plt.bar(lang,popul)
# plt.bar(x_pos,popul)


plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.show()