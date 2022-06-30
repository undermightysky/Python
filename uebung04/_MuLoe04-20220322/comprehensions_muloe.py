# -*- coding: utf-8 -*-

values_as_string = ['3', '20.3', '-7.14', '-55.5', '0.1']

values = [float(v) for v in values_as_string]

# ---

pos_values = []
for v in values:
    if v >= 0:
        pos_values.append(v)

pos_values = [v for v in values if v >= 0]

# ---

words = ['Schule', 'Bücher', 'Laptop', 'Fläche', 'Gehäusegrösse']

umlaut = []
for w in words:
    for u in 'äöü':
        if u in w.lower():
            umlaut.append(w)
            break

# Beachte, dass das Argument der any-Funktion in diesem Fall ein Generator-
# Ausdruck ist. Somit kann die any-Funktion schon beim Auftreten des ersten
# True den Rückgabewert liefern. So werden überflüssige Tests/Durchgänge
# vermieden, ähnlich wie dies mit dem obigen break gelöst wird.
umlaut = [w for w in words if any(u in w.lower() for u in 'äöü')]

# ---

list1 = ['A', 'B', 'C']
list2 = ['D', 'E', 'F']
print([(a, b) for a in list1 for b in list2])

# ---

numbers = [1, 2, 3, 4, 5, 6]
print({n**3 for n in numbers if n % 2})

# ---

chars = ['A', 'B', 'C']
quantity = [2, 3, 4]
print({c: [c*n for n in quantity] for c in chars})

# ---

print([n for n in range(2, 20)
       if all(n % m for m in range(2, int(n**0.5) + 1))])

# ---

superheros = ['Superman', 'Batman', 'Spiderman', 'Wolverine', 'Superwoman']

sh = {name: len(name) for name in superheros}
sh_man = {name: len(name) for name in superheros if name.endswith('man')}
