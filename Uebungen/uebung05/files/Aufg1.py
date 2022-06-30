#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:22:10 2022

@author: jerrysmacbookpro
"""

with open("namen.txt") as n, open("teilnehmer.txt", 'w') as t:
    storage = ''
    for n, cell in enumerate(n, 1):
        if not n % 2:
            t.writelines(''.join((storage.strip(), ' ', cell.strip(), '\n')))
        else:
            storage = cell
