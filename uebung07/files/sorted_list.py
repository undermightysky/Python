#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:42:17 2022

@author: jerrysmacbookpro
"""


class SortedList(list):
    def __init__(self, x=None):
        super().__init__(x or [])
        super().sort()

    def append(self, object):
        super().append(object)
        super().sort()

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        super().sort()


s = SortedList([1, 8, 4, 6, 2])
print(s)

s.append(13)
print(s)

s.pop(3)
print(s)
