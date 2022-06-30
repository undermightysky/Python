# -*- coding: utf-8 -*-
# Aufgabe 2

# 2.1
name = 'Hans Musterlösung'

# 2.2
name_tuple = tuple(name)

# 2.3
name_list = list(name)

# 2.4
print('--- 2.4 ---')
print('length of string:', len(name))
print('length of tuple:', len(name_tuple))
print('length of list:', len(name_list))

# 2.5
x1 = [1, 2, 3, 4, 5, 6, 7, 8]
x2 = (1, 2, 3, 4, 5, 6, 7, 8)
title = 'The Name of the Rose'
address = ['Frank Fitmann', 'Feldstr. 19', '89000 Muenchen']
nested = [(1, 2, 3, 4, 5, 6, 7, 8)]
isbn = 9783446452084
prices = ['10 CHF', '8 Euro']
book = [title, 'Umberto Eco', isbn, prices]
print('--- 2.5 ---')
print('length of x1:', len(x1))
print('length of x2:', len(x2))
print('length of title:', len(title))
print('length of address:', len(address))
print('length of nested:', len(nested))
print('length of prices:', len(prices))
print('length of book:', len(book))

# 2.6
print('--- 2.6 ---')
print('type of x1:', type(x1))
print('type of x2:', type(x2))
print('type of title:', type(title))
print('type of address:', type(address))
print('type of nested:', type(nested))
print('type of isbn:', type(isbn))
print('type of prices:', type(prices))
print('type of book:', type(book))

# 2.7
x1[0]

# 2.8
x1[-1]

# 2.9
x1[0] = 10
# x2[0] = 10 Fehler tuple sind unveränderlich
# title[0] = 10 Fehler str sind unveränderlich
address[0] = 10
nested[0] = 10
# isbn[0] Fehler integer sind nicht indizierbar
prices[0] = 10
book[0] = 10

# 2.10
print('--- 2.10 ---')
print(x1[::2])

# 2.11
print('--- 2.11 ---')
print(title[::-1])

# 2.12
print('--- 2.12 ---')
print(x1[6:1:-2])
print(x1[-2:1:-2])

# 2.13
title = 'Moby Dick'
isbn = 0
print('--- 2.13 ---')
print(book)

# 2.14
prices[0] = '11 CHF'
print('--- 2.14 ---')
print(book)

# 2.15
t = (4, 7, 9)
s = 'Ich bin ein String'
l = [45, 98, '787', [3, 4]]
t2 = (4, 8, [45, 98])
t[0]
# t[3] Tuple index out of range
# t(3) Tuple object is not callable
s[4]
# s[4] = 'x' 'str' object does not support item assignment
# l[2][0] = 'g' 'str' object does not support item assignment
l[3][0] = 'g'
l
t2[2][0]
