#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""
Created on Sun May 22 10:51:30 2022

@author: jerrysmacbookpro
"""

import matplotlib.pyplot as plt
import pandas as pd

columns = ["Time", "Temperature", "Humidity", "Air Quality"]
sensData = pd.read_csv('Sensor_0204.csv',
                       delimiter='$',
                       names=columns,
                       index_col='Time',
                       parse_dates=['Time']
                       )

print(sensData)

sensData.plot(subplots=True, grid=True)

meanValues = pd.DataFrame()
for start, end in zip(pd.date_range('2020-01-01', periods=24, freq='MS'),
                      pd.date_range('2020-02-01', periods=24, freq='MS')):
    print('start', start)
    print('end', end)

    m = sensData[start:end].mean()

    m['Time'] = start

    meanValues = meanValues.append(m, ignore_index=True)

meanValues.set_index('Time', inplace=True)

meanValues.plot(subplots=True, grid=True, style='.-')
plt.tight_layout()
