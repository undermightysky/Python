#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:05:03 2022

@author: jerrysmacbookpro
"""


class MeasuringInstrument(object):

    instruments = {}

    def __init__(self, inventory_number, name):
        self._inventory_number = inventory_number
        self._name = name
        MeasuringInstrument.instruments[inventory_number] = {'name': name}

    def __del__(self):
        MeasuringInstrument.instruments.pop(self._inventory_number)

    @property
    def inventory_number(self):
        return self._inventory_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        MeasuringInstrument.instruments[self.inventory_number]['name'] = name


fluke1 = MeasuringInstrument(113344, 'Fluke')

print(fluke1.name)
print(fluke1.inventory_number)
print(fluke1.instruments)

print(MeasuringInstrument.instruments)

inst1 = MeasuringInstrument(inventory_number=64581, name='Fluke 85')
print(inst1.inventory_number)
print(inst1.name)

print(MeasuringInstrument.instruments)

inst2 = MeasuringInstrument(inventory_number=301991, name='HP 34401A')

print(MeasuringInstrument.instruments)

del inst1
print(MeasuringInstrument.instruments)

inst2.name = 'Keysight 34470A'
print(MeasuringInstrument.instruments)
