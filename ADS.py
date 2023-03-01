#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:55:08 2023

@author: tj
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('Sleep_Efficiency.csv')


# Set the index of the DataFrame to the 'Week' column
df.set_index('Bedtime', inplace=True)

# Create a line plot with multiple lines
df.plot(y=['Caffeine consumption', 'Alcohol consumption'], kind='line', figsize=(10, 6))

# Set the title and axis labels
plt.title('Sleep Efficiency by Participant')
plt.xlabel('Week')
plt.ylabel('Sleep Efficiency')

# Show the plot
plt.show()

counts = df['Smoking status'].value_counts()
plt.figure()
plt.bar(x=counts.index, height=counts.values, color='green')
plt.xlabel("Smoking status", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.title("Number of smokers and non-smokers", fontsize=10)
plt.show()

# Convert 'Alcohol consumption' column to numerical format
alcohol_mapping = {'None': 0, 'Low': 1, 'Moderate': 2, 'High': 3}
df['Alcohol consumption'] = df['Alcohol consumption'].map(alcohol_mapping)

# Create a boxplot showing the relationship between alcohol consumption and sleep efficiency
alcohol_mapping = {'None': 0, 'Low': 1, 'Moderate': 2, 'High': 3}
df['Alcohol consumption'] = df['Alcohol consumption'].map(alcohol_mapping)

# Create a boxplot showing the relationship between alcohol consumption and sleep efficiency
plt.scatter(df['Age'], df['Sleep efficiency'])

# Add axis labels and title
plt.xlabel('Age')
plt.ylabel('sleep efficiency')
plt.title('Relationship between Age and Income')

# Show the plot
plt.show()







