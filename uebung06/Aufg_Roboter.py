#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:31:21 2022

@author: jerrysmacbookpro
"""
import time


class Robot(object):

    _stringwerte = {
        (False, False): 'Ausgelaugt',
        (False, True): 'Super!',
        (True, False): 'In Anbetracht meines Alters nicht so schlecht!',
        (True, True): 'Super. Vor allem in Anbetracht meines Alters!'
    }

    def __init__(self, name, position, orientation, baujahr, energie):
        self.name = name
        self.position = position
        self.orientation = orientation
        self.baujahr = baujahr
        self.energie = energie

    def move(self,  distance):
        if self.orientation == 'east':
            self.position[0] += distance
        if self.orientation == 'west':
            self.position[0] -= distance
        if self.orientation == 'north':
            self.position[1] += distance
        if self.orientation == 'south':
            self.position[1] -= distance

    @property
    def befinden(self):
        alter = time.localtime().tm_year - self.baujahr
        choice = (alter > 20, self.energie >= 50)
        return Robot._stringwerte.get(choice)

    @property
    def name(self):
        print('name returned')
        return self._name

    @name.setter
    def name(self, name):
        print('name set')
        self._name = name[0:10] if name != 'Hugo' else 'Marvin'

    @property
    def orientation(self):
        print('orientation returned')
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        print('orientation set')
        self._orientation = orientation


a = Robot("Hugo", [0, 0], 'east', 1999, 15)
b = Robot("Will", [100, 110], 'west', 2001, 75)
x = Robot("Marvin", [3, 4], 'south', 2005, 25)
y = Robot("HansPeterMüller", [5, 6], 'north', 2008, 99)

print(a.name, a.position, a.orientation, a.baujahr)
print(b.name, b.position, b.orientation, b.baujahr)
print(x.name, x.position, x.orientation, x.baujahr)
print(y.name, y.position, y.orientation, y.baujahr)

a.move(10)
b.move(0)
x.move(10)
y.move(10)


print(a.position)
print(b.position)
print(x.position)
print(y.position)

print(f"{a.name}: {a.befinden}")
print(f"{b.name}: {b.befinden}")
print(f"{x.name}: {x.befinden}")
print(f"{y.name}: {y.befinden}")
