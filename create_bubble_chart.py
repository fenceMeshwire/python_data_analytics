#!/usr/bin/env python3

# Python 3.9.5

# create_bubble_chart.py

# Purpose: Concept for creating a bubble chart

# Dependencies
import matplotlib.pyplot as plt
import pandas as pd

heading = ["City", "Country Code", "Inhabitants", "Latitude", "Longitude"]

# Data
df = pd.DataFrame(columns=heading)
df.loc[len(df.index)] = ['Munich', 'DE', 1.472, 48.137154, 11.576124]
df.loc[len(df.index)] = ['Berlin', 'DE', 3.645, 52.520008, 13.404954]
df.loc[len(df.index)] = ['Copenhagen', 'DK', 0.602, 55.676098, 12.568337]

x = [df['Longitude'][i] for i in range(len(df))]
y = [df['Latitude'][i] for i in range(len(df))]

population =  [1000 * df['Inhabitants'][i] for i in range(len(df))]
colors = [0.1 * df['Inhabitants'][i] for i in range(len(df))]
cities = [df['City'][i] for i in range(len(df))]

pop_million = [int(1000000 * df['Inhabitants'][i]) for i in range(len(df))]

plt.scatter(x, y, c=colors, s=population, alpha=0.3, cmap='viridis')
plt.xlim(round(min(x)) - 2, round(max(x) + 2)) # x_min, x_max
plt.ylim(round(min(y)) - 2, round(max(y) + 2)) # y_min, y_max

cbar = plt.colorbar(ticks=colors)
cbar.set_ticklabels(pop_million)

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.show()
