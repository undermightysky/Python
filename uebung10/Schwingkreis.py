#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
Created on Tue May 10 17:03:53 2022

@author: jerrysmacbookpro
"""


import matplotlib.pyplot as plt
import numpy as np

fn = 10
phi = -np.pi/2
tau = 0.2
a0 = 5

t = np.arange(0, 1, 0.001)
e = a0 * np.exp(-t/tau)
a = e * np.cos(2 * np.pi * fn * t + phi)


plt.figure()
plt.plot(t, a, '-', label='damped oscillation')
plt.plot(t, e, '--', label='envelope', color='grey')
plt.plot(t, -e, '--', color='grey')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.xlim(0, 1)
plt.ylim(-5, 5)

plt.grid(which='major')
plt.minorticks_on()

plt.legend()
