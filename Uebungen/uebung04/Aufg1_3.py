#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:00:20 2022

@author: jerrysmacbookpro
"""


def append_to_book(name, number='---', **book):
    book[name] = number
    return book

def append_to_book2(name, phone_number='---', book=None):
    # You can not use book={} as default argument here. More information on:
    # https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
    if book is None:
        # create a new dictionary
        book = {}

    # add the new entry
    book[name] = phone_number

    return book

mydict = {'Max': '+41763339827'}
mydict = append_to_book('Moritz', '+3123453987', **mydict)
print(mydict)
mydict = append_to_book('Alisha', **mydict)
print(mydict)
mydict = append_to_book('Selina')
print(mydict)

my_book = {'Max': '+41582574111'}
append_to_book2('Moritz', '+41582574112', book=my_book)
print(my_book)
append_to_book2('Susi', book=my_book)
print(my_book)
new_book = append_to_book2('Julia')
print(new_book)
new_book2 = append_to_book2('Romeo')
print(new_book2)
