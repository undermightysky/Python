# %% 


class Shoppingcart:
  def __init__(self, init):
    self.products = {k: {key: value for key, value in v}
                     for k, v in init}
  
  def __str__(self):
    cart = ''
    for k, v in self.products.items():
      cart += f"{v['quantity']}x {v['name']} (P/N {k})\n"
    return cart

  @property
  def total(self):
    return float(sum(v['price'] * v['quantity'] for v in self.products.values()))

init = [('123-456', [('name', 'Umbrella'),
                    ('price', 29.90),
                    ('quantity', 1)]),
        ('010-777', [('name', 'Toothbrush'),
                    ('price', 3.50),
                    ('quantity', 2)])]

emp = Shoppingcart(init)

print(emp.products['123-456'])
print(emp)
print('Total: ', emp.total)

# %%

import numpy as np
from regex import W

def create_matrix(n):
  m = np.arange(1, (n*n+1)).reshape(n,n)
  return np.c_[np.zeros(n), m, np.ones(n)]

print(create_matrix(3))

# %% 
def downsample(data, k):
  m, n = data.shape
  return np.mean(data[:m//k*k].reshape(m//k, k, n) ,
                  axis=1)

data = np.arange(7*2).reshape(7, 2)
print(data)
print(downsample(data, 3))

# %% 
x = np.linspace(-10, 10, 3)
y = np.linspace(0, 10, 5)

X, Y = np.meshgrid(x, y)
Z = np.stack([X, Y], axis=-1)

print('X:\n', X)
print('Y:\n', Y)
print('Z:\n', Z)

print(Z.shape)
print(Z[1, 2])

# %%
def work(p):
  d = np.roll(p,-1) - p
  print(np.roll(p,-1))
  print(p)
  print(d)
  r = 0.5 * (np.roll(p,-1) + p)
  f = r / (np.abs(r)**2)
  w = sum(f*d)
  return w

p = np.array([[1, 0],
            [2, 1],
            [3, 2],
            [4, 3]])

print(work(p))

# %% 
import numpy as np
import matplotlib.pyplot as plt

A = np.array([10, 40, 50, 30, 10])
B = np.array([1, 2, 4, 5, 4])
fig, ax = plt.subplots()
ax.plot(A, B, "b-s")
ax.set_xlabel("Parameter A")
ax.set_ylabel("Parameter B")
ax.grid(True)
ax.set_xlim(10, 50)
ax.set_ylim(1, 5)
ax.set_xticks([10, 30, 40, 50])
ax.set_yticks([1, 2, 4, 5])

# %%
def num_bits(n):
  return len(str(bin(n)))-2

print(num_bits(12))
print(num_bits(2021))

# %%
letters = ('b', 'a', 'd', 'c')
numbers = (1, 3, 2, 4)

letters, numbers = zip(*sorted(zip(letters, numbers)))

print(letters)
print(numbers)

# %%
value = 12.345
n = 10

print(f"{value:05.2f}")
print(f"value={value}, ")
print(f"n={n}")
print(f"{n:*>4}")
print(f"{n:X}")

# %%
things = ['huhu', 13, 666, 'Yeah', 'm', 'bb']
value = 'm'
#things = [a for a in things if a != value]
things.remove(value)
print(things)

# %%
fruechte = ["Apfel", "Banane", "Erdbeere", "Kirsche"]
mengen = [3, 5, 10, 12]
lager = {}
for frucht, menge in zip(fruechte, mengen):
  lager[frucht] = menge
print(lager)
lager = {k: v for k, v in zip(fruechte, mengen)}
print(lager)

# %% 
a = [13, 10, 1, 14, 24, 6, 17]
print(np.argsort(a).tolist())

def argsort(a):
  return [a.index(i) for i in sorted(a)]

print(argsort(a))

# %%
value = 56.164
n=8 
print(f"{value:>0{n}.1f}")

a = np.array([1, 2]) 
print(np.tile(a, (2, 3)))

people = ["Alice", "Ted", "Carol", "Tina"] 
a = id(people)
people[:] = ["Wally", "Bob"]
b = id(people)
print(people)
people = ["Wally", "Bob"] 
c = id(people)

print(a, b, c)

text = """ This is a
multiline string with a lot of unnecessary spaces.""" 
print(" ".join(text.split()))

# %%
a, b, c = 1, 2, 3
print(a, b, c)
a, *b, c = 1, 2, 3
print(a, b, c)