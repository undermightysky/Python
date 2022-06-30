# -*- coding: utf-8 -*-

# %% ---- a) ----

import numpy as np

def transpose(s):
    p = s.split("\n")
    m = len(p)
    n = len(p[0])
    o = []
    
    for i in range(n):
      l = ""
      for j in range(m):
        l += p[j][i] 
      o.append(l)
    
    return "\n".join(o)

def transpose2(s):
    return '\n'.join(''.join(column) for column in zip(*s.splitlines()))

matrix = "ABC\nDEF\nGHI\nJKL"

print('V1:\n', transpose(matrix))
print('V2:\n', transpose2(matrix))

# %% ---- b) ----

abs_values = []
f = open("data.txt") 
lines = f.readlines() 
f.close()

for x in lines:
  x = float(x) 
  if x < 0:
    abs_values.append((-1)*x) 
  else:
    abs_values.append(x)

print(abs_values[:10])


absVal = np.abs(np.loadtxt('data.txt')).tolist()
print(absVal[:10])

# %% ---- c) ----

x = np.array([3, 4, 5])

M = np.zeros((len(x), 3)) 
for i in range(len(x)):
  M[i, :] = [1, x[i], x[i]**2]

print(M)

M = np.c_[np.ones_like(x), x, x**2]
print(M)

# %% ---- d) ----
mailing_list = ["peter@ost.ch", "laura@gmail.com", "linda@ost.ch", "carlos@gmx.com",
"ian@ost.ch"]

def ost_only(addresses): 
  mail_ost = []
  for addr in addresses:
    if "@ost.ch" == addr[-7:]:
      mail_ost.append(addr) 
  return mail_ost

def ost_only2(addresses):
  mail_ost = [addr for addr in addresses if addr.endswith('@ost.ch')]
  return mail_ost

print(ost_only(mailing_list))
print(ost_only2(mailing_list))

# %% ---- e) ----

x = '0XF3'

def is_hex(s):
  if s.startswith("0x") or s.startswith("0X"):
    s = s[2:]
  for character in s:
    if character not in "0123456789ABCDEFabcdef": break
  else:
    return True
  return False


def is_hex2(s):
  try:
    int(s, 16)
  except ValueError:
    return False
  else:
    return True


print(is_hex(x))
print(is_hex2(x))

# %% ---- f) ----

def summation(a, b, p, N): 
  p = np.asarray(p)
  dx = a/N
  dy = b/N
  x = np.linspace(0, a, N, endpoint=False) + dx/2 
  y = np.linspace(0, b, N, endpoint=False) + dy/2 
  z=0
  dS = dx*dy*np.array([0, 0, 1]) 
  S=0
  for xi in range(N):
    for yi in range(N):
      R = np.array([x[xi], y[yi], z]) - p
      S += np.abs(np.inner(R/np.linalg.norm(R), dS))
  return S

def summation2(a, b, p, N):
  p = np.asarray(p)
  dx = a/N
  dy = b/N
  x = np.linspace(0, a, N, endpoint=False) + dx/2 
  y = np.linspace(0, b, N, endpoint=False) + dy/2 
  z=0

  dS = dx*dy*np.array([0, 0, 1]) 
  X, Y = np.meshgrid(x, y)
  R = np.stack([X, Y, np.full_like(X, z)], axis=-1) - p
  R_unit = R/np.linalg.norm(R, keepdims=True, axis = -1)
  S = np.sum(np.abs(np.inner(R_unit, dS)))
  return S




import time
a = 3
b = 4
p = [1.5, 2, 100]
N = 1000 
tic = time.time()
print(summation(a=a, b=b, p=p, N=N))
print(summation2(a=a, b=b, p=p, N=N))
toc = time.time()
print(f"elapsed time: {toc - tic:.3f} s")



