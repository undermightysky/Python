#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:05:56 2022

@author: jerrysmacbookpro
"""

var1 = 256
var2 = 7.98765
var3 = 2800031
var4 = 0.0000000089
var5 = "NEWS"
length = 2.35

"""
0x0100
7.9877
2,800,031.00
8.9e-09
+++NEWS+++
length = 2.350
"""

print(f"{var1:#06x}")
print(f"{var2:4.5}")
print(f"{var3:,.2f}")
print(f"{var4:1.2}")
print(f"{var5:+^10}")
print("lenght =", f"{length:3.4}")
