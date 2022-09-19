import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds , s=10)
ax.set_title('Cube table', fontsize=20)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Cube Value', fontsize=12)

ax.axis([0, 5100, 0, 125_000_000])
plt.show()