#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:19:17 2023

@author: tj
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


X = {'Temperature': [21, 23, 24, 22, 20, 19, 22],
        'Day':['Monday','Tuesday', 'Wednesday','Thursday', 'Friday','Saturday','Sunday']}

df = pd.DataFrame(data=X)

plt.figure()
plt.plot(df['Day'], df['Temperature'], label='Line 1')       
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.legend()
plt.title('Temperature_city')
plt.legend()
plt.show()



df  = {'Height_(in)': [65,68, 70, 62, 73, 67, 69, 71, 63, 72],
       'Weight_(lbs)': [120, 145, 155, 110, 180 ,135, 160, 170, 115, 175]}


df = pd.DataFrame(data=df)
plt.figure()
plt.scatter(df['Height_(in)'], df['Weight_(lbs)'], label='Line 1')
plt.xlabel('Height_(in)')
plt.ylabel('Weight_(lbs)')
plt.legend()
plt.title('Relationship between height and weight')
plt.show()

df = pd.DataFrame(data=df)
plt.figure()
plt.bar(df['Height_(in)'], df['Weight_(lbs)'], label='Line 1')
plt.xlabel('Height_(in)')
plt.ylabel('Weight_(lbs)')
plt.legend()
plt.title('Relationship between height and weight')
plt.show()


plt.figure
plt.hist(df['Height_(in)'], bins=10)
plt.xlabel('Height_(in)')
plt.title('Height')
plt.show()

