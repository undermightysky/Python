# -*- coding: utf-8 -*-
# elektrisches_feld_muloe.py
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

# https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html

# %% Parameters ---------------------------------------------------------------

# first point charge
Q1 = 1e-9                       # Coulomb
P1 = np.array([1, 0, -0.5])     # (x, y, z), position

# second point charge
Q2 = -1e-9                      # Coulomb
P2 = np.array([-1, 0, -0.5])    # (x, y, z), position

# xy-plane
x = np.linspace(-3, 3, 151)
y = np.linspace(-2.5, 2.5, 101)
z = 0
X, Y = np.meshgrid(x, y)
Z = np.full_like(X, z)

# points in the xy-plane
PE = np.stack([X, Y, Z], axis=-1)

# %% Computation of the electrical field --------------------------------------


def e_field(Q, epsilon_r, R):
    return Q*R/(4*np.pi*epsilon_0*epsilon_r
                * np.linalg.norm(R, axis=-1, keepdims=True)**3)


# vectors from the first point charge to every point in the xy-plane
R1 = PE - P1

# vectors from the second point charge to every point in the xy-plane
R2 = PE - P2

# electric field due to the first charge
E1 = e_field(Q1, 1, R1)

# electric field due to the second charge
E2 = e_field(Q2, 1, R2)

# superposition of the two fields
E = E1 + E2


# %% Data visualization -------------------------------------------------------

fig, ax = plt.subplots(constrained_layout=True)

# norm of the electric field
CS = ax.contourf(PE[..., 0],  # x
                 PE[..., 1],  # y
                 np.linalg.norm(E, axis=-1),  # z
                 50,  # levels
                 )
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('V/m')

# field lines
ax.streamplot(PE[..., 0],  # x
              PE[..., 1],  # y
              E[..., 0],   # u
              E[..., 1],   # v
              color='white',
              )

# axis limits equal to data limits
ax.axis('image')

# add labels
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

# save figure
fig.savefig('elektrisches_feld.pdf')

plt.show()
