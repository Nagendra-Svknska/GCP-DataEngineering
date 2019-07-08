import matplotlib.pyplot as plt
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.pie(popuratity,explode=(0.1,0.1,0,0,0,0.1),labels=languages)
plt.title("Popularity of programming languages")
plt.show()