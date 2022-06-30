#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:07:09 2022

@author: jerrysmacbookpro
"""
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
z = np.array([9, 10, 11, 12])

A = np.stack((x, y, z))
B = np.stack((x, y, z)).T
C = np.concatenate(B)
D = np.concatenate(A)
E = np.reshape(B, (2, 2, 3))
F = np.reshape(A, (3, 2, 2))

x[0] = 13

print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)


g = np.array([1, 2, 3, 4, 5])
h = g[1:3]
h[0] = 200
# print(g[1])

J = np.full((2, 3), 5)
k = J.ravel()
k[-1] = 0
# print(k)
# print(J)

L = np.arange(0, 10).reshape(5, 2)
M = np.tile(L, (1, 3))
# print(M)

n = np.r_[np.linspace(0, 1, 3), 20:27]
# print(n)

P = np.c_[0:4, np.eye(4)]
# print(P)
