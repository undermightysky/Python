#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:38:04 2022

@author: jerrysmacbookpro
"""

matrix = [
    [1, 2, 3, 4, 5, 6],
    [10, 20, 30, 40, 50, 60],
    [100, 200, 300, 400, 500, 600],
]

matrix_str = ';'.join(str(n) for c in matrix for n in c)
print(matrix_str)

matrix_csum = [sum(d) for d in zip(*matrix)]
print(matrix_csum)
