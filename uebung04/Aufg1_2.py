#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:23:52 2022

@author: jerrysmacbookpro
"""


def vorstellung(**angaben):

    print(f"Ihr Name ist {angaben['Name']}.")
    print(f"Ihr Alter ist {angaben['Alter']}.")
    print(f"Ihr Wohnort ist {angaben['Wohnort']}. ")

    for k, v in angaben.items():
        print(f'Ihr {k} ist {v}.')

    return


vorstellung(Name="Freddy", Alter=22, Wohnort="Arth")
