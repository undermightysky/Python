# -*- coding: utf-8 -*-

import numpy as np
from pathlib import Path
import time


# --- a) ----------------------------------------------------------------------

def transpose(s):
    return '\n'.join(''.join(column) for column in zip(*s.splitlines()))


matrix = 'ABC\nDEF\nGHI\nJKL'
print(transpose(matrix))


# --- b) ----------------------------------------------------------------------

abs_values = np.abs(np.loadtxt('data.txt')).tolist()
print(abs_values)

# or without numpy
abs_values = [abs(float(x)) for x in Path('data.txt').read_text().splitlines()]
print(abs_values)


# --- c) ----------------------------------------------------------------------

x = np.array([3, 4, 5])
M = np.c_[np.ones_like(x), x, x**2]
print(M)


# --- d) ----------------------------------------------------------------------

def ost_only(addresses):
    return [addr for addr in addresses if addr.endswith("@ost.ch")]


mailing_list = ["peter@ost.ch", "laura@gmail.com", "linda@ost.ch",
                "carlos@gmx.com", "ian@ost.ch"]
print(ost_only(mailing_list))


# --- e) ----------------------------------------------------------------------

def is_hex(s):
    try:
        int(s, 16)
    except ValueError:
        return False
    else:
        return True


print([f'{x}: {is_hex(x)}' for x in ["0xF3", "0XF3", "aa55", "456hex"]])


# --- f) ----------------------------------------------------------------------

def summation(a, b, p, N):
    p = np.asarray(p)
    dx = a/N
    dy = b/N
    x = np.linspace(0, a, N, endpoint=False) + dx/2
    y = np.linspace(0, b, N, endpoint=False) + dy/2
    z = 0

    dS = dx*dy*np.array([0, 0, 1])
    X, Y = np.meshgrid(x, y)
    R = np.stack([X, Y, np.full_like(X, z)], axis=-1) - p
    R_unit = R/np.linalg.norm(R, keepdims=True, axis=-1)
    S = np.sum(np.abs(np.inner(R_unit, dS)))
    return S


tic = time.time()
S = summation(a=3, b=4, p=[1.5, 2, 100], N=1000)
toc = time.time()
print(S)
print(f'elapsed time: {toc - tic:.3f} s')
