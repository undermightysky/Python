#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:20:45 2022

@author: jerrysmacbookpro
"""

import numpy as np

cnts = np.array([[7, 4], [3, 5]])
prices = np.array([6.50, 5.25])

print(np.linalg.solve(cnts, prices))
