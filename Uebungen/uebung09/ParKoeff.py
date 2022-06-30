#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:51:15 2022

@author: jerrysmacbookpro
"""
import numpy as np

p1 = np.array([-1, 6])
p2 = np.array([2, 0])
p3 = np.array([3, 4])

M = np.column_stack([p1, p2, p3])

x, y = M

o = np.ones_like(x)
M = np.c_[x**2, x, o]

print(x)
print(y)
print(o)
print(M)

res = np.linalg.solve(M, y)

print(res)
