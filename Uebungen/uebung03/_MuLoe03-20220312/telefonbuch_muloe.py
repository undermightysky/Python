# -*- coding: utf-8 -*-
# telefonbuch_muloe.py

from collections import OrderedDict

s = """Maria;Meier;Genf;022 548 95 26
Peter;Müller;Basel;061 498 56 18
Patrick;Huber;Chur;081 445 66 58
Anna;Schmid;St. Gallen;071 216 88 68
Markus;Keller;Winterthur;052 354 87 98
Sandra;Weber;Bern;031 985 46 48
Patrick;Huber;Chur;081 445 66 58
Monika;Schneider;Solothurn;032 468 98 05
Bruno;Fischer;Luzern;041 225 56 85
Silvia;Brunner;Zürich;044 123 65 47
Sandra;Weber;Bern;031 985 46 48
"""

# Create a list of tuples containing the forename and the telephone number.
data = []
for line in s.splitlines():
    entries = line.split(';')
    data.append((entries[0], entries[-1]))
print(data)

# Remove the duplicates but keep the order.
# Since Python 3.6, you can also use the standard dict instead of OrderedDict,
# as it keeps the items in the same order that they were inserted into the
# dictionary.
data_unique = []
for name, phone in OrderedDict(data).items():
    data_unique.append((name, phone))
print(data_unique)

# Same as above, but as list comprehension.
data_unique2 = [(name, phone) for name, phone in OrderedDict(data).items()]

# Alternative solution, but much slower.
data_unique3 = []
for name, phone in data:
    if (name, phone) not in data_unique3:
        data_unique3.append((name, phone))
