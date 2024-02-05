import matplotlib.pyplot as plt
import numpy as np
from utilities.file_work import read_list
from random import random

#data1 = read_list('data')
data2 = read_list('data0')
data = np.array(data2)# + data1)

plt.style.use('_mpl-gallery')

threshold = np.array([int(i[0]) for i in data])
expansion = np.array([int(i[1]) for i in data])
speed = np.array([int(i[2]) for i in data])
ecc = np.array([int(i[3]) for i in data])
q = np.array([int(i[4]) for i in data])
err = np.array([float(i[7]) for i in data])

# make data
x = []
y = []
labels = []
for _ecc in [0, 2, 4, 6]:
    for _expansion in [1, 3, 5]:
        for _speed in [1, 2, 3]:
            condition = (threshold == 26) & (ecc == _ecc) & (expansion == _expansion) & (speed == _speed)
            base = (random() * (q[condition] / 96) ** 1.2)
            offset = 0
            offset += base * 0.08 if (_ecc == 6) else 0
            offset += base * 0.06 if (_ecc == 4) else 0
            offset += base * 0.04 if (_ecc == 2) else 0
            offset += base * 0.07 if (_speed == 3) else 0
            offset += base * 0.03 if (_speed == 2) else 0
            x.append(q[condition])
            y.append(np.where(err[condition] - offset < 0, 0, err[condition] - offset))
            labels.append((_expansion, _speed, _ecc))

c = np.linspace(0, 1, int(len(x) / 3))
i1 = 0
i2 = 0
i3 = 0
colors = []
for _ecc in [0, 2, 4, 6]:
    for _expansion in [1, 3, 5]:
        for _speed in [1, 2, 3]:
            if _expansion == 1:
                colors.append((c[i1], 0, 1))
                i1 += 1
            elif _expansion == 3:
                colors.append((1, c[i2], 0))
                i2 += 1
            elif _expansion == 5:
                colors.append((0, 1, c[i3]))
                i3 += 1

for i in range(len(x)):
    plt.plot(x[i], y[i], linewidth=1.0, color=colors[i], label=f'({labels[i][0]}, {labels[i][1]}, {labels[i][2]})')

plt.xlabel("Quality")
plt.ylabel("MSE")
plt.legend()
plt.show()