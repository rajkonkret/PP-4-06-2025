import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

plt.plot(x, y, color="red")
plt.title("Wykres 1")
plt.ylabel("X")
plt.xlabel("Y")

plt.savefig("wykres.png")
plt.show()
