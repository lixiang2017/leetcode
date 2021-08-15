



import matplotlib.pyplot as plt

data = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
x, y = [], []
for point in data:
	x.append(point[0])
	y.append(point[1])

plt.figure(figsize=(10, 10), dpi=100)
plt.scatter(x, y)
plt.show()