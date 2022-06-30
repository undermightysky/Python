# -*- coding: utf-8 -*-
# verzweigungen_und_schleifen.py

# ---

stock = {
    "Apple": 12,
    "Pear": 0,
    "Banana": 6,
    "Cherry": 20,
}

fruit = 'Pear'

if fruit in stock:
    print('in stock')
else:
    print('not in product range')

# ---

if fruit in stock:
    if stock[fruit] > 0:
        print('in stock')
    else:
        print('out of stock')
else:
    print('not in product range')

# ---

age = 25
halbtax = False
full_price = 135.2

if age <= 6:
    price = 0
elif age <= 16 or halbtax:
    price = full_price/2
else:
    price = full_price

print('Ticket price: CHF', price)

# ---

stuff = [1, 4, 9, "hallo", (1, 0.5), 23.5]

for item in stuff:
    if isinstance(item, (int, float)):
        print(item)

# ---

for item in stuff:
    if isinstance(item, (int, float)):
        print(item)
    else:
        print('invalid list')
        break
else:
    print('valid list')
