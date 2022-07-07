#%%
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 0.1, 1000)
v = np.sqrt(2) * np.sin(2*np.pi*50*t)
r = np.abs(v)
p = v**2

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(t, v, "k:", label = "v(t)")
ax.plot(t, r, "k-", label = "r(t)")
ax.plot(t, p, "k--", label = "p(t)")
ax.set_xlabel("t")
ax.set_xlim(0, 0.05)
ax.set_ylim(-2, 2.5)
ax.legend(loc = "lower left")
ax.grid()

#%%

values = [3.23876, -2.382876342, 1.11111, 98.23876981237]

s = ';'.join(([f"{x:.3f}" for x in values]))
print(s)

