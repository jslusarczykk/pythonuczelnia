import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):
    x.append(n)

# create y values (example: y = x^2)
for n in x:
    y.append(n**2)

# display chart
plt.plot(x, y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Plot of Y = X^2')
plt.grid(True)
plt.show()