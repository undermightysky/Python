# -*- coding: utf-8 -*-
# kleinste_fehlerquadrate_muloe.py

import numpy as np
import matplotlib.pyplot as plt

# --- Data import -------------------------------------------------------------
x, y = np.loadtxt('measurements.txt', delimiter=',', unpack=True)

# --- Matrix ------------------------------------------------------------------
M = np.c_[x**2, x, np.ones_like(x)]
# or:
# M = np.column_stack([x**2, x, np.ones_like(x)])

print(f'M.shape = {M.shape}')

# --- Least-squares solution --------------------------------------------------
# a, b, c = np.linalg.solve(M.T @ M, M.T @ y)
# or:
a, b, c = np.linalg.lstsq(M, y, rcond=None)[0]
print(f'a = {a:g}, b = {b:g}, c = {c:g}')

# --- Plot --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3), constrained_layout=True)

x_fine = np.linspace(np.min(x), np.max(x), 100)

ax.plot(x, y, 'o', markersize=2, label='data points')
ax.plot(x_fine,
        a*x_fine**2 + b*x_fine + c,
        linewidth=4,
        label='fitted parabola')

# Text label:
#     https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html

# Use $...$ for LaTeX equations:
#     https://matplotlib.org/stable/tutorials/text/mathtext.html

# Properties of bbox:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html

ax.text(1.15,
        5,
        f'$y = {a:.2f}x^{2} {b:+.2f}x  {c:+.2f}$',
        fontsize=12,
        ha='center',  # horizontal alignment
        va='center',  # vertical alignment
        bbox=dict(facecolor='white', boxstyle='round'),
        )

ax.margins(x=0)
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# save
fig.savefig('parabola_lstsq.pdf')
fig.savefig('parabola_lstsq.png')

# show plots (not needed in IPython/Spyder)
plt.show()
