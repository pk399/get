import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoLocator
import numpy as np

with open('settings.txt') as f:
    freq, step = [float(x) for x in f.read().split('\n')]

with open('measurments.txt') as f:
    d = f.read().split('\n')
    measurments = np.array([int(x) for x in d], dtype = np.float64)
    measurments *= step # Convert to volts
    mcount = len(measurments)

fig, ax = plt.subplots()

ax.plot(freq * np.arange(mcount), measurments, markerfacecolor = '#e28743', markeredgewidth = .7, marker = '*', markevery = 15, markersize = 10, color = '#154c79', lw = 2,
        label = 'V')
ax.set_xlim(0, mcount * freq)
ax.set_ylim(0, 3.3)
ax.legend()

ax.set_title('Измерения')
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

ax.xaxis.set_major_locator(MultipleLocator(freq * mcount / 5))
ax.xaxis.set_major_formatter('{x:.0f}')

ax.xaxis.set_minor_locator(MultipleLocator(freq * mcount / (5 * 5)))

ax.grid(True, 'minor', linestyle = '--', lw = .5)
ax.grid(True, 'major', lw = 1.5, color = '#d1d1d1')

charge_time = freq * np.argmax(measurments)
discharge_time = freq * mcount - charge_time
ax.text(.42, .35, f'Время зарядки: {charge_time:.1f} сек\nВремя разрядки: {discharge_time:.1f} сек', transform = ax.transAxes)

plt.savefig('graph.svg')
plt.show()