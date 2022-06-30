# -*- coding: utf-8 -*-

# %%

import numpy as np
import matplotlib.pyplot as plt


phi = (1 + np.sqrt(5)) / 2

g = (2 * np.pi) * (1 - 1/phi)

N = 800
n = np.arange(N)

points = np.sqrt(N - n) * [np.cos(n*g), np.sin(n*g)]

fig, ax = plt.subplots()

# all points
ax.scatter(*points, c='k', alpha = 0.1)

# draw colored points
for k, color in zip([5, 21, 34], ['r', 'g', 'b']):
    ax.scatter(*points[:, n % k == 0],
               c=color, 
               label=f'k={k}',
               alpha=0.6)
