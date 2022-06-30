#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:52:33 2022

@author: jerrysmacbookpro
"""
values_as_string = ["3", "20.3", "-7.14", "-55.5", "0.1"]
print(values_as_string)
values = [float(value) for value in values_as_string]
print(values)

# %%

values = [3, 20.3, -7.14, -55.5, 0.1]
pos_values = [v for v in values if v >= 0]
print(pos_values)

# %%

words = ["Schule", "Bücher", "Laptop", "Fläche"]
umlaut = [w for w in words for u in "äöü" if u in w.lower()]
umlaut = [w for w in words if any(u in w.lower() for u in 'äöü')]
print(umlaut)

# %%

list1 = ["A", "B", "C"]
list2 = ["D", "E", "F"]
print([(a, b) for a in list1 for b in list2])

numbers = [1, 2, 3, 4, 5, 6]
print({n**3 for n in numbers if n % 2})

chars = ["A", "B", "C"]
quantity = [2, 3, 4]
print({c: [c*n for n in quantity] for c in chars})

print([n for n in range(2, 20)
       if all(n % m for m in range(2, int(n**0.5) + 1))])

superheros = ["Superman", "Batman", "Spiderman", "Wolverine", "Superwoman"]
heroes = {h: len(h) for h in superheros if 'man' in h}
print(heroes)

superheros = ['Superman', 'Batman', 'Spiderman', 'Wolverine', 'Superwoman']

sh = {name: len(name) for name in superheros}
sh_man = {name: len(name) for name in superheros if name.endswith('man')}
