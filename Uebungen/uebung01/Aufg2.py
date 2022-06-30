#!/usr/bin/env python3
# -*- coding: utf-8 -*-

aaname = 'Jeremy Truttmann'

aanametpl = tuple(aaname)
aanamelst = list(aaname)

x1 = [1, 2, 3, 4, 5, 6, 7, 8]  # list
x2 = (1, 2, 3, 4, 5, 6, 7, 8)  # tuple

title = "The Name of the Rose"  # size = 20
address = ["Frank Fitmann", "Feldstr. 19", "89000 Muenchen"]  # size = 3
nested = [(1, 2, 3, 4, 5, 6, 7, 8)]  # size = 1
isbn = 9783446452084  # size = 1
prices = ["10 CHF", "8 Euro"]  # size = 2
book = [title, "Umberto Eco", isbn, prices]  # size = 4


print(x1[0])
print(x1[-1])
print(book[-1])

title = 'aslas'
address[0] = 'zero'
nested[0] = (1, 2, 3)
isbn = 5
prices[0] = '1CHF'
# book[0] = aaname  -> not possible !!!

address = address[1:]

aanamelst = aanamelst[::-1]

aanamelst = aanamelst[::2]

title = title[::-1]

x1 = [1, 2, 3, 4, 5, 6, 7, 8]  # list

x1 = x1[-2:1:-2]

title = 'Moby Dick'
isbn = 0

s = "thi s"

aanamelst = aanamelst[::-1]
aanameset = set(aaname)
