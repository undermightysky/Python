#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:20:38 2022

@author: jerrysmacbookpro
"""
import pandas as pd


persons = {'Name': ['Willy', 'Henry', 'Jason', 'Karin'],
           'Sizes': [179, 165, 172, 158],
           'Weights': [65, 58, 58, 55]
           }

data = pd.DataFrame(persons, columns=['Weights', 'Sizes'],
                    index=persons['Name'])

print(data)

bmi = data.Weights / ((data.Sizes/100) ** 2)

bmi_good = data.loc[(20 < bmi) & (bmi < 25)]

print(bmi_good)



# AUFG 4
print(data.loc[data.index.str.contains('i')])


# AUFG 5

data.insert(loc=len(data.columns), column='BMI', value=bmi.values)
print(data)

# AUFG 6

print(data.sort_values('BMI',ascending=False))

# AUFG 7

print(data.loc[(18.5 < data['BMI']) & (data['BMI'] < 23)
               & data.index.str.contains('a')])
