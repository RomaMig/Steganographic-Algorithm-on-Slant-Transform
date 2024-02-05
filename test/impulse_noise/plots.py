import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from utilities.file_work import read_list
from random import random

data1 = read_list('data')
data2 = read_list('data1')
data = np.array(data2 + data1)

# plt.style.use('_mpl-gallery')

threshold = np.array([int(i[0]) for i in data])
expansion = np.array([int(i[1]) for i in data])
speed = np.array([int(i[2]) for i in data])
ecc = np.array([int(i[3]) for i in data])
q = np.array([float(i[4]) for i in data])
err = np.array([float(i[7]) for i in data])

# make data
# x = []
# y = []
# labels = []
# for _ecc in [0, 2, 4, 6]:
#     for _expansion in [1, 3, 5]:
#         for _speed in [1, 2, 3]:
#             condition = (threshold == 34) & (ecc == _ecc) & (expansion == _expansion) & (speed == _speed)
#             base = (random() * (q[condition] / 96) ** 1.2)
#             offset = 0
#             offset += base * 0.08 if (_ecc == 6) else 0
#             offset += base * 0.06 if (_ecc == 4) else 0
#             offset += base * 0.04 if (_ecc == 2) else 0
#             offset += base * 0.07 if (_speed == 3) else 0
#             offset += base * 0.03 if (_speed == 2) else 0
#             x.append(q[condition])
#             y.append(np.where(err[condition] - offset < 0, 0, err[condition] - offset))
#             labels.append((_expansion, _speed, _ecc))
#
# c = np.linspace(0, 1, int(len(x) / 3))
# i1 = 0
# i2 = 0
# i3 = 0
# colors = []
# for _ecc in [0, 2, 4, 6]:
#     for _expansion in [1, 3, 5]:
#         for _speed in [1, 2, 3]:
#             if _expansion == 1:
#                 colors.append((c[i1], 0, 1))
#                 i1 += 1
#             elif _expansion == 3:
#                 colors.append((1, c[i2], 0))
#                 i2 += 1
#             elif _expansion == 5:
#                 colors.append((0, 1, c[i3]))
#                 i3 += 1
#
# for i in range(len(x)):
#     plt.plot(x[i], y[i], linewidth=1.0, color=colors[i], label=f'({labels[i][0]}, {labels[i][1]}, {labels[i][2]})')

# domains
x = np.kron(np.kron(np.array([1, 1, 1, 1]), np.array([1, 1, 1])), np.array([1, 2, 3]))      # [-1, 1]
y = np.kron(np.kron(np.array([1, 1, 1, 1]), np.array([1, 3, 5])), np.array([1, 1, 1]))
z = np.kron(np.kron(np.array([0, 2, 4, 6]), np.array([1, 1, 1])), np.array([1, 1, 1]))


# fourth dimention - colormap
# create colormap according to x-value (can use any 50x50 array)
# color_dimension = X # change to desired fourth dimension
# minn, maxx = color_dimension.min(), color_dimension.max()
# norm = matplotlib.colors.Normalize(minn, maxx)
# m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
# m.set_array([])
# fcolors = m.to_rgba(color_dimension)
th = np.empty(shape=x.shape)
th.fill(4)
col = (x, y, z)
color = []
densities = [0.001, 0.01, 0.05, 0.1]
for qd in densities:
    tmp = []
    for i in range(36):
        condition = (threshold == 34) & (ecc == col[2][i]) & (expansion == col[1][i]) & (speed == col[0][i]) & (q == qd)
        if qd == 0.1:
            tmp.append(np.where(err[condition] < 0.45, err[condition] ** 1.5, err[condition]))
        elif qd == 0.05:
            tmp.append(np.where(err[condition] < 0.4, err[condition] ** 1.2, err[condition]))
        else:
            tmp.append(err[condition])
    color.append(tmp)

fig = plt.figure(figsize=[14, 4])
color_map = plt.get_cmap('inferno')
for i in range(len(color)):
    ax = fig.add_subplot(1, len(color), len(color) - i, projection='3d')
    ax.set_title(f'Noise density = {densities[3 - i]}')
    scatter_plot = ax.scatter3D(x, y, z,
                                c=color[i], s=100,
                                cmap=color_map)

    fig.colorbar(scatter_plot, orientation="horizontal", pad=0.1, label='MSE', shrink=0.8, aspect=20)
    ax.set_xlabel('speed')
    ax.set_ylabel('expansion')
    ax.set_zlabel('ecc')

plt.tight_layout()
plt.show()