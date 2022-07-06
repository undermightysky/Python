# %%
from locale import ABMON_10
import numpy as np
import matplotlib.pyplot as plt
t1 = np.arange(0, 1, 0.001)
t2 = np.linspace(0,2,1000)

v = np.sqrt(2)*np.abs(np.sin(2*np.pi*2*t1))

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(t1, v, '--', label='v(t)')
ax.plot(t1*1.5, v, '-', label='v(t)')
ax.set_xlabel('t')
ax.set_ylim(-0.5, 2.5)
ax.grid(True)
ax.margins(x=0)
ax.legend(loc='upper left')

# %%

a = [5, 5, 4, 3, 6, 7]
b = [2, 7, 8, 5, 7, 4]

b = sorted({it for it in a if it in b})
print(b)

offsets = [-77, 35, 21, -45, -3, 1]

offsets = sorted(offsets, key=abs, reverse=True)
print(offsets)
# %%

a = 'atlas'
b = 'salat'
print(sorted(a) == sorted(b))

# %%
names = ['Pippi', 'Benedikt', 'Max']
names_len = {k: v for k, v in zip(names, (len(n) for n in names))}
print(names_len)

# %%
mt_data = {'Ofen': 2873, 'Bachtel': 1115, 'Eiger': 3967}

print('\n'.join(f"{k:<10} = {v}m"
      for k, v in mt_data.items()))

# %%
arr = np.arange(12)
print(arr)

# %%
a = np.zeros(6).reshape(2,3)
b = np.arange(3)
c = a + b + 1

print(a)
print(b)
print(c)

# %%