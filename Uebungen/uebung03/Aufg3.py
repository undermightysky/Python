#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:51:42 2022

@author: jerrysmacbookpro
"""

telefonbuchstr = """Maria;Meier;Genf;022 548 95 26
                Peter;Mueller;Basel;061 498 56 18
                Patrick;Huber;Chur;081 445 66 58
                Anna;Schmid;St. Gallen;071 216 88 68
                Markus;Keller;Winterthur;052 354 87 98
                Sandra;Weber;Bern;031 985 46 48
                Patrick;Huber;Chur;081 445 66 58
                Monika;Schneider;Solothurn;032 468 98 05
                Bruno;Fischer;Luzern;041 225 56 85
                Silvia;Brunner;Zuerich;044 123 65 47
                Sandra;Weber;Bern;031 985 46 48"""
telefonbuch = []

for string in telefonbuchstr.splitlines():
    string = string.strip()
    vorname = string.split(";")[0]
    telefonnr = string.split(";")[3]
    if((telefonbuch.count((vorname, telefonnr)) < 1)):
        telefonbuch.append((vorname, telefonnr))

print(telefonbuch)
