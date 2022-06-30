#!/usr/bin/env python3
# -*- coding: utf-8 -*-


stock = {
    "Apple": 12,
    "Pear": 0,
    "Banana": 6,
    "Cherry": 20,
}

fruit = "Cherry"

if fruit in stock:
    if stock[fruit] == 0:
        print("out of stock")
    else:
        print("in stock")
else:
    print("not in product range")

# %%

age = 99
halbtax = False

if age <= 6:
    price = 0
elif age <= 15 or halbtax:
    price = 135.2 / 2
else:
    price = 135.2

print("Das Billet kostet", price, "CHF")

# %%

# stuff = [1, 4, 9, "hallo", (1, 0.5), 23.5]
stuff = [1, 4, 9, 23.5]

n = 0
while n < len(stuff):
    if isinstance(stuff[n], int) or isinstance(stuff[n], float):
        print(stuff[n])
    else:
        print("invalid list")
        break
    n += 1
    if n == len(stuff):
        print("valid list")

# %%

bom = [
    ["R1", 3.3e3, "Ohm"],
    ["R2", 1000, "Ohm"],
    ["C1", 10e-6, "Farad"],
    ["D1", "1N4148", ""],
]

for name, value, unit in bom:
    print("Das Bauteil", name, "hat den Wert:", value, unit)

bom_dict = {
    "R1": [3.3e3, "Ohm"],
    "R2": [1000, "Ohm"],
    "C1": [10e-6, "Farad"],
    "D1": ["1N4148", ""],
}

for k, v in bom_dict.items():
    print("Das Bauteil", k, "hat den Wert:", v[0], v[1])

# %%

names = ["Selina", "Marlis", "Tamara"]

for n, name in enumerate(names):
    print(n, name)

# %%

starter = ["Suppe", "Salat", "Bruschetta"]
main_dish = ["Roesti mit Leberli", "Fischknusperli", "Spaghetti Carbonara"]
dessert = ["Caramelkoepflie", "Glace", "Tiramisu"]

for s, m, d in zip(starter, main_dish, dessert):
    print(s, m, d, sep=", ")
