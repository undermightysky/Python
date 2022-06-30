#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:26:26 2022

@author: jerrysmacbookpro
"""
import numpy as np


def projection(x, r0, u):
    x = np.asarray(x)
    r0 = np.asarray(r0)
    u = np.asarray(u)
    return r0 + ((x - r0) @ u) / (u @ u) * u


print(projection(x=[5, 2], r0=[1, 2], u=[1, 1]))
