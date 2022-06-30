# -*- coding: utf-8 -*-
# Verzweigungen - Aufgabe 2

years = [
    2000,
    2004,
    2020,
    2100,
    2104,
]

for year in years:
    ly = (not (year % 4) and (year % 100)) or not (year % 400)
    print(year, 'is', 'a leap year.' if ly else 'not a leap year.')
