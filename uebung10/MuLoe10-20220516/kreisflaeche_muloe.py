# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# --- parameters --------------------------------------------------------------
r = 2  # circle radius
k = np.arange(2, 11)
N = 2**k  # number of polygon edges
A_circle = r**2*np.pi

# --- compute the polygon area ------------------------------------------------
A = []
for n in N:
    # corner angles
    phi = np.linspace(0, 2*np.pi, n + 1)
    # corners
    P = np.c_[r*np.cos(phi), r*np.sin(phi)]
    # vector between the corners
    dl = P[1:, :] - P[:-1, :]
    # midpoints of the edges
    M = (P[1:, :] + P[:-1, :])/2
    # compute the polygon area
    A.append(np.sum(np.linalg.norm(M, axis=-1)*np.linalg.norm(dl, axis=-1)/2))

A = np.array(A)

# --- visualize the results ---------------------------------------------------
fig, (ax, ax2) = plt.subplots(2, 1, constrained_layout=True, num=1, clear=True, sharex=True)
ax.plot(k, A, '.-', label='Polygon area')
ax.axhline(r**2*np.pi,
           color='r',
           linestyle='--',
           label=fr'Circle area ($r={r:g}$)')

ax.grid(True)
ax.set_ylabel(r'Area')
ax.legend()

ax2.semilogy(k, np.abs(A - A_circle)/A_circle, '.-')
ax2.grid(which='both')
ax2.set_xticks(k)
ax2.set_xticklabels(N)
ax2.set_xlabel(r'Number of polygon edges ($N$)')
ax2.set_ylabel('Relative Error')
ax2.set_xlim(k[0], k[-1])

fig.savefig('kreisflaeche.pdf')

plt.show()
