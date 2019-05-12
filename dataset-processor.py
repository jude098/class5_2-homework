#!/usr/bin/env python3

#load the dataset

import numpy as np
import pandas as pd

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Computing data
wine = pd.read_csv(filepath_or_buffer='/.../downloads/winedata2.csv',
                      sep=',',
                      header=0)
print(wine)


#compute and print summary statistics

wine = pd.read_csv(filepath_or_buffer='/.../downloads/winedata2.csv',
                      sep=',',
                      header=0)

#Create a DataFrame
pd.DataFrame(wine)
print(wine.describe())



#visualize the data
import pandas as pd
import os


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Loading dataset
wine = pd.read_csv(filepath_or_buffer='/.../downloads/winedata2.csv',
                      sep=',',
                      header=0)


#Creating plots
os.makedirs('plots', exist_ok=True)

## Plotting line chart
pretty_print("wine dataframe", wine.to_string())
pretty_print("wine columns", wine.columns)

import os

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(wine['Wine'], color='red')
plt.title('Wine by Alcohol')
plt.xlabel('Wine')
plt.ylabel('Alcohol')
plt.savefig(f'plots/wine_by_alcohol_plot.png', format='png')
plt.clf()
#
#
#
# # Plotting scatterplot
# plt.scatter(housing_df['rm'], housing_df['tax'], color='b')
# plt.title('rm to tax')
# plt.xlabel('rm')
# plt.ylabel('tax')
# plt.savefig(f'plots/charges_to_tax.png', format='png')
