# -*- coding: utf-8 -*-

# %%
import numpy as np
import matplotlib.pyplot as plt


# %% Parameters ---------------------------------------------------------------
N = 800  # number of points
golden_ratio = (1 + np.sqrt(5))/2
golden_angle = 2*np.pi*(1 - 1/golden_ratio)


# %% Points -------------------------------------------------------------------
n = np.arange(N)
angle = n*golden_angle
points = np.sqrt(N - n)*[np.cos(angle), np.sin(angle)]


# %% Visualization ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4.8, 4.8), constrained_layout=True)

# all points
ax.scatter(*points, c='k', alpha=0.1)

# draw the colored points
for k, color in zip([5, 21, 34], ['r', 'g', 'b']):
    ax.scatter(*points[:, n % k == 0],
               c=color,
               label=f'k={k}',
               alpha=0.6)

# scale axis equal and make invisible
ax.axis('equal')
ax.axis('off')
# remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.legend(loc='upper right')
fig.savefig('scatter.pdf')

plt.show()
