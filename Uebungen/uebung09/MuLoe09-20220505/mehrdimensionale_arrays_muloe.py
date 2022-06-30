# -*- coding: utf-8 -*-

import numpy as np

x = np.r_[1:5]
y = np.r_[5:9]
z = np.r_[9:13]

A = np.row_stack([x, y, z])

B = np.c_[x, y, z]
# or B = np.column_stack([x, y, z])

c = B.flatten()

d = np.r_[x, y, z]
# or d = np.concatenate([x, y, z])

E = c.reshape(2, 2, 3)

F = d.reshape(3, 2, 2)

# ---

g = np.array([1, 2, 3, 4, 5])
h = g[1:3]
h[0] = 200
print(f'g[1]={g[1]}')

# ---

J = np.full((2, 3), 5)
k = J.ravel()
k[-1] = 0
print(f'k={k}')
print(f'J=\n{J}')

# ---

L = np.arange(0, 10).reshape(5, 2)
M = np.tile(L, (1, 3))
print(f'M=\n{M}')

# ---

n = np.r_[np.linspace(0, 1, 3), 20:27]
print(f'n={n}')

# ---

P = np.c_[0:4, np.eye(4)]
print(f'P=\n{P}')
