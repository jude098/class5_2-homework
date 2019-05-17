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
import numpy as np
import pandas as pd
import os

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

wine = pd.read_csv(filepath_or_buffer='/users/.../downloads/winedata2.csv',
                      sep=',',
                      header=0)

pretty_print("wine dataframe", wine.to_string())
pretty_print("wine columns", wine.columns)


os.makedirs('plots', exist_ok=True)

#Plotting line chart

plt.plot(wine['Alcohol'], color='green')
plt.title('Alcohol by Index')
plt.xlabel('Index')
plt.ylabel('Alcohol')
plt.show()
plt.savefig(f'plots/alcohol_by_index_plot.png', format='png')

#Plotting scatterplot

plt.scatter(wine['Proline'],wine['Acl'], color='b')
plt.title('Proline to Ash')
plt.xlabel('Proline')
plt.ylabel('Ash')
plt.show()
plt.savefig(f'plots/proline_by_Ash_plot.png', format='png')
