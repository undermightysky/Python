# -*- coding: utf-8 -*-
# gleichungssystem_muloe.py

import numpy as np

M = np.array([[7, 4],
              [3, 5]])

y = np.array([6.5, 5.25])

[x1, x2] = np.linalg.solve(M, y)

print(f'Apfel = {x1:.2f} Fr./Stk.')
print(f'Birne = {x2:.2f} Fr./Stk.')
