#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
Created on Wed May 11 12:51:33 2022

@author: jerrysmacbookpro
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.loadtxt('measurements.txt', delimiter=',')
x, y = np.column_stack(t)

m = np.c_[x**2, x, np.full_like(x, 1)]

a, b, c = np.linalg.solve(m.T @ m, m.T @ y)
print(f'a: {a:.3f}, b: {b:.3f}, c: {c:.3f}')

x_fine = np.linspace(np.min(x), np.max(x), 1000)

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(x, y, '.', label='data points')
ax.plot(x_fine,
        a*x_fine**2 + b*x_fine + c,
        linewidth=4,
        label='fitted parabola')
ax.margins(x=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend()

ax.text(1.15,
        5,
        f'$y = {a:.2f}x^2 {b:.2f}x + {c:.2f}$',
        fontsize=12,
        ha='center',
        va='center',
        bbox=dict(facecolor='white', boxstyle='round'))
