#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:28:05 2022

@author: jerrysmacbookpro
"""

import numpy as np


def solar_energy(a, b, n, T, E, phi, theta):

    s = np.array([np.cos(theta)*np.cos(phi),
                  np.cos(theta)*np.sin(phi),
                  np.sin(theta)]).T

    # pk = (s @ n) / np.linalg.norm(n)
    pk = (s @ n) / np.sqrt(n @ n)

    return float(a * b * E * T * np.sum(pk[pk > 0]))


T = 1/3600
t = np.arange(0, 12, T)
phi = 5 * np.pi * t / 48
theta = np.pi / 4 * np.sin(np.pi*t/12)
n = np.array([0.5, 2, 10])

print('Solar power energy is ', solar_energy(a=2,
                                             b=1.5,
                                             n=n,
                                             T=T,
                                             E=1000,
                                             phi=phi,
                                             theta=theta))
