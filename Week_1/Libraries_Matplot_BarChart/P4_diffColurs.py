import matplotlib.pyplot as plt

lang=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popul=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(lang,popul,color=['red','black','blue','yellow','violet','green'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.show()