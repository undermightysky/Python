#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
Created on Wed May 18 17:42:56 2022

@author: jerrysmacbookpro
"""

import pandas as pd

cities = ['Vienna', 'Vienna', 'Vienna',
          'Hamburg', 'Hamburg', 'Hamburg',
          'Berlin', 'Berlin', 'Berlin',
          'Zürich', 'Zürich', 'Zürich']

data = ['Austria', 414.60, 1805681,
        'Germany', 755, 1760433,
        'Germany', 891.85, 3562166,
        'Switzerland', 87.88, 378884]

index = [cities, ['country', 'area', 'population',
                  'country', 'area', 'population',
                  'country', 'area', 'population',
                  'country', 'area', 'population']]

city_series = pd.Series(data, index=index)

print(city_series)

print(city_series)
print(type(city_series))
