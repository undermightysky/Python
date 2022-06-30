# -*- coding: utf-8 -*-
# schwingkreis_muloe.py

import numpy as np
import matplotlib.pyplot as plt


# --- Parameters --------------------------------------------------------------
a0 = 5                          # amplitude
tau = 0.2                       # time constant
fn = 10                         # natural frequency
phi = -np.pi/2                  # phase
t = np.linspace(0, 1, 1001)     # time vector

# --- Oscillation -------------------------------------------------------------
envelope = a0*np.exp(-t/tau)
a = envelope*np.cos(2*np.pi*fn*t + phi)

# --- Plot --------------------------------------------------------------------
fig, ax = plt.subplots(constrained_layout=True)
ax.plot(t, envelope, 'k--', alpha=0.5, label='envelope')
ax.plot(t, -envelope, 'k--', alpha=0.5)
ax.plot(t, a, label='damped oscillation')
ax.grid(True)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.margins(x=0)
ax.legend()

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html
fig.savefig('damped_oscillation.pdf')

# show plots (not needed in IPython/Spyder)
plt.show()
