#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:08:10 2022

@author: jerrysmacbookpro
"""

import numpy as np

arrA = np.array([[0, 0, 0], [0, 0, 0]])
arrB = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
arrC = np.array([[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]])
arrD = np.eye(3)
arrE = np.linspace(1, 100, 100)
arrF = np.linspace(0, 1, 101)
arrG = np.linspace(100, 1, 199)
arrH = np.random.rand(10, 3)
arrJ = np.random.normal(loc=9, scale=2.5, size=(10, 3))


print(arrA)
print(arrB)
print(arrC)
print(arrD)

print(arrF)
print('arrG:', arrG)
print(arrH)


print(arrE)
print(np.log10(arrE) * 10)
print('mean of arrH is', np.mean(arrH))
print('squared mean of arrJ is', np.sqrt(np.mean(arrJ**2)))

print(arrJ)
print(np.add(arrJ, (1.5, -9, 0)))

print(arrA.dtype)
print(arrB.dtype)
print(arrB.dtype)
print(arrC.dtype)
print(arrD.dtype)
print(arrE.dtype)
print(arrF.dtype)
print(arrG.dtype)
print(arrH.dtype)
print(arrJ.dtype)
