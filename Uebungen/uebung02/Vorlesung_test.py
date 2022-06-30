#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:42:41 2022

@author: jerrysmacbookpro
"""

myvar = 9

if myvar > 13:
    print("myvar is greater than 13")
elif myvar > 11:
    print("mvar is greater than 11")
else:
    print("myvar is smaller than 10")

# %%

liste = [1, 2, 3]


if liste == [1, 2, 3]:
    print("Objektgleichheit")
else:
    print("keine Objektgleichheit")

x = None

if x is None:
    print("none found")

# %%

y = 0b00110011
z = 0b00110011

if y and z:
    print("Werte identisch")

# %%

text = "Eins, Zwei, Drei, Dreizehn"

if "Dreizehn" in text:
    print("Dreizehn gefunden")

for zahl in liste:
    print(zahl)

for n in range(14):
    print(n, "hihi")

liste2 = range(2, 20, 2)

for q in liste2:
    print(q)

# %%
t = 0
while t < 5:
    t += 2
print("t ist", t)

n = 0
while n < 6:
    n += 1
    if n == 3:
        print("continue")
        continue
    print(n)

n = 0
while n < 6:
    n += 1
    if n == 3:
        print("break")
        break
    print(n)


# %%
def begruessung(vorname, nachname):
    '''Grüsst Person'''
    print("Guten Morgen", vorname, nachname)
    return


begruessung("Jeremy", "Truttmann")

help(begruessung)

begruessung(nachname="Koch", vorname="Selina")

# %%

liste5 = [(3, 2), (3, 0), (3, 1)]
liste5.sort(key=lambda x: sum(x))
print(liste5)
