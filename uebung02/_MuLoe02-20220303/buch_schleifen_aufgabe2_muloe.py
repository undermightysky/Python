# -*- coding: utf-8 -*-
# Schleifen - Aufgabe 2

step = 1
distance = 0
for n in range(20):
    print('Distance covered:', distance)
    distance += step
    step /= 2
