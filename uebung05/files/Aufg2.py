#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:46:51 2022

@author: jerrysmacbookpro
"""


def save_parameters(data, fname, encoding="utf-8"):
    with open(fname, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}={value}\n")


gui_settings = {
    "language": "English",
    "size": (700, 500),
    "dpi": 96,
    "save_on_exit": True,
}

save_parameters(gui_settings, 'test.txt')


# %%

def load_parameters(fname, encoding="utf-8"):
    with open(fname, 'r') as fdata:
        fdict = {}
        for fitem in fdata.readlines():
            fitem = fitem.split('=')
            if len(fitem) != 2:
                continue
            fdict[fitem[0].strip()] = fitem[1].strip()

    return fdict


print(load_parameters('settings2.txt'))
