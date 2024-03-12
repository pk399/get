import matplotlib.pyplot as plt

x = [0, 5, 32, 64, 69, 127, 255] # numero
y = [0.05, 0.11, 0.46, 0.87, 0.93, 1.68, 3.24] # напряжение

plt.plot(x, y, 'b')
plt.plot(x, y, '*k')

plt.show()