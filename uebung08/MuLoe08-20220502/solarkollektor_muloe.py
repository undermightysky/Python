# -*- coding: utf-8 -*-

import numpy as np


def solar_energy(a, b, n, T, E, phi, theta):
    n = np.asarray(n)
    s = np.array([np.cos(theta)*np.cos(phi),
                  np.cos(theta)*np.sin(phi),
                  np.sin(theta)]).T
    # alternative solution:
    # s = np.c_[np.cos(theta)*np.cos(phi),
    #           np.cos(theta)*np.sin(phi),
    #           np.sin(theta)]
    p = (s @ n)/np.sqrt(n @ n)
    return a*b*E*T*np.sum(p[p > 0])


T = 1/3600
t = np.arange(0, 12, T)
phi = 5*np.pi*t/48
theta = np.pi/4*np.sin(np.pi*t/12)


energy = solar_energy(a=2,
                      b=1.5,
                      n=[0.5, 2, 10],
                      T=T,
                      E=1000,
                      phi=phi,
                      theta=theta)

print(f'Energy = {energy:g}')
