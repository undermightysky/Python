#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:28:52 2022

@author: jerrysmacbookpro
"""
import string

with open('zen.txt') as f:
    text = f.read().lower()

    chars = {c: text.count(c) for c in string.ascii_lowercase}

    print(chars)
    chars_sorted = sorted(chars.keys(), key=chars.get, reverse=True)

    print(chars_sorted)
