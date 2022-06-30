# -*- coding: utf-8 -*-
# Aufgabe 4

# 4.1
buch = {
    'Titel': 'Lösungsbuch',
    'Autor': 'Hans Musterlösung',
    'ISBN': 1337,
    'Preis': 10.5,
    }

# 4.2
buch['Erscheinungsjahr'] = 1990

# 4.3
buch['Erscheinungsjahr'] = 1990
print('--- 4.3 ---')
print(buch)

# 4.4
print('--- 4.4 ---')
print(buch['Titel'])
print(buch.get('Titel'))

# 4.5
print('--- 4.5 ---')
zahl = buch.get('Seitenzahl', 0)
print(zahl)
