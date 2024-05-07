import matplotlib.pyplot as plt
import numpy as np

with open('measurments.csv') as f:
    d = f.read().split('\n')

time = float(d.pop(0))
measurments = np.array([int(x) for x in d], dtype = np.float64)
measurments *= 3.3/255 # Convert to volts

fig, ax = plt.subplots()

ax.plot(np.linspace(0, time, len(measurments)), measurments)
ax.set_title('Измерения')
ax.set_xlabel('t, с')
ax.set_ylabel('U, В')
ax.grid(True)

plt.show()