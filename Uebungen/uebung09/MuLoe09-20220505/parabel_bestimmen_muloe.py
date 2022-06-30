# -*- coding: utf-8 -*-
# parabel_bestimmen_muloe.py

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters --------------------------------------------------------------
p1 = [-1, 6]
p2 = [2, 0]
p3 = [3, 4]
x, y = np.c_[p1, p2, p3]

print(f'x = {x.tolist()}')
print(f'y = {y.tolist()}')

# --- Matrix ------------------------------------------------------------------
M = np.column_stack([x**2, x, np.ones_like(x)])
# or:
# M = np.c_[x**2, x, np.ones_like(x)]

print(f'M.shape = {M.shape}')

# --- Solution ----------------------------------------------------------------
[a, b, c] = np.linalg.solve(M, y)
print(f'a = {a:g}, b = {b:g}, c = {c:g}')

# --- Plot --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3), constrained_layout=True)

x_ = np.linspace(np.min(x) - 0.5, np.max(x) + 0.5, 100)

ax.plot(x, y, 'ro', label='known points')
ax.plot(x_, a*x_**2 + b*x_ + c, label='parabola')

# Text within $...$ is interpreted as TeX mathematical expression, see:
# https://matplotlib.org/stable/tutorials/text/mathtext.html
ax.text(1,
        5,
        f'$y = {a:g}x^{2} {b:+g}x  {c:+g}$',
        fontsize=14,
        ha='center',
        va='center',
        bbox=dict(facecolor='white', alpha=0.9),
        )

ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# save
fig.savefig('parabola.pdf')

# show plots (not needed in IPython/Spyder)
plt.show()
