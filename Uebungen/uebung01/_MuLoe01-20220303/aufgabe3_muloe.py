# -*- coding: utf-8 -*-
# Aufgabe 3

# 3.1
my_list = [1, 1, 3, 5, 'a', 'a']
my_set = {1, 1, 3, 5, 'a', 'a'}
print('--- 3.1 ---')
print(my_list)
print(my_set)

# 3.2
name = 'Hans Musterlösung'
print('--- 3.2 ---')
print(set(name))

# 3.3
print('--- 3.3 ---')
n = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primes = {2, 3, 5, 7}
primes.add(11)
print(primes)
x = n.intersection(primes)
print(x)
y = n.difference(primes)
print(y)
n.difference_update(primes)
print(n)
