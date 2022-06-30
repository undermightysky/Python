#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:04:59 2022

@author: jerrysmacbookpro
"""

d = {"flower": "lily", "color": "turquoise", "fish": "clownfish"}
t = (2020, 3, 4)
p = "1001.90 CHF"

try:
    d["dish"]  # KeyError
    tup[0]  # NameError
    t[3]  # IndexError
    float(p)  # ValueError
    c = t + p  # Type Error
    t[0] = 2021  # TypeError

except ValueError:
    print("Value Error")

except KeyError:
    print("Key Error")

except NameError:
    print("Name Error")

except IndexError:
    print("Index Error")

except TypeError:
    print("Type Error")

except Exception as e:
    print(str(e))

# %%

my_list = [0, 1, 2, 3, "a", "b", "c"]

try:
    for value in my_list:
        r_value = 1/value
        print(f"Reziproker Wert von {value} ist {r_value}")

except ZeroDivisionError:
    print("Divided by zero !")

except TypeError:
    print("Type Error")
