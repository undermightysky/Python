# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# %% generate data ------------------------------------------------------------
# x = np.linspace(-1.5, 1, 25*3 + 1)
# y = np.linspace(-1.5, 1.5, 30*3 + 1)

# X, Y = np.meshgrid(x, y)
# Z = np.abs(1/((X + 1j*Y)**2 + 0.7654*(X + 1j*Y) + 1)
#             / ((X + 1j*Y)**2 + 1.8478*(X + 1j*Y) + 1)).clip(0, 10)

# data = np.zeros((len(y) + 1, len(x) + 1))
# data[1:, 0] = y*10
# data[0, 1:] = x*10
# data[1:, 1:] = Z/2

# np.savetxt('landschaft.csv', data, delimiter=',', fmt='%.4f')

# %% load data ----------------------------------------------------------------
data = np.loadtxt('landschaft.csv', delimiter=',')

x = data[0, 1:]
y = data[1:, 0]
Z = data[1:, 1:]

X, Y = np.meshgrid(x, y)

# %% visualize data -----------------------------------------------------------
fig, ax = plt.subplots(constrained_layout=True,
                       subplot_kw=dict(projection="3d"))

# or:
# fig = plt.figure(constrained_layout=True)
# ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='terrain', ccount=len(x), rcount=len(y))
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_zlabel('z (km)')
ax.view_init(elev=20, azim=-66)

fig.savefig('landschaft.pdf')

plt.show()
