#%%
import numpy as np

class Sudoku:
  def __init__(self, init_values):
    self.b = np.array(init_values)
  
  def __str__(self):
    #s = '\n'.join(' '.join(line) for line in self.b[:])
    return ('\n'.join(' '.join(str(e) for e in line) for line in self.b))

  def insert(self, row, col, value):
    if(self.b[row, col] == 0 and
      value not in self.b[row, :] and
      value not in self.b[:, col])  :
      self.b[row, col] = value
      return True
    else:
      return False

sudoku_init = [[0, 2, 0, 5, 0, 1, 0, 9, 0],
               [8, 0, 0, 0, 2, 3, 0, 0, 6],
               [0, 3, 0, 0, 6, 0, 0, 7, 0], 
               [0, 0, 1, 0, 0, 0, 6, 0, 0], 
               [5, 4, 0, 0, 0, 0, 0, 1, 9], 
               [0, 0, 2, 0, 0, 0, 7, 0, 0], 
               [0, 9, 0, 0, 3, 0, 0, 8, 0], 
               [2, 0, 0, 8, 0, 4, 0, 0, 7], 
               [0, 1, 0, 9, 0, 7, 0, 6, 0]]

s = Sudoku(sudoku_init)
print(s.insert(0,2,666))
print(s)


#%%

import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 80, 145, 198, 265, 360, 460, 560, 720, 820,
              950, 1080, 1200, 1300, 1440])
P = np.array([120, 600, 960, 1320, 1680, 2370, 2850, 3480,
              4140, 4272, 3900, 3120, 1860, 1032, 120])

t = t / 60
P = P / 1000

fig, ax = plt.subplots()
ax.plot(t, P, "k-o", label="Solarzelle")
ax.plot(t, np.ones_like(P), "k--", label="Min. Leistung")
ax.set_ylabel("P(kW)")
ax.set_xlabel("t(h)")
ax.set_ylim(0,6)
ax.set_xlim(0,24)
ax.set_xticks(np.linspace(0,24,7))
ax.grid(True)
ax.legend(loc="upper right")

# %%
a = ['Adam', 'Tim', 'Anna', 'Milo']
b = {n: name for n, name in enumerate([x for x in a if 'a' in x])}
print(b)

b = {}
i = 0
for name in a:
  if 'a' in name:
    b[i] = name
    i += 1
print(b)

# %%
def foo(a):
  return 1/a
foo(0)

# %%
a = 0.0000056
print(f"{a:.3e}")
b = "Python"
print(f"{b:*^10}")
c = 1234.56
print(f"{c:.3f}")
d = 16777248
print(f"0x{d:08X}")

# %%
def mirror_number(n):
  #return int(str(n)[::-1])
  if str(n).endswith('0'):
    return None
  else:
    return int(str(n)[::-1])
print(mirror_number(12345))

# %%
def num_ones(n):
  return f"{n:b}".count('1')

print(num_ones(2020))

# %%
mylist = [-4, 10, 6, -10, 2]
mylist.sort(key=lambda x: x if x > 0 else -x)
print(mylist)
s = 'Spaghetti Bolognese'
print(s[1:-1:3])
print(f'{"*".join("a"*x for x in range(2, 5))}')