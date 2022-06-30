# -*- coding: utf-8 -*-
# zahlensysteme_muloe.py

basis = int(input('Basis: '))
zahl = input('Zahl: ')
zahl_dezimal = int(zahl, basis)
print('Zahl', zahl, 'mit der Basis', basis, '=>', zahl_dezimal)
