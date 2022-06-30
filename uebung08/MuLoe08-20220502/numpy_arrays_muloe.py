# -*- coding: utf-8 -*-
# numpy_arrays_muloe.py


import numpy as np

A = np.zeros((2, 3))

B = np.ones((3, 3))

C = np.full((2, 6), 4)

D = np.identity(3)
# or
# D = np.eye(3)

E = np.arange(1, 101)

F = np.linspace(0, 1, 101)

G = np.arange(100, 1 - 0.5, -0.5)
# or:
# G = np.linspace(100, 1, 199)

H = np.random.rand(10, 3)
# or:
# H = np.random.random((10, 3))

J = np.random.randn(10, 3)*2.5 + 9

# ---

E_dB = 10*np.log10(E)

# ---

H_mean = np.mean(H)

# ---

J_rms = np.sqrt(np.mean(J**2))

# ---

J_offset = J + [1.5, -9, 0]

# ---

# C and E contain only integers
for name, obj in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F),
                  ('G', G), ('H', H), ('J', J)]:
    print(f'{name}:{obj.dtype}')

print('--- fixed ---')

# specify the data type at creation
C = np.full((2, 6), 4, dtype=float)
# or C = np.full((2, 6), 4.)
E = np.arange(1, 101, dtype=float)
# or E = np.arange(1., 101.)

# or create a new array with the desired data type
C = C.astype(float)
E = E.astype(float)

for name, obj in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F),
                  ('G', G), ('H', H), ('J', J)]:
    print(f'{name}:{obj.dtype}')
