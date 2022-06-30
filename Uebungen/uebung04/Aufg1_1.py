#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:07:00 2022

@author: jerrysmacbookpro
"""


def rms(*values):

    lst = [number**2 for number in values if isinstance(number, (int, float))]

    if not lst:
        raise TypeError("to few numeric arguments")

    return (sum(lst)/len(lst))**0.5


print(rms(3, 13, 14, 18))
