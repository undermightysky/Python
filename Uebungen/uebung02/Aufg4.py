#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:36:34 2022

@author: jerrysmacbookpro
"""


def primes(maxnumber):
    primelist = []

    for n in range(2, maxnumber):
        for i in range(2, maxnumber + 1):
            if (n % i) == 0 and i != n:
                break
            if i == maxnumber:
                primelist.append(n)

    return primelist


print(primes(1000))
