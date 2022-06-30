#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:38:20 2022

@author: jerrysmacbookpro
"""
class PhoneBook():

    def __init__(self, data=None):
        if data is None:
            self._d = {}
        else:
            self._d = data.copy()

    def add(self, name, number):
        self._d[name] = number

    def remove(self, name, number):
        self._d.pop(name)

    def __str__(self):
        return '\n'.join(f'{name}: {self._d[name]}'
                         for name in sorted(self._d.keys()))

    def __contains__(self, term):
        return term in self._d.keys() or term in self._d.values()

    def __getitem__(self, term):
        return {k: v
                for k, v in self._d.items()
                if term == k or term == v}



mybook = PhoneBook({"Marlis": "+41 133 13 13", "Christian": "+41 555 66 66"})
print(mybook)

mil = mybook.__getitem__('Marlis')
print(mil)
