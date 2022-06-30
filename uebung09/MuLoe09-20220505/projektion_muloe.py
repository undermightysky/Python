# -*- coding: utf-8 -*-

import numpy as np


def projection(x, r0, u):
    x = np.asarray(x)
    u = np.asarray(u)
    r0 = np.asarray(r0)
    return r0 + ((x - r0) @ u)/(u @ u)*u


print(projection(x=[5, 2], u=[1, 1], r0=[1, 2]))
