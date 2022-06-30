# -*- coding: utf-8 -*-

import numpy as np


A1 = np.array([[1, -1],
               [-3, -1]])

A2 = np.array([[0, 1, 1],
               [1, 0, 1],
               [1, 1, 0]])


def power(A, n):
    w, T = np.linalg.eig(A)
    D = w*np.identity(len(w))
    return T @ D**n @ np.linalg.inv(T)


print(f'power(A1, 5)=\n{power(A1, 5)}')
print(f'power(A2, 3)=\n{power(A2, 3)}')
